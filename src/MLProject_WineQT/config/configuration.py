# configuration Manager
from src.MLProject_WineQT.constants.const import *
from src.MLProject_WineQT.utils.common import read_yaml, create_directories
from src.MLProject_WineQT.entity.config_entity import (DataingestionConfig,
                                                       DataValidationConfig)


class ConfigurationManager:
     def __init__(
         self,
         config_filepath = CONFIG_FILE_PATH,
         params_filepath = PARAMS_FILE_PATH,
         schema_filepath = SCHEMA_FILE_PATH):
         
         self.config = read_yaml(config_filepath)
         self.params = read_yaml(params_filepath)
         self.schema = read_yaml(schema_filepath)
         
         create_directories([self.config.artifacts_root])
         
     def get_data_ingestion_config(self) -> DataingestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        get_data_ingestion_config=DataingestionConfig(root_dir=config.root_dir,
                                                      Source_URL=config.source_URL,
                                                      local_data_files=config.local_data_file,
                                                      unzip_dir=config.unzip_dir)
        return get_data_ingestion_config
    
    
     def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation  # Access 'data_validation' config block
        
        # Fetch the schema (columns) from the schema file
        schema = self.schema.COLUMNS
        create_directories([config.root_dir]) # Debug print to ensure schema is loaded
        
        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=schema
        )
        return data_validation_config
           
             