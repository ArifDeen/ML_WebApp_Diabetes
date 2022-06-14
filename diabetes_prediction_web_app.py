import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open("trained_model.sav", 'rb'))


# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Patient is not diabetic'
    else:
      return 'Patient is diabetic'
  
    # Convert User report 
def convert_userInput_into_number(fieldName, option):
    if fieldName == option:
        fieldName = 1
    else:
        fieldName = 0
    return fieldName   

  
def main():
    
    
    # giving a title
    st.title('Diabetes Prediction Web App')
    
    
    # getting the input data from the user
    Sex = st.text_input('Sex')
    Sex = convert_userInput_into_number(Sex, 'Male')
    print(Sex)
    Glucose = st.text_input('Glucose Level')
    HighChol = st.text_input('Does the Patient have high level of cholesterol?')
    HighChol = convert_userInput_into_number(HighChol,'Yes')
    PhysActivity = st.text_input('Does the Patient engage in physical activities')
    PhysActivity = convert_userInput_into_number(PhysActivity,'Yes')
    BMI = st.text_input('Body Mass Index of Patient')
    Stroke = st.text_input('Does the Patient have Stroke?')
    Stroke = convert_userInput_into_number(Stroke, 'Yes')
    HeartDiseaseorAttack = st.text_input('Has the Patient ever had Heart Disease or Attack?')
    HeartDiseaseorAttack = convert_userInput_into_number(HeartDiseaseorAttack,'Yes')
    EyeProb = st.text_input('Does the Patient have Eye Defect?')
    EyeProb = convert_userInput_into_number(EyeProb,'Yes')
    BloodPressure = st.text_input('Blood Pressure of Patient')
    Age = st.text_input('Age of Patient')
    

    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Sex, Glucose, HighChol, PhysActivity, BMI, Stroke, HeartDiseaseorAttack, EyeProb, BloodPressure, Age])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
