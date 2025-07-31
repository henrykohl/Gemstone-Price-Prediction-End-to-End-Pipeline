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
                              \        |           |                |             |                                |           |                |             v
                                       |        (Image)             |         Azure repo
                                       |           |                |             |
                                       |           | CD             |             | CD'  
                                       |           v                |             v
  Pytest <- tox <- [testing] -> CI--------> Github Action server    |        Azure server
                                       |                            |             |
              [unit]    [integrate]    |                            |             |
                                       | CT {AirFlow}               |             v
           test cases   test cases     |____________________________|_______Monitoring {evidently.ai}
                |___________|_______________________________________| 
  </pre>