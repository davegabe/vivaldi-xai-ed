"""
Vitals Plotting Utility - Generates professional clinical visualizations.
Creates comprehensive vitals panels for Zero-Shot and utility plots for Agentic.
"""

import base64
import io
from pathlib import Path
from typing import Optional, Tuple
from datetime import datetime

# CRITICAL: Import threading_utils BEFORE matplotlib to set Agg backend
try:
    from ..data.schema import VitalSignSeries, PLAUSIBILITY_LIMITS
    from ..utils.threading_utils import matplotlib_lock
except ImportError:
    from src.data.schema import VitalSignSeries, PLAUSIBILITY_LIMITS
    from src.utils.threading_utils import matplotlib_lock

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


# Clinical color scheme (light/professional theme)
COLORS = {
    "hr": "#E53935",        # Red for heart rate
    "sbp": "#1E88E5",       # Blue for systolic BP
    "dbp": "#64B5F6",       # Light blue for diastolic BP
    "spo2": "#43A047",      # Green for SpO2
    "rr": "#FB8C00",        # Orange for respiratory rate
    "temp": "#8E24AA",      # Purple for temperature
    "normal_range": "#C8E6C9",  # Darker light green for better visibility
    "warning_range": "#FFE0B2",  # Darker light orange for better visibility
    "critical_range": "#FFCDD2",  # Darker light red for better visibility
}

# Official adult clinical baselines (visual context only)
# Sources: NEWS2, AHA, WHO (non-diagnostic)
OFFICIAL_CLINICAL_THRESHOLDS = {
    "hr": {
        "normal": (60, 100),
        "warning": (40, 120),
    },
    "rr": {
        "normal": (12, 20),
        "warning": (8, 25),
    },
    "spo2": {
        "normal": (95, 100),
        "warning": (90, 94),
    },
    "sbp": {
        "normal": (100, 140),
        "warning": (90, 180),
    },
    "dbp": {
        "normal": (60, 90),
        "warning": (50, 110),
    },
    "temp": {
        "normal": (36.1, 37.9),
        "warning": (35.0, 38.9),
    },
}

LOCALIZATION = {
    "en": {
        "hr_label": "Heart Rate",
        "rr_label": "Respiratory Rate",
        "rr_unit": "breaths/min",
        "sbp_label": "Systolic BP",
        "spo2_label": "SpO2",
        "dbp_label": "Diastolic BP",
        "temp_label": "Temperature",
        "outside_normal": "Outside normal",
        "median": "Median",
    },
    "it": {
        "hr_label": "Frequenza Cardiaca",
        "rr_label": "Frequenza Respiratoria",
        "rr_unit": "atti/min",
        "sbp_label": "Pressione Sistolica",
        "spo2_label": "SpO2",
        "dbp_label": "Pressione Diastolica",
        "temp_label": "Temperatura",
        "outside_normal": "Fuori range",
        "median": "Mediana",
    },
    "sq": {
        "hr_label": "Rrahjet e Zemrës",
        "rr_label": "Frekuenca e Frymëmarrjes",
        "rr_unit": "frymë/min",
        "sbp_label": "Presioni Sistolik",
        "spo2_label": "SpO2",
        "dbp_label": "Presioni Diastolik",
        "temp_label": "Temperatura",
        "outside_normal": "Jashtë normës",
        "median": "Mesatarja",
    }
}


