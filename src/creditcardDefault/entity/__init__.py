from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir : Path
    source_url: str
    local_data_file: Path
    unzip_dir :Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_dir: Path
    status_file: Path
    all_schema: dict

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    
@dataclass
class ModelTrainingConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    target_name: str
    n_estimators: int
    criterion: str
    max_depth : int
    min_samples_split: int

