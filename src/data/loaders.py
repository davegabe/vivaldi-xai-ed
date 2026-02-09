"""
Data loaders for MC-MED dataset files.
Provides efficient loading and parsing of clinical data.
"""

import pandas as pd
from pathlib import Path
from typing import Iterator, Optional
from datetime import datetime
from tqdm import tqdm

from .schema import (
    PatientVisit,
    Demographics,
    ESILevel,
    Disposition,
    VitalSignSeries,
    VitalSign,
    MedicalHistory,
    Medication,
)


class VisitsLoader:
    """
    Loader for visits.csv containing demographics, triage, and outcomes.
    Primary data source for ESI prediction and LOS prediction.
    """
    
    def __init__(self, filepath: Path):
        self.filepath = filepath
        self._df: Optional[pd.DataFrame] = None
    
    def load(self, sample_size: Optional[int] = None) -> pd.DataFrame:
        """Load visits data, optionally sampling for faster iteration."""
        self._df = pd.read_csv(self.filepath)
        
        if sample_size and sample_size < len(self._df):
            self._df = self._df.sample(n=sample_size, random_state=42)
        
        return self._df
    
    def get_demographic_breakdown(self) -> dict[str, int]:
        """Get count of visits by ethnicity group (Table 1 validation)."""
        if self._df is None:
            self.load()
        
        # Try Race column first, then Ethnicity
        for col in ["Race", "Ethnicity", "race", "ethnicity"]:
            if col in self._df.columns:
                return self._df[col].value_counts().to_dict()
        return {}
    
    def iter_visits(self, quiet: bool = False) -> Iterator[PatientVisit]:
        """Iterate over visits as typed objects."""
        if self._df is None:
            self.load()
        
        iterator = self._df.iterrows()
        if not quiet:
            iterator = tqdm(iterator, total=len(self._df), desc="Loading visits")
            
        for _, row in iterator:
            yield self._row_to_visit(row)
    
    def _row_to_visit(self, row: pd.Series) -> PatientVisit:
        """Convert DataFrame row to PatientVisit object."""
        # Combine Race and Ethnicity into single field
        race_val = str(row.get("Race", "")).strip()
        eth_val = str(row.get("Ethnicity", "")).strip()
        
        # Combine: prioritize ethnicity if different from race
        if eth_val and eth_val.lower() not in ["nan", "unknown", "", race_val.lower()]:
            ethnicity = f"{race_val} ({eth_val})" if race_val else eth_val
        else:
            ethnicity = race_val if race_val and race_val.lower() != "nan" else "Unknown"
        
        demographics = Demographics(
            age=int(row.get("Age", 0)),
            gender=row.get("Gender", "Other"),
            ethnicity=ethnicity,
            insurance_class=str(row.get("Payor_class", "Unknown")),
        )
        
        # Parse ESI level from values like "3-Urgent", "2-Emergent"
        triage_acuity = None
        esi_val = row.get("Triage_acuity")
        if pd.notna(esi_val):
            try:
                esi_str = str(esi_val).strip()
                esi_num = int(esi_str[0])
                triage_acuity = ESILevel(esi_num)
            except (ValueError, TypeError, IndexError):
                pass
        
        # Parse disposition
        disposition = None
        dispo_val = row.get("ED_dispo")
        if pd.notna(dispo_val):
            disposition = Disposition.ADMIT if "admit" in str(dispo_val).lower() else Disposition.DISCHARGE
        
        # Parse LOS
        los_hours = None
        los_val = row.get("ED_LOS")
        if pd.notna(los_val):
            los_hours = float(los_val)
        
        return PatientVisit(
            visit_id=str(row.get("CSN", row.name)),
            patient_id=str(row.get("MRN", "")),
            demographics=demographics,
            chief_complaint=row.get("CC"),
            triage_acuity=triage_acuity,
            ed_disposition=disposition,
            ed_los_hours=los_hours,
            arrival_mode=str(row.get("Means_of_arrival", "Unknown")),
        )


