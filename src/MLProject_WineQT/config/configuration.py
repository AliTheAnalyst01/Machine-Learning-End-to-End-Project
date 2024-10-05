# configuration Manager
from src.MLProject_WineQT.constants.const import *
from src.MLProject_WineQT.utils.common import read_yaml, create_directories
from src.MLProject_WineQT.entity.config_entity import (DataingestionConfig,
                                                       DataValidationConfig,
                                                       DataTransformationConfig,
                                                       ModelTrainerConfig)


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
    
    
     def get_data_transformation_config(self) -> DataTransformationConfig:
            config = self.config.data_transformation
            create_directories([config.root_dir])
            
            data_transformation_config=DataTransformationConfig(
                root_dir=config.root_dir,
                data_path=config.data_path
            )
            return data_transformation_config
        
        
     def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN
        create_directories([config.root_dir]) 
        
        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column= schema.name,
)

        return model_trainer_config
           
             