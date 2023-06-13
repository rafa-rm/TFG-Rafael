import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
  
# loading in the model to predict on the data
pickle_in = open('../model.pkl', 'rb')
classifier = pickle.load(pickle_in)
  
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(features):  
   
    prediction = classifier.predict([[0.137671,	0.377921, 0.831427,	0.383320, 0.004049,	
                                      False, False, True,	False, False, False, True, 
                                      False, False, False]])    
    print(prediction)
    return prediction
      
  
# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("Heart Disease Prediction")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit Heart Disease Classifier ML App </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction

    age = st.text_input("Idade", "Digite aqui")
    sex = st.text_input("Sexo", "Digite aqui")
    cp = st.text_input("Tipo de dor no peito", "Digite aqui")
    rbps = st.text_input("Pressão sanguínea em repouso (mm Hg)", "Digite aqui")
    chol = st.text_input("Colesterol Sérico (mg/dl)", "Digite aqui")
    fbs = st.text_input("Fasting blood sugar", "Digite aqui")
    ecg = st.text_input("ECG em repouso", "Digite aqui")
    max_heart = st.text_input("Máxima frequência cardíaca", "Digite aqui")
    ex_angina = st.text_input("Angina induzida por exercício", "Digite aqui")
    oldpeak = st.text_input("Oldpeak", "Digite aqui")
    slp = st.text_input("Slope peak exercise", "Digite aqui")

    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction([age,sex,cp,rbps,chol,fbs,ecg,
                            max_heart,ex_angina,oldpeak,slp])
    st.success('The output is {}'.format(result))
     
if __name__=='__main__':
    main()