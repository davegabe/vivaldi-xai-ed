
import json
from pathlib import Path
from .session import get_collection

def save_user_profile(reviewer_id: str, profile: dict, output_dir: Path = Path("results")):
    """Save user profile to MongoDB (fallback to file)."""
    # 1. Try MongoDB
    coll = get_collection("user_profiles")
    if coll is not None:
        try:
            coll.update_one(
                {"_id": reviewer_id},
                {"$set": profile},
                upsert=True
            )
            return
        except Exception as e:
            print(f"MongoDB Profile Save Error: {e}")

    # 2. Fallback to File
    output_dir.mkdir(parents=True, exist_ok=True)
    profiles_file = output_dir / "user_profiles.json"
    
    profiles = {}
    if profiles_file.exists():
        try:
            with open(profiles_file) as f:
                profiles = json.load(f)
        except Exception:
            pass
            
    profiles[reviewer_id] = profile
    
    with open(profiles_file, "w") as f:
        json.dump(profiles, f, indent=2)

def load_user_profile(reviewer_id: str, output_dir: Path = Path("results")) -> dict:
    """Load user profile from MongoDB (fallback to file)."""
    # 1. Try MongoDB
    coll = get_collection("user_profiles")
    if coll is not None:
        try:
            doc = coll.find_one({"_id": reviewer_id})
            if doc:
                return doc
        except Exception as e:
            print(f"MongoDB Profile Load Error: {e}")

    # 2. Fallback to File
    profiles_file = output_dir / "user_profiles.json"
    
    if not profiles_file.exists():
        return None
        
    try:
        with open(profiles_file) as f:
            profiles = json.load(f)
            return profiles.get(reviewer_id)
    except Exception:
        return None

def get_completed_count(reviewer_id: str, output_dir: Path = Path("results")) -> int:
    """Get count of completed reviews for a user."""
    # 1. Try MongoDB
    coll = get_collection("reviews")
    if coll is not None:
        try:
            return coll.count_documents({"reviewer_id": reviewer_id})
        except Exception as e:
            print(f"MongoDB Count Error: {e}")
            
    # 2. Fallback to File
    reviews_path = output_dir / "expert_reviews.json"
    if reviews_path.exists():
        try:
            with open(reviews_path) as f:
                all_reviews = json.load(f)
                return len([r for r in all_reviews if r.get("reviewer_id") == reviewer_id])
        except Exception:
            pass
    return 0

def get_completed_ids(reviewer_id: str, output_dir: Path = Path("results")) -> set:
    """Get set of output_ids completed by a user."""
    # 1. Try MongoDB
    coll = get_collection("reviews")
    if coll is not None:
        try:
            return set(doc["output_id"] for doc in coll.find({"reviewer_id": reviewer_id}, {"output_id": 1}))
        except Exception as e:
            print(f"MongoDB IDs Error: {e}")
            
    # 2. Fallback to File
    completed_ids = set()
    reviews_path = output_dir / "expert_reviews.json"
    if reviews_path.exists():
        try:
            with open(reviews_path) as f:
                all_reviews = json.load(f)
                for r in all_reviews:
                    if r.get("reviewer_id") == reviewer_id and "output_id" in r:
                        completed_ids.add(r["output_id"])
        except Exception:
            pass
    return completed_ids
