"""
Configuration management for XAI-Agent-Pulse research project.
"""

import os
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, field
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


@dataclass
class DatasetConfig:
    """Configuration for MC-MED dataset paths."""
    
    base_path: Path = field(default_factory=lambda: Path(__file__).parent.parent / "dataset")
    
    @property
    def visits_path(self) -> Path:
        return self.base_path / "visits.csv"
    
    @property
    def numerics_path(self) -> Path:
        return self.base_path / "numerics.csv"
    
    @property
    def pmh_path(self) -> Path:
        return self.base_path / "pmh.csv"
    
    @property
    def meds_path(self) -> Path:
        return self.base_path / "meds.csv"
    


@dataclass
class ModelConfig:
    """Configuration for LLM models.
    
    Note: Model registry and adapters are in src/models/adapters.py
    This just holds default settings and API keys from environment.
    """
    
    # Default model (key from SUPPORTED_MODELS)
    default_model: str = field(
        default_factory=lambda: os.getenv("DEFAULT_MODEL", "gpt-5.2")
    )
    
    # API Keys (loaded from environment)
    openai_api_key: Optional[str] = field(
        default_factory=lambda: os.getenv("OPENAI_API_KEY")
    )
    google_project_id: Optional[str] = field(
        default_factory=lambda: os.getenv("GOOGLE_CLOUD_PROJECT")
    )
    google_location: Optional[str] = field(
        default_factory=lambda: os.getenv("GOOGLE_CLOUD_LOCATION")
    )
    medgemma_endpoint_id: Optional[str] = field(
        default_factory=lambda: os.getenv("MEDGEMMA_ENDPOINT_ID")
    )
    
    # Ollama settings
    ollama_base_url: str = field(
        default_factory=lambda: os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    )


@dataclass
class ExperimentConfig:
    """Configuration for experiment parameters."""
    
    # Sample sizes
    sample_size: int = 1000  # Number of visits to process per experiment
    test_split: float = 0.2  # Hold-out test set ratio
    
    # Random seed for reproducibility
    random_seed: int = 444
    
    # Demographic groups for fairness analysis (from MC-MED)
    demographic_groups: tuple = (
        "White",
        "Other / Unknown",
        "Asian",
        "Black or African American",
        "Native Hawaiian or Other Pacific Islander",
        "American Indian or Alaska Native",
    )
    
    # ESI levels
    esi_levels: tuple = (1, 2, 3, 4, 5)
    
    # Output directory
    output_dir: Path = field(
        default_factory=lambda: Path(__file__).parent.parent / "results"
    )


@dataclass
class ContinuationConfig:
    """Configuration for LLM continuation and loop detection."""
    
    # Max continuations before giving up
    max_continuations: int = 1
    
    # Loop Detection Thresholds
    # Type-Token Ratio: If TTR < this value, the model is likely stuck repeating
    ttr_threshold: float = 0.3
    
    # N-gram duplication: If more than this fraction of n-grams are duplicates, it's looping
    ngram_duplication_threshold: float = 0.5
    
    # N-gram size for repetition detection
    ngram_size: int = 4
    
    # Number of characters to analyze from the tail of the response
    tail_chars: int = 500


@dataclass
class Config:
    """Main configuration container."""
    
    dataset: DatasetConfig = field(default_factory=DatasetConfig)
    model: ModelConfig = field(default_factory=ModelConfig)
    experiment: ExperimentConfig = field(default_factory=ExperimentConfig)
    continuation: ContinuationConfig = field(default_factory=ContinuationConfig)
    


# Global configuration instance
config = Config()
