from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True)
class DataingestionConfig:
    root_dir: Path
    Source_URL: str
    local_data_files: Path
    unzip_dir: Path