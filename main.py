from src.MLProject_WineQT.my_logging.loger import logger
from src.MLProject_WineQT.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = 'Data Ingestion Stage'

try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<")
        
except Exception as e:
        logger.exception(e)
        raise e


