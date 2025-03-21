import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the trained model
with open("best_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Diabetes Risk Prediction App")

st.write("Enter the details below to predict the risk of diabetes.")

# Input fields for user
HighBP = st.selectbox("High Blood Pressure (0 = No, 1 = Yes)", [0, 1])
HighChol = st.selectbox("High Cholesterol (0 = No, 1 = Yes)", [0, 1]) 
Bmi = st.number_input("Body Mass Index (BMI)", min_value=10.0, max_value=100.0, step=0.1)
Stroke = st.selectbox("Ever had a Stroke (0 = No, 1 = Yes)", [0, 1])
HeartDiseaseorAttack = st.selectbox("Heart Disease or Attack (0 = No, 1 = Yes)", [0, 1])
HvyAlcoholConsump = st.selectbox("Heavy Alcohol Consumption (0 = No, 1 = Yes)", [0, 1])
GenHealth = st.selectbox("General Health (1 = Excellent, 5 = Poor)", [1, 2, 3, 4, 5])
MentHealth = st.number_input("Days of Poor Mental Health (0-30)", min_value=0, max_value=30, step=1)
PhysHealth = st.number_input("Days of Poor Physical Health (0-30)", min_value=0, max_value=30, step=1)
DiffWalk = st.selectbox("Difficulty Walking (0 = No, 1 = Yes)", [0, 1])
Age = st.selectbox("Age Group (1 = 18-24, 13 = 80+)", list(range(1, 14)))
Income = st.selectbox("Income Scale (1 = <10K, 8 = >75K)", list(range(1, 9)))


# Predict function
if st.button("Predict Diabetes Risk"):
    # Prepare input data
    input_data = pd.DataFrame([[HighBP,HighChol,Bmi,Stroke,GenHealth,MentHealth,PhysHealth,DiffWalk
                            ,HeartDiseaseorAttack,HvyAlcoholConsump,Age,Income]],columns=['HighBP','HighChol','BMI','Stroke','GenHealth','MentHealth','PhysHealth','DiffWalk'
                            ,'HeartDiseaseorAttack','HvyAlcoholConsump','Age','Income'])
    
    prediction = model.predict(input_data)
    
    # Display result
    result = "Diabetes" if prediction == 1  else "No Diabetes"
    st.subheader(f"Prediction: **{result}**")