def generate_vitals_panel(
    vitals: VitalSignSeries,
    output_dir: Path,
    visit_id: str,
    dpi: int = 100,
    thresholds: Optional[dict[str, Tuple[float, float]]] = None,
    warning_thresholds: Optional[dict[str, Tuple[float, float]]] = None,
    language: str = "en"
) -> Tuple[Optional[Path], Optional[str]]:
    """
    Generate a comprehensive vitals panel with all available signals.
    
    Args:
        vitals: VitalSignSeries object with patient vital signs
        output_dir: Directory to save the plot
        visit_id: Patient visit ID for filename
        dpi: Resolution for saved image
        thresholds: Optional dict mapping signal keys to (low, high) threshold tuples
        
    Returns:
        Tuple of (file_path, base64_encoded_string), or (None, None) if no data
    """
    if not vitals or not vitals.has_data():
        return None, None
    
    # Base defaults from official clinical references
    active_thresholds = {
        k: v["normal"] for k, v in OFFICIAL_CLINICAL_THRESHOLDS.items()
    }
    
    # Apply personalized thresholds if provided (overrides defaults)
    if thresholds:
        active_thresholds.update(thresholds)
    
    # Select localization
    loc = LOCALIZATION.get(language, LOCALIZATION["en"])

    # Use lock to prevent concurrent matplotlib access
    with matplotlib_lock:
        available_signals = []
        if vitals.heart_rate:
            available_signals.append(("hr", vitals.heart_rate, loc["hr_label"], "bpm", COLORS["hr"]))
        if vitals.respiratory_rate:
            available_signals.append(("rr", vitals.respiratory_rate, loc["rr_label"], loc["rr_unit"], COLORS["rr"]))
        if vitals.systolic_bp:
            available_signals.append(("sbp", vitals.systolic_bp, loc["sbp_label"], "mmHg", COLORS["sbp"]))
        if vitals.spo2:
            available_signals.append(("spo2", vitals.spo2, loc["spo2_label"], "%", COLORS["spo2"]))
        if vitals.diastolic_bp:
            available_signals.append(("dbp", vitals.diastolic_bp, loc["dbp_label"], "mmHg", COLORS["dbp"]))
        if vitals.temperature:
            available_signals.append(("temp", vitals.temperature, loc["temp_label"], "°C", COLORS["temp"]))
        
        if not available_signals:
            return None, None
        
        # Create figure with 2 columns
        n_plots = len(available_signals)
        ncols = 2
        nrows = (n_plots + ncols - 1) // ncols
        
        fig, axes = plt.subplots(nrows, ncols, figsize=(16, 4 * nrows), constrained_layout=True)
        axes_flat = axes.flatten()
        
        for idx, (signal_key, data, label, unit, color) in enumerate(available_signals):
            ax = axes_flat[idx]
            
            # Standard single-line plot
            times = [v.timestamp for v in data]
            values = [v.value for v in data]
            ax.plot(times, values, color=color, linewidth=2, marker=".", markersize=6)
            
            # Add normal/warning/critical range shading
            if signal_key in active_thresholds:
                baseline = OFFICIAL_CLINICAL_THRESHOLDS.get(signal_key, {})
                
                # Determine effective boundaries for view scaling
                n_low, n_high = active_thresholds[signal_key]
                w_range = (
                    warning_thresholds.get(signal_key)
                    if warning_thresholds and signal_key in warning_thresholds
                    else baseline.get("warning")
                )
                
                # Calculate margin for visual breathing room if plausibility limits exist
                p_limits = PLAUSIBILITY_LIMITS.get(signal_key)
                margin = (p_limits[1] - p_limits[0]) * 0.01 if p_limits else 0

                _add_risk_zones(
                    ax, 
                    times, 
                    normal_range=active_thresholds[signal_key],
                    warning_range=w_range
                )
                
                # Dynamic Y-Axis Scaling
                # We want to show the data, the normal range, and the start of the danger zone
                # Calculate relevant points of interest
                points_of_interest = list(values) if values else []
                points_of_interest.extend([n_low, n_high])
                if w_range:
                    points_of_interest.extend(w_range)
                
                if points_of_interest:
                    view_min = min(points_of_interest)
                    view_max = max(points_of_interest)
                    span = view_max - view_min
                    padding = span * 0.15 if span > 0 else 1.0
                    
                    
                    # Clamp limits to physical plausibility if defined
                    if signal_key in PLAUSIBILITY_LIMITS:
                        p_min, p_max = PLAUSIBILITY_LIMITS[signal_key]
                        final_min = max(view_min - padding, p_min - margin)
                        final_max = min(view_max + padding, p_max + margin)
                        ax.set_ylim(final_min, final_max)
                    else:
                        ax.set_ylim(view_min - padding, view_max + padding)
            
            # Calculate clinically meaningful statistics
            if values:
                min_val = min(values)
                max_val = max(values)
                median_val = np.median(values)
                
                # Calculate % time outside normal range
                normal_low, normal_high = active_thresholds[signal_key]
                pct_abnormal = 100 * sum(
                    v < normal_low or v > normal_high for v in values
                ) / len(values)
                
                # Primary title: signal name and min-max range
                ax.set_title(
                    f"{label} [{unit}]  (Min-Max: {min_val:.1f}-{max_val:.1f})",
                    fontsize=12,
                    fontweight="semibold"
                )
                
                # Bottom-left: burden of abnormality
                ax.text(
                    0.01,
                    0.02,
                    f"{loc['outside_normal']}: {pct_abnormal:.0f}%",
                    transform=ax.transAxes,
                    fontsize=9,
                    ha="left",
                    va="bottom",
                    alpha=0.85,
                )
                
                # Bottom-right: typical value
                ax.text(
                    0.99,
                    0.02,
                    f"{loc['median']}: {median_val:.1f}",
                    transform=ax.transAxes,
                    fontsize=9,
                    ha="right",
                    va="bottom",
                    alpha=0.85,
                )
            else:
                ax.set_title(f"{label} [{unit}]", fontsize=12, fontweight="semibold")
            
            # Styling
            ax.grid(True, alpha=0.3, linestyle="--")
            ax.tick_params(axis="both", labelsize=10)
            
            # Format time labels
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
            plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
        
        # Hide unused subplots
        for i in range(idx + 1, len(axes_flat)):
            fig.delaxes(axes_flat[i])
        
        # # Add clinician-facing transparency disclaimer
        # fig.suptitle(
        #     "Vital sign ranges shown are reference thresholds (NEWS2/WHO). ",
        #     fontsize=10,
        #     y=0.995,
        #     alpha=0.8,
        # )
            
        # Save to file
        output_dir.mkdir(parents=True, exist_ok=True)
        filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_vitals_panel_{visit_id}.png"
        file_path = output_dir / filename
        plt.savefig(file_path, dpi=dpi, bbox_inches="tight", facecolor="white")
        
        # Generate base64
        buf = io.BytesIO()
        plt.savefig(buf, format="png", dpi=dpi, bbox_inches="tight", facecolor="white")
        buf.seek(0)
        b64_string = base64.b64encode(buf.read()).decode("utf-8")
        buf.close()
        
        plt.close(fig)
        
        return file_path, b64_string


