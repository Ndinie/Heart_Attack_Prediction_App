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
    st.write('This App is to analyse whether you have heart attack or not')
    
with col2:
    st.subheader('Please fill in the details of the person under consideration and click on the button below!')
    with st.form("Diabetes Predictor App"):
        age = st.number_input("Age in Years", 1, 150, 25, 1)
        sex = st.slider("sex", 0, 1)
        exang = st.slider("exercise induced angina", 0, 99, 20, 1)
        ca = st.slider('number of major vessels', 0, 122, 69, 1)
        cp = st.slider("chest pain indication", 0, 846, 79, 1)
        trtbps = st.slider("resting blood pressure", 0.0, 67.1, 31.4, 0.1)
        chol = st.slider("cholesterol level", 0.000, 2.420, 0.471, 0.001)
        fbs = st.slider("fasting blood sugar", 0.000, 2.420, 0.471, 0.001)
        rest_ecg = st.slider("resting electrocardiographic results", 0.000, 2.420, 0.471, 0.001)
        thalach = st.slider("maximum heart rate", 0.000, 2.420, 0.471, 0.001)

        row = [age, sex, exang, ca, cp, trtbps, chol, fbs, rest_ecg, thalach]


        # Every form must have a submit button.
        submitted = st.form_submit_button("Analyse")
        if submitted:
            new_data=np.expand_dims(row,axis=0)
            outcome=model.predict(new_data)[0]

            if outcome==0:
                st.subheader("You have no heart attack! Keep it Up!!")
            else:
                st.subheader('From our database, you are predicted to have a heart attack.')

