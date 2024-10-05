import os
from src.MLProject_WineQT.my_logging.loger import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.MLProject_WineQT.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config
    # Note you can add different data transformation technique such as scaler,PCA, and all  
    # you can perform all kind of the EDA in ML cycle here before passing this data to the model
    
    # i am only add the train_test_split becuse this data is already cleaned
    
    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)
        train,test = train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir,'train.csv'),index=False)
        test.to_csv(os.path.join(self.config.root_dir,'test.csv'),index=False)
        
        logger.info('spliting the data in the train and test sets')
        logger.info(train.shape)
        logger.info(test.shape)
        
        
        print(train.shape)
        print(test.shape)
          