def _add_risk_zones(
    ax, 
    times, 
    normal_range: Tuple[float, float],
    warning_range: Optional[Tuple[float, float]] = None
):
    """Add shaded normal, warning, and danger (critical) ranges to a subplot."""
    if not times:
        return
    
    # 1. Normal Zone (Green)
    n_low, n_high = normal_range
    ax.axhspan(n_low, n_high, alpha=0.35, color=COLORS["normal_range"], zorder=0, label="_nolegend_")
    
    # Define boundaries where Danger starts (default to Normal boundaries if no Warning)
    danger_upper_start = n_high
    danger_lower_start = n_low
    
    # 2. Warning Zones (Orange)
    if warning_range:
        w_low, w_high = warning_range
        danger_upper_start = max(n_high, w_high)
        danger_lower_start = min(n_low, w_low)
        
        # Upper Warning
        if w_high > n_high:
            ax.axhspan(n_high, w_high, alpha=0.3, color=COLORS["warning_range"], zorder=0, label="_nolegend_")
        # Lower Warning
        if w_low < n_low:
            ax.axhspan(w_low, n_low, alpha=0.3, color=COLORS["warning_range"], zorder=0, label="_nolegend_")
            
    # 3. Danger Zones (Red) - Extend to infinity
    # Use a sufficiently large number to represent infinity for visual plotting purposes
    # The plot limits (ylim) should be set by the caller to constrain the view
    INF = 10000 
    
    # Upper Danger
    ax.axhspan(danger_upper_start, INF, alpha=0.25, color=COLORS["critical_range"], zorder=0, label="_nolegend_")
    
    # Lower Danger
    ax.axhspan(-INF, danger_lower_start, alpha=0.25, color=COLORS["critical_range"], zorder=0, label="_nolegend_")
    
    # Add boundary lines for Normal
    ax.axhline(n_low, color="#66BB6A", linestyle="--", linewidth=1.0, alpha=0.9)
    ax.axhline(n_high, color="#66BB6A", linestyle="--", linewidth=1.0, alpha=0.9)


def encode_image_to_base64(image_path: Path) -> Optional[str]:
    """Read an image file and return its base64 encoding."""
    if not image_path.exists():
        return None
    
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
