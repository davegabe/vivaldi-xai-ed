"""
Agent Orchestrator - Iterative agentic pipeline (Doctor-Centric).
"""

import time
import json
import concurrent.futures
from typing import Optional
import traceback
import re

from ..data.schema import PatientVisit, VitalSignSeries
from ..logging import get_logger
from .doctor import DoctorAgent
from .consultant import ConsultantAgent
from .coder import CoderAgent
from .synthesizer import SynthesizerAgent
from .triage import TriageAgent
from ..prompts import (
    IterationHistory,
    CalculationResult,
    AgentOutput,
    ImageReview
)

class AgentOrchestrator:
    """
    Orchestrates the "Clinical Team" pipeline.
    
    Architecture (Doctor Centric):
    Phase 0: Triage (Automated Baselines + Plot)
    Phase 1: Clinical Rounds (Doctor leads, Consultant advises)
    Phase 2: Execution (Coder)
    Phase 3: Synthesis (Synthesizer)
    """
    
    MAX_ITERATIONS = 3
    
    def __init__(self, model_key: Optional[str] = None):
        self.triage = TriageAgent(model_key)
        self.doctor = DoctorAgent(model_key)
        self.consultant = ConsultantAgent(model_key)
        self.coder = CoderAgent(model_key)
        self.synthesizer = SynthesizerAgent(model_key)
        self.logger = get_logger()
    
    def process_visit(
        self,
        patient: PatientVisit,
        vitals: Optional[VitalSignSeries] = None,
        pmh: Optional[list[str]] = None,
        meds: Optional[list[str]] = None,
        progress_callback=None,
    ) -> AgentOutput:
        """
        Process a patient visit through the Clinical Team pipeline.
        """
        start_time = time.time()
        output = AgentOutput(visit_id=patient.visit_id)
        history = IterationHistory()
        
        # Ensure vitals is not None for strict downstream typing
        # If None (e.g. data missing), use empty series which handles to_text_summary safely
        if vitals is None:
            raise ValueError("Vitals cannot be None")
        
        # Phase timing accumulators
        phase_times = {
            "triage": 0.0,
            "doctor": 0.0,
            "consultant": 0.0,
            "coder": 0.0,
            "synthesis": 0.0
        }
        
        # Reset agents
        self.doctor.reset()
        self.coder.reset()
        
        with self.logger.visit_context(patient.visit_id):
            try:
                # =================================================================
                # PHASE 0: TRIAGE (Context & Safety)
                # =================================================================
                if progress_callback:
                    progress_callback.set_postfix_str("Phase 0: Triage Agent", refresh=True)
                
                # Output dir for artifacts
                triage_figures_dir = self.logger.output_dir / "visits" / patient.visit_id / "figures"
                triage_figures_dir.mkdir(parents=True, exist_ok=True)
                
                # Execute Triage Agent
                t_start = time.time()
                triage_result = self.triage.run_assignment(
                    patient=patient,
                    vitals=vitals,
                    output_dir=triage_figures_dir,
                    pmh=pmh,
                    meds=meds
                )
                phase_times["triage"] = time.time() - t_start
                
                # Extract Triage Results
                triage_metrics = triage_result.metrics
                triage_context = triage_result.context
                triage_plot = triage_result.artifacts.vitals_panel
                
                # Extract Clinical Context Summary for propagation
                clinical_context_str = triage_context.clinical_context_summary if triage_context else "No context available."
                
                # Append Triage Rationale if available (explains thresholds)
                if triage_context and triage_context.rationale:
                    clinical_context_str += f"\n\n## Triage Vitals Threshold Rationale\n{triage_context.rationale}"
                
                # Log Context Summary for visibility
                self.logger.log_agent_step("orchestrator", {}, {"triage_context": clinical_context_str}, 0)
                
                # Pre-populate calculations with Triage results
                triage_calc_results = []
                for k, v in triage_metrics.items():
                    triage_calc_results.append(CalculationResult(
                        success=True,
                        metric_name=k,
                        value=v,
                        interpretation="Triage Baseline"
                    ))
                
                # Pre-populate images
                if triage_plot:
                    triage_calc_results.append(CalculationResult(
                        success=True, 
                        metric_name="triage_vital_panel", 
                        value="Attached", 
                        image_paths=[triage_plot]
                    ))
                    output.generated_images.append(triage_plot)
                
                output.calculations.extend(triage_calc_results)
                
                # =================================================================
                # CLINICAL LOOP
                # =================================================================
                
                for iteration in range(self.MAX_ITERATIONS):
                    # 1. Doctor's Analysis
                    if progress_callback:
                        progress_callback.set_postfix_str(f"Iter {iteration+1}: Doctor Analysis", refresh=True)
                        
                    t_doc = time.time()
                    doctor_analysis_text = self.doctor.analyze_situation(
                        patient=patient,
                        calculations=output.calculations,
                        vitals_summary=vitals.to_text_summary(),
                        clinical_context=clinical_context_str,
                        iteration=iteration,
                        image_reviews=output.image_reviews, # Add visual context
                        available_image_paths=output.generated_images # Pass absolute paths for lookup
                    )
                    phase_times["doctor"] += (time.time() - t_doc)
                    output.doctor_history.append(doctor_analysis_text)
                    
                    # 2. Consultant's Critique
                    if progress_callback:
                        progress_callback.set_postfix_str(f"Iter {iteration+1}: Consultant Critique", refresh=True)
                        
                    t_cons = time.time()
                    consultant_text = self.consultant.critique_analysis(
                        doctor_analysis_text=doctor_analysis_text,
                        vitals_summary=vitals.to_text_summary(),
                        clinical_context=clinical_context_str,
                        calculations=output.calculations
                    )
                    phase_times["consultant"] += (time.time() - t_cons)
                    output.consultant_history.append(consultant_text)
                    
                    history.add_feedback(consultant_text)
                    
                    # 3. Doctor Prescribes Tasks
                    if progress_callback:
                         progress_callback.set_postfix_str(f"Iter {iteration+1}: Doctor Planning", refresh=True)
                    
                    t_plan = time.time()
                    doctor_task_output = self.doctor.prescribe_tasks(
                         analysis_text=doctor_analysis_text,
                         consultant_feedback=consultant_text,
                         max_images=self.doctor.llm.config.max_images
                    )
                    phase_times["doctor"] += (time.time() - t_plan)
                    
                    tasks = doctor_task_output.tasks
                    
                    # 4. Coder Execution
                    if progress_callback:
                        progress_callback.set_postfix_str(f"Iter {iteration+1}: Coder Exec ({len(tasks)})", refresh=True)
                        
                    t_coder = time.time()
                    new_results = self._run_calculations(
                        vitals,
                        tasks=tasks,
                        patient=patient,
                        previous_results=output.calculations,
                        clinical_context=clinical_context_str
                    )
                    phase_times["coder"] += (time.time() - t_coder)
                    
                    output.calculations.extend(new_results)
                    for res in new_results:
                        if res.image_paths:
                            output.generated_images.extend(res.image_paths)
                            
                    # 5. Doctor Ranks Images (Final step of round)
                    if progress_callback:
                        progress_callback.set_postfix_str(f"Iter {iteration+1}: Doctor Ranking", refresh=True)
                    
                    t_rank = time.time()
                    
                    # Split results: New vs Old
                    # We only want to "rank" the new stuff.
                    # The old stuff is already ranked in output.image_reviews                    
                    ranking_output = self.doctor.rank_images(
                        new_results=new_results,
                        clinical_context=clinical_context_str,
                        analysis_text=doctor_analysis_text,
                        existing_reviews=output.image_reviews
                    ) 
                    phase_times["doctor"] += (time.time() - t_rank)
                    
                    # Update reviews in output
                    output.image_reviews = ranking_output.selected_images
                    
                    # Update iterations used to reflect work done
                    output.iterations_used = iteration + 1

                    # Check for sufficiency (New Structured Logic)
                    if ranking_output.is_sufficient:
                         output.verified = True
                         break

                # =================================================================
                # PHASE 3: SYNTHESIS (Discharge)
                # =================================================================
                if progress_callback:
                    progress_callback.set_postfix_str("Phase 3: Synthesis", refresh=True)
                    
                # 1. Image Selection Logic
                # Use Doctor's Top Ranked Images directly
                final_images = []
                added_filenames = set()
                
                # Always add Triage
                if triage_plot:
                    triage_review = ImageReview(
                        filename=triage_plot.split('/')[-1],
                        relevance_score=10, 
                        description="Comprehensive vital signs panel with custom thresholds based on patient history.",
                        rationale="Primary baseline for patient stability, with custom thresholds based on patient history.",
                    )
                    final_images.append(triage_review)
                    added_filenames.add(triage_review.filename)
                
                # Add Top Doctor Images
                if output.image_reviews:
                     # Sort by relevance
                     sorted_reviews = sorted(output.image_reviews, key=lambda x: x.relevance_score, reverse=True)
                     # Add up to max_images - 1
                     for rev in sorted_reviews:
                          if len(final_images) >= self.synthesizer.max_images: # Add up to max_images - 1
                               break
                          if rev.filename not in added_filenames:
                               final_images.append(rev)
                               added_filenames.add(rev.filename)
                               
                # Create a synthetic ReviewResult adapter to pass Doctor's judgments to Synthesizer
                t_synth = time.time()
                
                # Update output image reviews to match what is actually sent to the synthesizer
                # This ensures blinded outputs match the narrative
                output.image_reviews = final_images
                
                assessment = self.synthesizer.synthesize(
                    patient,
                    vitals,
                    output,
                    clinical_context=clinical_context_str,
                    iteration=output.iterations_used,
                    top_images=final_images # Pass selected images
                )
                phase_times["synthesis"] = time.time() - t_synth
                
                output.assessment = assessment
                
                output.phase_durations = phase_times

            except Exception as e:
                tb = traceback.format_exc()
                self.logger.log_error(f"Orchestrator failed processing visit {patient.visit_id}: {e}\n{tb}")
                raise e
        
        output.processing_time_ms = (time.time() - start_time) * 1000
        return output
    
    def _run_calculations(
        self, 
        vitals: VitalSignSeries, 
        tasks: list[str],
        patient: PatientVisit,
        previous_results: Optional[list[CalculationResult]] = None,
        retry_metrics: Optional[list[str]] = None,
        clinical_context: str = ""
    ) -> list[CalculationResult]:
        """Run all calculation tasks from the plan with auto-retry for failures."""
        results = previous_results or []
        retry_metrics = retry_metrics or []
        
        # Deduplicate tasks
        unique_metrics = set(tasks)

        # Execute unique tasks if not already successful
        final_results = []
        existing_metrics = {r.metric_name.lower().replace(" ", "_") for r in results if r.success}
        
        task_list = []
        
        # Helper to execute a single task with error handling
        def execute_task(metric_key, task_str):
            parameters = {}
            if metric_key in retry_metrics:
                parameters["retry"] = True
                parameters["alternative_method"] = True
            
            with self.logger.visit_context(patient.visit_id):
                return self.coder.calculate_metric(
                    task_str, 
                    vitals, 
                    parameters, 
                    demographics=patient.demographics, 
                    clinical_context=clinical_context,
                    previous_results=results,
                    visit_id=patient.visit_id
                )

        for metric in unique_metrics:
            m_key = metric.lower().replace(" ", "_").strip()
            
            if m_key in existing_metrics and m_key not in retry_metrics:
                continue
            
            # Parameters are no longer passed from the task schema
            task_list.append((m_key, metric))
        
        if task_list:
            # print(f"[Orchestrator] Executing {len(task_list)} tasks in parallel...")
            with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                future_to_metric = {
                    executor.submit(execute_task, t[0], t[1]): t[1] 
                    for t in task_list
                }
                for future in concurrent.futures.as_completed(future_to_metric):
                    try:
                        final_results.append(future.result())
                    except Exception as exc:
                        self.logger.log_error(f"Task generated exception: {exc}")
            
        return final_results
