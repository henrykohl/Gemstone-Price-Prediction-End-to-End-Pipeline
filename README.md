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

* (1:55:40) 完成 `src/components/model_trainer.py` (2:08:05 完成)

* (1:56:15) 建立 `src/pipeline/training_pipeline.py` 
          
* (2:11:08) 執行
  ```bash
  source activate ./env
  python src/pipeline/training_pipeline.py
  ```

* (2:17:05) Git commit

* 注意，`src/components/model_evaluation.py` 尚未完成

# Lecture 12 Note -- [MLFlow & DVC integration - Part 2](https://www.youtube.com/watch?v=FeJkHlCX3m0)

* (12:48) recap `src/pipeline/training_pipeline.py`

* (14:00) 建立 `src/pipeline/prediction_pipeline.py` (47:00 完成，除class CustomData)

* (16:45) 執行
  ```bash
  source activate ./env
  python src/pipeline/training_pipeline.py
  ```

* (20:32) 建立 `app.py` (未完成)

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
  > label 的 "for" 關聯 select 的 "id" ?? \
  > name 的值是要給 `app.py` 使用的

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

# Lecture 13 Note -- [MLFlow & DVC integration - Part 3](https://www.youtube.com/watch?v=aS466KYOxB4)

* (12:42) Review `app.py`
  > `source activate ./env` \
  > `python app.py`
  > - 開啟 browser (網址最後為 `:8000` 與 `:8000/predict`)

* (18:05) 啟用新個 Conda Lab 
  > 也算是要建立新的 GitHub \
  
  
* (18:00~1:21:00)  此部分 Lecture 筆記，參考 [practicstools GitHub](https://github.com/henrykohl/practicstools)


---

* (1:21:10) 切換回到 Gemstone-Price-Prediction-End-to-End-Pipeline 專案

* (1:22:22) 建立 `src/components/model_evaluation.py`

* (1:42:05) 輸入 "give me all mlflow methods" 在 ChatGpt 中

* (1:46:15) 修改(新增) `src/pipeline/training_pipeline.py`

* (1:47:15) 執行 `python src/pipeline/training_pipeline.py` (Lecture Demo 遇到一些錯誤)

* (1:57:20) 成功執行 `python src/pipeline/training_pipeline.py`

* (2:03:10) Git commit ("mlflow added")

* 除錯筆記 -- 直些執行 Lecture demo 會產生兩個錯誤： 
  - Error 1：<font color="orange">No module named 'distutils._modified'</font>
  - Error 2：<font color="orange">PermissionError: [Errno 13] Permission denied: '/config'</font>

* Error 1 解決方式：安裝 `setuptools==68.2.2`，將其加入`requirements_dev.txt`
  > 執行 `pip install -r requirements_dev.txt` 安裝

* Error 2 解決方式：在 replicate 此專案的 repository 時，初始要把資料夾 `/mlruns` 刪除
  > 執行 `python src/pipeline/training_pipeline.py` 回新建一個資料夾 `/mlruns`

# Lecture 14 Note -- [DVC & Airflow in End-to-End Project](https://www.youtube.com/watch?v=WwwvtPgjpQw)

* (15:05) 開啟 [practicaltools](https://github.com/henrykohl/practicstools) Github
  > 清空(移除所有檔案)

* (17:17) 執行 
  ```bash
  ls -a
  rm -rf .git
  ls -a
  ```

* [DVC Documentation](https://dvc.org/doc)

* (22:30) 執行 `git remote -v`
  > haven't initialized the git. So it shows "fatal: not a git repository"

* 執行 
  ```bash
  git init
  ls -a
  git status
  touch README.md
  git status
  #git commit -m "first commit"
  git add README.md
  git config --global user.email "you@example.com"
  git config --global user.name "Your name"
  git commit -m "first commit"
  git status
  ```

* (28:27) without 'git', we cannot use DVC.

* (38:43) `touch test.py`
  ```python
  import pandas as pd
  Data=[
    {"name":"sunny","age":28,"city":"bhopal"},
    {"name":"sudhanshu","age":33,"city":"Delhi"},
    {"name":"krish","age":35,"city":"bengalore"},
    {"name":"vikas","age":29,"city":"pune"}
  ]

  Data = pd.DataFrame(Data)

  Data.to_csv("data/data.csv",index=False)
  ```
* 建立 `/data` 資料夾

* (33:20) 執行
  ```bash
  git status
  git add test.py
  git commit -m "second commit"
  git log

  git checkout 編號 # 編號是 commit id
  ```

* (37:20) 執行
  ```bash
  python test.py
  pip list # pandas 還未安裝
  conda create -p venv python=3.8 -y
  ```

* (38:24) 執行 
  ```bash
  touch requirements.txt
  conda activate ./venv
  pip install -r requirements.txt
  ````
  > 建立 `requirements.txt` 
  > > ```python
  > > pandas
  > > ```

* (40:20) 執行 `python test.py`

* (44:29) 修改 `requirements.txt`
  ```txt
  pandas
  dvs
  ```
* [Get Started with DVC](https://dvc.org/doc/start)

* (45:55) 再次執行 `pip install -r requirements.txt`

* 執行 
  ```bash
  python
  import dvc
  exit()

  git status ## 顯示 untracked files
  ```

* (48:45) 執行 `touch .gitignore`
  ```txt
  /venv
  ```
  
* (51:12) 執行 `dvc init`
  > 自動建立 `.dvcignore`

* (53:08) 查看 `.dvc` 資料夾

* (56:35) 執行 `git status`
  ```txt
  .dvc/.gitignore
  .dvc/config
  .dvcignore
  ```
  > Changes to be committed automatically

* (58:10) 執行 
  ```bash
  git commit -m "third commit"
  git status
  ```

* (1:00:07) `dvc add data/data.csv`
  > 產生 `data.csv.dvc` 檔案

* (1:04:31) 
  <pre>
  We never use git/github for data management/versioning

    git/github
      |
      |------> Source Code Management[SCM] (O) / Data Tracking (X)
      1. Storage size (<25MB)
      2. Conflict resolution (SCM:version)
      3. Performance (pushing data causes degradation performance)
  </pre>

* (1:13:40) 執行 `git status`

* (1:14:45) 執行 `git commit -m "fourth commit"`
  > "nothing added to commit..."

* (1:15:59) 新增一行資料 `data/data.csv`
  ```csv
  ...
  dipesh,31,agra 
  ```

* 在 `data.csv.dvc` 查看 md5 的 id

* (1:16:21) 執行 `dvc add data/data.csv`
  > 在 `data.csv.dvc` 中 md5 的 id 發生改變

* (1:17:00) 執行 `git status`，沒有新的改變 

* `.dvc` 資料夾中產生 `/cache` 資料夾

* (1:18:40) 再新增一行資料 `data/data.csv`
  ```csv
  ...
  rahul,30,goa 
  ```

* (1:18:52) 執行 `dvc add data/data.csv`
  > `.dvc/cache` 中 又會新增一個資料夾 \
  > 在 `data.csv.dvc` 中 md5 的 id 又再次發生改變
