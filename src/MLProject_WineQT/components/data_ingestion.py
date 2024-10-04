# update the component
import os
import urllib.request as request
import zipfile
from src.MLProject_WineQT.my_logging.loger import logger
from src.MLProject_WineQT.utils.common import get_size
from pathlib import Path
from src.MLProject_WineQT.entity.config_entity import DataingestionConfig

# updata the component 
class DataIngestion:
    def __init__(self,config: DataingestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_files):
            filename,header = request.urlretrieve(
                url=self.config.Source_URL,
                filename=self.config.local_data_files
            ) 
            logger.info(f"{filename} download with following info: /n {header}")
        else:
            logger.info(f"file already exist fo size: {get_size(Path(self.config.local_data_files))}")
            
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        if zipfile.is_zipfile(self.config.local_data_files):
            with zipfile.ZipFile(self.config.local_data_files, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
        else:
            raise zipfile.BadZipFile(f"{self.config.local_data_files} is not a valid zip file")