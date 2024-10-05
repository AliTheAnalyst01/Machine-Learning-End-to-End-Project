from src.MLProject_WineQT.my_logging.loger import logger
from src.MLProject_WineQT.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.MLProject_WineQT.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from src.MLProject_WineQT.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline


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

    
    



