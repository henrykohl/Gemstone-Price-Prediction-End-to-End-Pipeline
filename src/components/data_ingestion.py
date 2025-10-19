import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import customexception


import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    raw_data_path:str=os.path.join("artifacts","raw.csv")
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        

    def initiate_data_ingestion(self):
        logging.info("data ingestion started")
        try:
            data=pd.read_csv("https://raw.githubusercontent.com/henrykohl/Gemstone-Price-Prediction-End-to-End-Pipeline/refs/heads/main/notebooks/data/raw.csv") # 修改過
            logging.info(" reading a df") ## data 是 pandas.core.frame.DataFrame 類型物件

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False) 
            logging.info(" i have saved the raw dataset in artifact folder") ## 將 data 存成 csv 檔
            
            logging.info("here i have performed train test split")
            
            train_data,test_data=train_test_split(data,test_size=0.25)
            logging.info("train test split completed") ## 把 data 分成 train_data 與 test_data
            
            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)
            
            logging.info("data ingestion part completed") ## train_data 與 test_data 分別存成不同 csv 黨
            
            return (
                 
                
                self.ingestion_config.train_data_path, # train.csv 路徑
                self.ingestion_config.test_data_path  # test.csv 路徑
            )



        except Exception as e:
            logging.info()
            raise customexception(e,sys)


if __name__=="__main__":
    obj=DataIngestion()

    obj.initiate_data_ingestion()