class NumericsLoader:
    """
    Loader for numerics.csv containing time-series vital signs.
    """
    
    # Mapping of possible column names to standardized names
    VITAL_MAPPING = {
        "heart_rate": ["HR", "heart_rate", "HeartRate", "pulse"],
        "systolic_bp": ["SBP", "systolic_bp", "SystolicBP", "sbp"],
        "diastolic_bp": ["DBP", "diastolic_bp", "DiastolicBP", "dbp"],
        "spo2": ["SpO2", "spo2", "O2Sat", "oxygen_saturation"],
        "respiratory_rate": ["RR", "respiratory_rate", "RespRate", "resp_rate"],
        "temperature": ["Temp", "temperature", "Temperature", "temp"],
    }
    
    def __init__(self, filepath: Path, window_index: pd.DataFrame):
        self.filepath = filepath
        self._df: Optional[pd.DataFrame] = None
        self.window_index = window_index  # DataFrame with CSN, window_start, window_end (required)
    
    def load(self) -> pd.DataFrame:
        """Load numerics data."""
        self._df = pd.read_csv(self.filepath)
        return self._df
    
    def get_vitals_for_visit(self, visit_id: str) -> VitalSignSeries:
        """Get all vital signs for a specific visit."""
        if self._df is None:
            self.load()
        
        # Ensure ID match (handle int/str diffs)
        try:
            visit_id_int = int(visit_id)
            visit_data = self._df[self._df["CSN"] == visit_id_int].copy()
        except ValueError:
            # Handle non-integer IDs if any
            visit_data = self._df[self._df["CSN"].astype(str) == str(visit_id)].copy()
        
        # Apply 24h window filter
        if not visit_data.empty:
            window_row = self.window_index[self.window_index['CSN'].astype(str) == str(visit_id)]
            if not window_row.empty:
                start_time = pd.to_datetime(window_row.iloc[0]['window_start']).replace(tzinfo=None)
                end_time = pd.to_datetime(window_row.iloc[0]['window_end']).replace(tzinfo=None)
                
                # Convert Time column to datetime if not already
                if 'Time' in visit_data.columns:
                    visit_data['Time'] = pd.to_datetime(visit_data['Time'], errors='coerce').dt.tz_localize(None)
                    # Filter to the 24h window, but KEEP ground truth measures regardless of time
                    # This ensures we don't drop Pain scores recorded at T-2h (Triage) just because
                    # the high-density vital window starts at T=0
                    time_mask = (visit_data['Time'] >= start_time) & (visit_data['Time'] <= end_time)
                    
                    # We ensure that the ground truth measures are consistent across age, gender, and ethnicity
                    gt_measures = ["pain"]
                    measure_mask = visit_data["Measure"].astype(str).str.lower().isin(gt_measures)
                    
                    # Keep row if it's within window OR it's a ground truth measure
                    visit_data = visit_data[time_mask | measure_mask]

        
        series = VitalSignSeries(visit_id=visit_id)
        
        # === LONG FORMAT PARSING ===
        for standard_name, possible_names in self.VITAL_MAPPING.items():
            # Filter rows where Measure matches any alias
            # Case-insensitive matching
            mask = visit_data["Measure"].astype(str).str.lower().isin([n.lower() for n in possible_names])
            vital_rows = visit_data[mask]
            
            if not vital_rows.empty:
                vitals = self._parse_vital_rows(vital_rows)
                
                # Convert temperature from Fahrenheit to Celsius
                if standard_name == "temperature":
                    for v in vitals:
                        if v.value > 50:  # Fahrenheit (no human has 50°C body temp)
                            v.value = (v.value - 32) * 5 / 9
                
                setattr(series, standard_name, vitals)
        
        # Pain (Long format)
        pain_mask = visit_data["Measure"].astype(str).str.lower().isin(["pain", "pain_score", "pain score"])
        pain_rows = visit_data[pain_mask]
        if not pain_rows.empty:
             # Take last value
             try:
                 vals = pd.to_numeric(pain_rows["Value"], errors="coerce").dropna()
                 if not vals.empty:
                     series.pain_score = int(vals.iloc[-1])
             except:
                 pass
        
        # Apply outlier filtering
        series.filter_outliers()
        
        return series

    def _parse_vital_rows(self, rows: pd.DataFrame) -> list[VitalSign]:
        """Parse rows from long-format dataframe into VitalSigns."""
        if rows.empty:
            return []
            
        # Vectorized datetime conversion
        time_col = "Time" if "Time" in rows.columns else None
        timestamps = []
        
        if time_col:
            # Native parsing for safety
            for ts_str in rows[time_col]:
                try:
                    # Clean simple ISO format
                    clean_str = str(ts_str).replace("Z", "+00:00")
                    timestamps.append(datetime.fromisoformat(clean_str))
                except (ValueError, TypeError):
                    timestamps.append(None)
        else:
            now = datetime.now()
            timestamps = [now] * len(rows)
            
        values = pd.to_numeric(rows["Value"], errors='coerce')
        
        vitals = []
        for val, ts in zip(values, timestamps):
            # Check for valid float and valid datetime
            if pd.notna(val) and ts is not None:
                vitals.append(VitalSign(
                    timestamp=ts,
                    value=float(val),
                    unit="",
                ))
                
        # Sort by time
        vitals.sort(key=lambda x: x.timestamp)
        return vitals


