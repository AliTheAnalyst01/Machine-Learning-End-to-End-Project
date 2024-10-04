from src.MLProject_WineQT.constants.const import *
from src.MLProject_WineQT.utils.common import read_yaml, create_directories
from src.MLProject_WineQT.entity.config_entity import DataingestionConfig
from src.MLProject_WineQT.my_logging.loger import logger
import zipfile
import os

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

