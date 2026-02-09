
import streamlit as st
import json
import random
from pathlib import Path

from .session import get_collection
from .profiles import get_completed_ids

@st.cache_data(ttl=3600)  # Cache for 1 hour
def _load_raw_blinded_outputs(results_base: Path = Path("results"), language: str = "it") -> dict:
    """Cache the JSON file loading and parsing (slow I/O operation).
    
    Args:
        results_base: Base results directory
        language: 'it' for Italian (translated_results), 'en' for English (original results)
    
    Returns dict of {model_name: [outputs]}.
    """
    outputs_by_model = {}
    
    if not results_base.exists():
        return outputs_by_model
    
    translated_base = results_base / "translated_results"
    
    # Use glob to find all blinded_outputs.json files directly
    # This avoids iterating over directories that don't contain the target file
    # Pattern: results/*/blinded_outputs.json
    json_files = sorted(results_base.glob("*/blinded_outputs.json"))
    
    for source_file in json_files:
        model_dir_name = source_file.parent.name
        
        # Skip translated_results directory itself if picked up (though unlikely with strict structure)
        if model_dir_name == "translated_results":
             continue

        # Check if a translated version exists for this model in the target language directory
        # Structure: results/translated_results/<language>/<model>/blinded_outputs.json
        translated_file = translated_base / language / model_dir_name / "blinded_outputs.json"
        
        # Language-based selection:
        # - Non-English: prefer translated if available, fall back to original
        # - English: always use original (effectively skips this block as language='en' won't be found usually, or will be same)
        if language != "en" and translated_file.exists():
            final_file = translated_file
        else:
            final_file = source_file
        
        try:
            with open(final_file) as f:
                outputs = json.load(f)
                outputs_by_model[model_dir_name] = outputs
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading {final_file}: {e}")
            continue
    
    return outputs_by_model

def get_evaluation_counts(results_base: Path = Path("results")) -> dict:
    """Get count of evaluations per output_id."""
    counts = {}
    
    # 1. MongoDB Counts
    coll = get_collection("reviews")
    if coll is not None:
        try:
            pipeline = [
                {"$group": {"_id": "$output_id", "count": {"$sum": 1}}}
            ]
            for doc in coll.aggregate(pipeline):
                counts[doc["_id"]] = doc["count"]
        except Exception as e:
            print(f"MongoDB Count Error: {e}")
            
    # 2. Local Fallback (Merge/Add)
    reviews_file = results_base / "expert_reviews.json"
    if reviews_file.exists():
        try:
            with open(reviews_file) as f:
                local_reviews = json.load(f)
                for r in local_reviews:
                    oid = r.get("output_id")
                    if oid:
                        counts[oid] = counts.get(oid, 0) + 1
        except Exception as e:
            print(f"Local Reviews Count Error: {e}")
            
    return counts

def load_blinded_outputs(reviewer_id: str = None, results_base: Path = Path("results"), language: str = "it") -> list:
    """Load all blinded outputs, filtered by max evaluations and grouped.
    
    Structure:
    [Separator(Visit A), Visit A Model Agentic 1, Visit A Model ZeroShot 1, ..., Separator(Visit B), ...]
    
    Randomization:
    - Visit order seeded by reviewer_id
    - Model order within visit seeded by reviewer_id + visit_id
    """
    
    LIMIT_PER_EXAMPLE = 30
    
    if not results_base.exists():
        return []
    
    # Get current language from session state
    language = st.session_state.get('language', 'it')
    
    # Load and parse JSON files (cached part is in _load_raw_outputs)
    raw_outputs_by_model = _load_raw_blinded_outputs(results_base, language=language)
    
    # Get Counts (Global Limit)
    eval_counts = get_evaluation_counts(results_base)

    # Get Completed IDs (User Limit)
    completed_ids = set()
    if reviewer_id:
        completed_ids = get_completed_ids(reviewer_id, results_base)
    
    # 1. Flatten to list of dicts with 'visit_id'
    all_items = []
    
    for model, outputs in raw_outputs_by_model.items():
        for output in outputs:
            output_id = output.get('id', '')
            if not output_id:
                continue
            
            # CHECK LIMIT (Global)
            if eval_counts.get(output_id, 0) >= LIMIT_PER_EXAMPLE:
                continue

            # CHECK HISTORY (User)
            if output_id in completed_ids:
                continue
            
            # Extract visit_id
            if '_' in output_id:
                visit_id = output_id.rsplit('_', 1)[0]
            else:
                visit_id = output_id
            
            # Skip outputs without ESI prediction
            if output.get('esi_level') is None:
                continue
            
            all_items.append({
                'type': 'review',
                'output_id': output_id,
                'visit_id': visit_id,
                'model': model,
                'output': output
            })
            
    # 2. Group by visit_id
    visits = {}
    for item in all_items:
        v_id = item['visit_id']
        if v_id not in visits:
            visits[v_id] = []
        visits[v_id].append(item)
        
    # 3. Sort visits randomly (seeded by reviewer_id)
    visit_ids = list(visits.keys())
    visit_ids.sort() # Ensure stable starting point before shuffle
    
    if reviewer_id:
        rng = random.Random(reviewer_id)
        rng.shuffle(visit_ids)
    
    final_forms = []
    form_idx = 0
    
    for v_id in visit_ids:
        # 5. Interleaved Random Sort: Agentic (_B) / Zero-Shot (_A)
        # Requirement: Alternating A-Z order, but randomized within each category.
        
        visit_items = visits[v_id]
        
        agentic_items = []
        zeroshot_items = []
        others = []
        
        for item in visit_items:
            oid = item.get('output_id', '')
            if oid.endswith('_B'):
                agentic_items.append(item)
            elif oid.endswith('_A'):
                zeroshot_items.append(item)
            else:
                others.append(item)
                
        # Skip if no items after filtering
        if not agentic_items and not zeroshot_items and not others:
            continue
            
        # Randomize within categories
        if reviewer_id:
            visit_seed = f"{reviewer_id}_{v_id}"
            rng_visit = random.Random(visit_seed)
            rng_visit.shuffle(agentic_items)
            rng_visit.shuffle(zeroshot_items)
            rng_visit.shuffle(others)
            
        # Truncate to ensure equal pairs (avoid orphans)
        min_len = min(len(agentic_items), len(zeroshot_items))
        
        # Only keep pairs
        agentic_items = agentic_items[:min_len]
        zeroshot_items = zeroshot_items[:min_len]
        
        # Interleave: Agentic first, then Zero-Shot
        interleaved_items = []
        
        for i in range(min_len):
            interleaved_items.append(agentic_items[i])
            interleaved_items.append(zeroshot_items[i])
                
        # Append any others 
        interleaved_items.extend(others)
        
        # If after filtering and pairing we have nothing, skip this visit
        if not interleaved_items:
            continue

        # 4. Insert Separator (ONLY if we have content)
        separator = {
            'type': 'separator',
            'visit_id': v_id
        }
        
        # Extract patient context from the first available output for this visit
        if interleaved_items and 'output' in interleaved_items[0]:
             first_output = interleaved_items[0]['output']
             if 'demographics' in first_output:
                 separator['demographics'] = first_output['demographics']
             if 'patient_overview' in first_output:
                 separator['patient_overview'] = first_output['patient_overview']

        final_forms.append(separator)
        
        for item in interleaved_items:
            form_idx += 1
            item['form_id'] = form_idx
            final_forms.append(item)
    
    return final_forms