class PMHLoader:
    """Loader for past medical history from pmh.csv."""
    
    def __init__(self, filepath: Path):
        self.filepath = filepath
        self._df: Optional[pd.DataFrame] = None
    
    def load(self) -> pd.DataFrame:
        """Load PMH data."""
        self._df = pd.read_csv(self.filepath)
        return self._df
    
    def get_history(self, patient_id: str) -> MedicalHistory:
        """
        Get medical history for a patient by MRN.
        
        CSV Columns: MRN, Noted_date, CodeType, Code, Desc10, CCS, DescCCS
        """
        if self._df is None:
            self.load()
        
        # Filter by MRN (ensure string matching)
        try:
            mrn_int = int(patient_id)
            patient_data = self._df[self._df["MRN"] == mrn_int]
        except ValueError:
            patient_data = self._df[self._df["MRN"].astype(str) == str(patient_id)]
        
        conditions = []
        # Use Desc10 (ICD description) or DescCCS (category)
        if "Desc10" in self._df.columns:
            conditions = patient_data["Desc10"].dropna().unique().tolist()
        elif "DescCCS" in self._df.columns:
            conditions = patient_data["DescCCS"].dropna().unique().tolist()
        
        return MedicalHistory(patient_id=patient_id, conditions=conditions)


class MedsLoader:
    """Loader for medications from meds.csv."""
    
    def __init__(self, filepath: Path):
        self.filepath = filepath
        self._df: Optional[pd.DataFrame] = None
    
    def load(self) -> pd.DataFrame:
        """Load medications data."""
        self._df = pd.read_csv(self.filepath)
        return self._df
    
    def get_medications(self, patient_id: str) -> list[Medication]:
        """
        Get all medications for a patient by MRN.
        
        CSV Columns: MRN, Med_ID, NDC, Name, Generic_name, Med_class, ...
        """
        if self._df is None:
            self.load()
        
        try:
            mrn_int = int(patient_id)
            patient_data = self._df[self._df["MRN"] == mrn_int]
        except ValueError:
            patient_data = self._df[self._df["MRN"].astype(str) == str(patient_id)]
        
        meds = []
        for _, row in patient_data.iterrows():
            # Prefer Generic_name, fallback to Name
            name = row.get("Generic_name")
            if pd.isna(name):
                name = row.get("Name", "Unknown Med")
            
            meds.append(Medication(
                patient_id=patient_id,
                name=str(name),
                med_class=row.get("Med_class"),
            ))
        
        return meds
