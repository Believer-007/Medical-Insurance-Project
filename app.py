import streamlit as st
import pandas as pd 
import pickle

model = pickle.load(open('med_model.pkl','rb'))

def main():
    st.title('Medical Insurance Cost Predictor')

    Age = st.text_input('Age')
    Sex = st.text_input('Sex (Enter 0 for Male and 1 for Female)')
    Bmi = st.text_input('Bmi')
    Children = st.text_input('Children')
    Smoker = st.text_input('Smoker (Enter 0 for NO and 1 for Yes)')
    BMI_category = st.text_input('BMI_category (Obesity: 1, Overwight: 2, Normal: 3, Weightloss: 4)')
    #region = st.text_input('region')

    if st.button('Insurance Price'):
        makeprediction = model.predict([[Age,Sex,Bmi,Children,Smoker,BMI_category]])
        output = round(makeprediction[0],2)
        st.success('You can expect price of somewhere around {}'.format(output))


if __name__=='__main__':
    main()