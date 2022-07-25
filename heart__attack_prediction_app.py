# -*- coding: utf-8 -*-
"""Heart_ Attack_Prediction_app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WkgvIUqbFhV1xDMfWsFXXK1_Xct1xkJ2
"""
import subprocess
import sys
import streamlit as st

st.set_page_config(page_title="Heart Attack Prediction App", page_icon=":hospital:", layout="wide")

@st.cache
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
install('pickle-mixin')
install('sklearn')

import pickle
import os
import numpy as np
import warnings
warnings.filterwarnings('ignore')

MODEL_PATH=os.path.join(os.getcwd(),'model','best_estimator.pkl')
with open(MODEL_PATH,'rb') as file:
    model=pickle.load(file)

import joblib
import pandas as pd
from PIL import Image

col1, col2 = st.columns(2)

with col1:
    st.title('Heart Attack Prediction App')
    st.write('This Heart Attack Prediction App is to analyse whether you have the chance getting a heart attack or not')
    image = Image.open(os.path.join(os.getcwd(),'static','heart-image.jpg'))
    st.image(image, use_column_width=True)
    
with col2:
    st.subheader('Please fill in the details of the person under consideration and click on the button below!')
    with st.form("Heart Attack Prediction App"):
        age = st.number_input("Age", 1, 100)
        sex = st.selectbox("Sex (0 = Female, 1 = Male)", 0, 1)
        cp = st.selectbox('Chest Pain Type (0 = Typical Angina, 1 = Atypical Angina, 2 = Non-anginal Pain, 3 = Asymptomatic)',(0,1,2,3))
        trtbps = st.slider("Resting Blood Pressure", 0, 200)
        chol = st.slider("Cholesterol Level", 100, 600)
        fbs = st.selectbox("Fasting Blood Sugar (1 = True, 0 = False) ", 0, 1)
        rest_ecg = st.slider("Resting Electrocardiographic Results (0 = Normal, 1 = ST-T wave normality, 2 = Left ventricular hypertrophy) ", 0, 1, 2)
        thalach = st.slider("Maximum Heart Rate", 0, 220)
        exng = st.selectbox("Exercise Induced Angina (1 = Yes, 0 = No)", 0, 1)
        oldpeak = st.slider("ST Depression Induced by Exercise Relative to rest",0.0,7.0,0.8,0.1)
        slp = st.selectbox('Slope', 0, 2)
        caa = st.selectbox('Number of Major Vessels', 0, 3)
        thall = st.selectbox('Thalium Stress Test result', 0, 2, 3)
        
        row = [age, sex, cp, trtbps, chol, fbs, rest_ecg, thalach, exng, oldpeak, slp, caa, thall]

        # Every form must have a submit button.
        submitted = st.form_submit_button("Analyse")
        if submitted:
            new_data=np.expand_dims(row,axis=0)
            outcome=model.predict(new_data)[0]

            if outcome==0:
                st.subheader("You have no heart attack! Keep it Up!!")
            else:
                st.subheader('From our database, you are predicted to have a heart attack.')

