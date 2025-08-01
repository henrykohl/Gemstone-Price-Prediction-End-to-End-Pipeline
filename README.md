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