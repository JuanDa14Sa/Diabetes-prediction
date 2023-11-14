import streamlit as st
import joblib

model = joblib.load('diabetes_model.pkl')

st.title('Diabetes prediction :syringe:')
st.caption('Created by: Juan David Sánchez')
st.text('This app is not a substitute for medical advice and is for educational purposes only.')
st.header('Enter the following details to know if you have diabetes or not')
glucose = st.number_input('Enter glucose')
bmi = st.slider('Enter bmi', 0.0, 100.0)
age = st.number_input('Enter age', min_value=21, max_value=100)
dpf = st.number_input('Enter Diabetes Pedigree Function')
num_preg = st.number_input('Enter number of pregnancies', min_value=0, max_value=20)
blood_pressure = st.number_input('Enter blood pressure')
insulin = st.number_input('Enter insulin')
features_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'Insulin', 'BMI',
       'DiabetesPedigreeFunction', 'Age']
input_data = [[num_preg, glucose, blood_pressure, insulin, bmi, dpf, age]]
# prediction = model.predict(input_data)
prediction_prob = model.predict_proba(input_data)


st.write(f'There is a {prediction_prob[0][1]*100:.2f}% chance that you have diabetes.')
if prediction_prob[0][1] > 0.5:
    st.write('Take care of your health! :anguished:')
else: 
    st.write('You are healthy! :smile:')



