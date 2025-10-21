import os
import sys
from src.logger.logging import logging
from src.exception.exception import customexception
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation


obj=DataIngestion()
## 獲得 train.csv 路徑, test.csv 路徑
train_data_path,test_data_path=obj.initiate_data_ingestion() 

data_transformation=DataTransformation()
## 獲得 numpy.ndarray (2D), numpy.ndarray (2D)
train_arr,test_arr=data_transformation.initialize_data_transformation(train_data_path,test_data_path)

## 儲存 best 模型物件
model_trainer_obj=ModelTrainer()
model_trainer_obj.initate_model_training(train_arr,test_arr)

# model_eval_obj = ModelEvaluation()
# model_eval_obj.initiate_model_evaluation(train_arr,test_arr)