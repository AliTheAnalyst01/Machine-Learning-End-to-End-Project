# update the component
import os
from pathlib import Path
import urllib.request as request
import zipfile
from src.MLProject_WineQT.my_logging.loger import logger
from src.MLProject_WineQT.utils.common import get_size
from src.MLProject_WineQT.entity.config_entity import DataingestionConfig


class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH):
        self.config = read_yaml(config_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataingestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        return DataingestionConfig(
            root_dir=config.root_dir,
            Source_URL=config.source_URL,
            local_data_files=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

class DataIngestion:
    def __init__(self, config: DataingestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_files):
            try:
                filename, header = request.urlretrieve(
                    url=self.config.Source_URL,
                    filename=self.config.local_data_files
            )
                logger.info(f"{filename} downloaded with the following info: \n{header}")

            # After downloading, validate if it's a valid zip file
                if not zipfile.is_zipfile(self.config.local_data_files):
                    raise zipfile.BadZipFile(f"{self.config.local_data_files} is not a valid zip file")
            except Exception as e:
                logger.error(f"Error downloading file: {e}")
                raise 
            else:
                logger.info(f"File already exists with size: {get_size(Path(self.config.local_data_files))}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        if zipfile.is_zipfile(self.config.local_data_files):
            with zipfile.ZipFile(self.config.local_data_files, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"Extracted {self.config.local_data_files} to {unzip_path}")
        else:
            raise zipfile.BadZipFile(f"{self.config.local_data_files} is not a valid zip file")
