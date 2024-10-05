from MLProject_WineQT.config.configuration import ConfigurationManager
from MLProject_WineQT.components.model_evalution import ModelEvalution
from MLProject_WineQT.my_logging.loger import logger

STAGE_NAME = "Model Evalution Stage"



class ModelEvalutionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
            config = ConfigurationManager()
            model_evalution_config = config.get_model_evalution_config()
            model_evalution_config = ModelEvalution(config=model_evalution_config)
            model_evalution_config.save_result()
            
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} <<<<<<< Started")
        obj = ModelEvalutionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} <<<<<<<<<< Completed \n\nx=================")
    except Exception as e:
        logger.exception(e)
        raise e