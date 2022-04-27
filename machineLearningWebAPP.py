import numpy as np
import streamlit as st
import pickle


# loading the saved model
loaded_model = pickle.load(open('C:/Users/Denyse/Desktop/machineDeployment/trained_model.sav','rb'))

# creating function for prediction
def diabetes_prediction(input_data):
     # change input data into numpy array
     input_data_as_numpy_array = np.asarray(input_data)

     # reshape thhe arraay
     input_data_reshape = input_data_as_numpy_array.reshape(1,-1)

     # standardise the input data
     #std_data = scaler.transform(input_data_reshape)
     #print(std_data)
     prediction = loaded_model.predict(input_data_reshape)
     print(prediction)



     if (prediction == 0):
      return 'person is not a diabetic'
     else:
      return 'person is a diabetic'

def main():
     #giving a tittle
    st.title('Diabetes prediction web App')

     #getting the input dta from the user

    pregnancies = st.text_input('number of pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure =  st.text_input('BloodPressure value')
    SkinThickness =  st.text_input('SkinThickness value')
    Insulin =  st.text_input('Insulin level')
    BMI =  st.text_input('BMI value')
    DiabetsPedigreeFuction =  st.text_input('DiabetsPedigreeFuction level')
    Age =  st.text_input('Age of person')

     # code for prediction
    diagnosis = ""

      #creating a button for prediction 

    if st.button('Diabets test reslt'):

          diagnosis = diabetes_prediction([pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetsPedigreeFuction,Age])
    st.success(diagnosis)



if __name__ == '__main__':
    main()

