import os
from box.exceptions import BoxValueError
import yaml
from src.MLProject_WineQT.my_logging.loger import logger
import json
from ensure import ensure_annotations
from box import config_box
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml:Path) -> config_box:
    """
    reads your file returns
    
    Args:
        path_to_yaml(str): path like input
    
    Raise:
        ValueError: if yaml file is empty 
        e : empty file 
        
    Return Config Box : ConfigBox_type
    
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_yaml} load successfuly")
            return config_box(content)
    except BoxValueError:
        raise ValueError('your file is empty')
    
    except Exception as e:
        raise e
    
    
    
@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """create a list of directories
    Args:
    path_to_directories(list): list of path of directories
    ignore_log(bool,optional): ignore
    multiple dirs is to be created Defualt
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directories at: {path}") 
            

