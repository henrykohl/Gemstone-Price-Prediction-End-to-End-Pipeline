# firstproject

* Github Resource：[Gemstone-Price-Prediction-End-to-End-Pipeline](https://github.com/sunnysavita10/Gemstone-Price-Prediction-End-to-End-Pipelin)

* [My Gemstone Github](https://github.com/henrykohl/Gemstone-Price-Prediction-End-to-End-Pipeline)

# Lecture 9 Note -- [MLOps End to End Project](https://www.youtube.com/watch?v=G6frVmkVMr4)

* Flow
  <pre>
    Machine Learning       
           |
           v
         build  / ___________
           |    \           |            ________________
           |                |           |                |
           v                |           |                v
        testing             |           |             debuging
        |     |         retraining      |                |
        v     v             ^           |                v
      unit   integrate      |           |              deploy
           |                |           |                |
           |                |           |                v
           |________________|___________|             monitoring  
                            |____________________________|
  </pre>  

* Complete flow/Architectur: 
  > Design the entire machine learning operations pipeline by using various tools
  <pre>
  Github <- Git <- [building] /________       (Docker file)          _____________
                       |      \        |           |                |             |   
                       |               |           |                |             v
                       |               |        (Image)             |         Azure repo
                       |               |           |                |             |
                       |               |           | CD             |             | CD'  
                       v               |           v                |             v
  Pytest <- tox <- [testing] -> CI--------> Github Action server    |        Azure server
                  /         \          |                            |             |
              [unit]    [integrate]    |                            |             |
                |            |         | CT {AirFlow}               |             v
           test cases   test cases     |____________________________|_______Monitoring {evidently.ai}
                |____________|______________________________________| 
  </pre>

* Tools in this particular project
  <pre>
  Data management -- DVC
  Experiment tracking -- MLFlow
  Model registry -- Dags Hub
  BentoML
  </pre>

* Agenda
  1. Jupyter implementation
  2. END-END project
  3. Various tools Adding
  4. Deploy

## (39:50) Implementation (in VS Code)

* 完成 `init_setup.sh`，執行 `base init_setup.sh`

* If it didn't activate the "env" environment，手動執行 `source activate ./env`

* 執行 `pip install -r requirements_dev.txt`

* (57:00) Git commit 提交 ()

* (1:04:00) `experiment/experiments.ipynb`

# Lecture 10 Note -- [MLOps End to End Project - Model Building](https://www.youtube.com/watch?v=6TvfUdnUXNY)

* 自行建立 `notebooks/data` 資料夾，放入 `raw.csv`、`test.csv`、`train.csv`三個資料檔案 -- [Resource](https://github.com/abhijitpaul0212/GemstonePricePrediction/tree/master/artifacts)
  > `raw.csv` is `gemstone.csv` used in Lecture 10.

* (32:45) Machine Learning Pipeline
  1. data ingestion
  2. EDA
  3. Preprocessing
  - outlier data
  - transforming data
  - handling missing value
  - imbalanced data
  - encoding step
  4. Model

# Lecture 11 Note -- [MLFlow & DVC integration](https://www.youtube.com/watch?v=fhWVCMjXmw0)

* (21:36) 完成 `src/exception/exception.py`
  > 在根目錄執行 `python -m src.exception.exception`，用以測試(Colab 沒問題)

* (30:55) 建立 `test.py`
  ```python
  import sys
  print(sys.exc_info())
  ```
  > Colab 測試時顯示: (None, None, None)

* (41:38) 完成 `src/logger/logging.py`
  > (44:31) 執行 `python src/logger/logging.py` \
  > > Lecture demo 時，執行 `python src/logger/logging.py` 出錯，錯誤訊息“circular import” \
  >
  > (47:46) 在 `experiment/experiments.ipynb` 上，將 `logging.py` 內容貼到 cell 中執行，沒問題
  > > Lecture demo 接著執行 `python test.py` ，也沒有問題 
  >
  > 小結論：在其他檔案使用 `from src.logger.logging import logging` 沒問題

* 建立 `src/logger/__init__.py` 與 `src/exception/__init__.py`

* (54:08) 完成 `test.py` (測試 `logging.py` 功能)
  > (55:08) 執行 `python test.py`

* (57:43) Git commit ("logger and exception updated")

* (1:05:00) 建立 `src/components/data_ingestion.py` (內容未完成)

* (1:13:33) 建立 `src/components/data_transformation.py` (內容未完成)

* Machine Learning
  1. Training Pipeline
  - 1. Data Ingestion
  - 2. Data Transformation -> OBJ -- Scaling, Encoded
  - 3. Model Training
  - 4. Evaluation
  2. Prediction Pipeline -- bulk, single value
  - having Data
  - 1. Transformation
  - 2. Prediction

* (1:19:51) 完成 `src/utils/utils.py`

* (1:26:21) 建立 `src/components/model_trainer.py`

* (1:29:30) 建立 `src/components/model_evaluation.py`

* (1:30:55) Git commit ("structure updated")


* 1:35:00 a few more concepts
  <pre>
  SRC
    |----component
              |----------Data Ingestion, DI         
              |----------Data Transformation, DT     ~~~\  Pipeline     
              |----------Model Trainer, MT           ~~~/     |------> Training
              |----------Model Evaluation, ME                 |------> Prediction
                                                                                            
                                                                                            
      (config)   (config)   (config) 
        |          |          |
        v          v          v
        |DI| ----> |DT| ----> |MT| ----> |ME|
        |       ^  |       ^  |       ^
        v       |  v       |  v       |   
        (artifact) (artifact) (artifact) 
  </pre>


* (1:40:00) 完成 `src/components/data_ingestion.py`
  > 用 data=pd.read_csv("https://raw.githubusercontent.com/henrykohl/Gemstone-Price-Prediction-End-to-End-Pipeline/refs/heads/main/notebooks/data/raw.csv") \
  > 取代 data=pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/fsdsmendtoend/main/notebooks/data/gemstone.csv") \
  > (1:48:12) 執行 `python src/components/data_ingestion.py`
  > > 建立 `artifact` 資料夾，並包含三個檔案

* (1:55:05) 完成 `src/components/data_transformation.py`

* (1:55:40) 完成 `src/components/model_trainer.py`

* (1:56:15) 建立 `src/pipeline/training_pipeline.py` (2:08:05 完成)
          
* (2:11:08) 執行
  ```bash
  source activate ./env
  python src/pipeline/training_pipeline.py
  ```

* (2:17:05) Git commit

# Lecture 12 Note -- [MLFlow & DVC integration - Part 2](https://www.youtube.com/watch?v=FeJkHlCX3m0)

* (12:48) recap `src/pipeline/training_pipeline.py`

* (14:00) 建立 `src/pipeline/prediction_pipeline.py` (47:00 完成，除class CustomData)

* (16:45) 執行
  ```bash
  source activate ./env
  python src/pipeline/training_pipeline.py
  ```

* (20:32) 建立 `app.py`

* (20:50) 開始編寫 `src/pipeline/prediction_pipeline.py` 

* (23:10) 回看 `src/utils/utils.py` 的 `def load_object(file_path):`

* (24:23) Git commit (create prefiction file) -- 只完成 import 的那部分
  > `git config -l`

* (30:00) 繼續編寫 `src/pipeline/prediction_pipeline.py`  

* (36:00) prediction pipeline
  1. Data 
      - Bulk 
      - Single
  2. Preprocessing
  3. Model --> Prediction
  4. Evaluate

* (47:00) Git commit -- class CustomData 未完成

* (49:30) 開始編寫 `app.py`

* (53:40) 建立 `/templates`

* 完成 `/templates/index.html`

* 完成 `app.py` (除了 `predict_datapoint()` 之外)
  ```python
  def predict_datapoint():
  ```

* (57:50) 測試，執行 `python app.py` 後，開啟 browser (網址最後為 `:8000`)

* (58:50) 完成 `/templates/form.html`

* (1:00:20) 完成 `app.py` 中 `predict_datapoint()`

* (1:03:00) 執行 `python app.py` 後，開啟 browser (網址最後為 `:8000/predict`) -- 檢視頁面

* (1:23:00) 完成 `/templates/result.html`

* (1:24:42) 執行 `python app.py` 後，開啟 browser (網址最後為 `:8000/predict`)
  <pre>
  Carat: 1.23
  Depth: 23
  Table: 5
  x: 0.32
  y: 5.1
  z: 1.1432
  Cut: Good
  Color: F
  Clarity: VVS2
  結果--25981.28
  </pre>

* (1:33:55) Git commit "app created"
