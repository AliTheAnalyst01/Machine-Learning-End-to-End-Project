from MLProject_WineQT.my_logging.loger import logger
from MLProject_WineQT.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from MLProject_WineQT.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from MLProject_WineQT.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from MLProject_WineQT.pipeline.stage04_model_trainer import ModelTrainerTrainingPipeline

STAGE_NAME = 'Data Ingestion Stage'

try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<")
        
except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = 'Data Validation Stage'
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<")
            
except Exception as e:
        logger.exception(e)
        raise e
    
    
STAGE_NAME = 'Data Transforming Stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataTransformationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} <<<<<  Completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Trainer Stage'

try:
        logger.info(">>>>> stage {STAGE_NAME} Started <<<<<<<")
        data_ingestion = ModelTrainerTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
        logger.exception(e)
        raise e
    
    



