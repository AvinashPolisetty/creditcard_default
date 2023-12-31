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
    