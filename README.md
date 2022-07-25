# Project Title
Predictive Model on Heart Attack

# Project Description
According to World Health Organisation (WHO), every year around 17.9 million deaths are due to cardiovascular diseases (CVDs) predisposing CVD becoming the leading cause of death globally. CVDs are a group of disorders of the heart and blood vessels, if left untreated it may cause heart attack. Heart attack occurs due to the presence of obstruction of blood flow into the heart. The presence of blockage may be due to the accumulation of fat, cholesterol, and other substances. Despite treatment has improved over the years and most CVD’s pathophysiology have been elucidated, heart attack can still be fatal.

# Data Description
Thus, clinicians believe that prevention of heart attack is always better than curing it. After many years of research, scientists and clinicians discovered that, the probability of one’s getting heart attack can be determined by analysing the patient’s age, gender, exercise induced angina, number of major vessels, chest pain indication, resting blood pressure, cholesterol level, fasting blood sugar, resting electrocardiographic results, and maximum heart rate achieved.

# How to install and run the project
This project can be run via [Google Colab]([https://colab.research.google.com/drive/1T0dhh7LAojDREjf9otVbAjLyhqvEdl2B?usp=sharing](https://colab.research.google.com/?utm_source=scs-index)) with the help of GPU and without additional modules installation.

# How to use the project
You can access the full codes [Heart_ Attack_Prediction_main](https://colab.research.google.com/drive/10TdIMgB3o8LG12AfzT1ECkHpEu-iyA0z?usp=sharing) to test it out.

After training the dataset, we able to acquire its classification report as below!

![Classification Report](https://github.com/Ndinie/Heart_Attack_Prediction_App/blob/main/static/classification-report.png)

Even with this accuracy rate, we able to achieve almost 90% accuracy on our test data as below:

![Test-data-3](https://github.com/Ndinie/Heart_Attack_Prediction_App/blob/main/static/Test-data-3.png)

But there is also possibilities that our model predict the test data incorrectly.
Thus to increase the accuracy, we can add more sample data to test on or we can even finetune our hyperparameter of our pipelines.

# Credits
Great appreciation to [RASHIK RAHMAN](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset) for providing this dataset!

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)

