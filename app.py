import streamlit as st
import pandas as pd
import sklearn
import pickle
import numpy as np


st.title("House Loan Prediction")
st.write("Simple Home Loan Predciton Using a Random Forest Classifer")


model=pickle.load(open('model.pkl','rb'))
data=pd.read_csv('data//train.csv')

nav=st.sidebar.radio('Navigation',['Home','Prediction','Contribute','Insights','Feedback'])
if nav=='Home':
    st.title('Acme Insurance Inc.')
    st.subheader('Annual Health Expenditure Prediction')
    st.image('data//Housing loan.jpg')
    if st.checkbox('Show Data'):
        st.dataframe(data)


if nav=='Prediction':

    st.subheader('Please give the following information:')
    
    Loan_ID = st.number_input('Loan_ID')
   
    Gender = st.number_input('Gender: Male= 1 Female =0',min_value= 0 ,max_value=1)
    
    Married = st.number_input('Married', min_value=0.0, max_value=100.0, step=1.0)

    Education = st.number_input('Education: Graduate=1,Not a Graduate=0 ', min_value=0.0, max_value=100.0, step=1.0)
    
    Self_Employed = st.number_input('Self_Employed: Yes=1 No=0', min_value=0.0, max_value=100.0, step=1.0)
    
    ApplicantIncome = st.number_input('ApplicantIncome', min_value=0.0, step=1.0)

    CoapplicantIncome = st.number_input('CoapplicantIncome', min_value=0.0, step=1.0)

    LoanAmount = st.number_input('LoanAmount', min_value=0.0, step=1.0)

    Loan_Amount_Term = st.number_input('Loan_Amount_Term', min_value=0.0, step=1.0)

    Credit_History = st.number_input('Credit_History: Yes=1 No=0', min_value=0.0, step=1.0)

    st.header("Type  1 for YES and 0 for NO in any one box below")
    Urban = st.number_input('Urban: Yes=1 No=0', min_value=0.0, step=1.0)

    Semi_Urban = st.number_input('Semi_Urban: Yes=1 No=0', min_value=0.0, step=1.0)

    Rural = st.number_input('Rural: Yes=1 No=0', min_value=0.0, step=1.0)
    
    input = np.array([Loan_ID , Gender, Married, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Urban, Semi_Urban, Rural])
    input = input.reshape(1, 13)    


    if st.button('Predict'):
        st.title('The Eligibity of getting a Home Loan ' + str(round(int(model.predict(input)))))

if nav == "Contribute":
    st.header("Contribute to our dataset by giving your data")
    Loan_ID = st.number_input('Loan_ID', min_value=0.0, max_value=1000.0, step=1.0)
   
    Gender = st.number_input('Gender: Male= 1 Female =0',min_value= 0 ,max_value=1)
    
    Married = st.number_input('Married', min_value=0.0, max_value=100.0, step=1.0)

    Education = st.number_input('Education: Graduate=1,Not a Graduate=0 ', min_value=0.0, max_value=100.0, step=1.0)
    
    Self_Employed = st.number_input('Self_Employed: Yes=1 No=0', min_value=0.0, max_value=100.0, step=1.0)
    
    ApplicantIncome = st.number_input('ApplicantIncome', min_value=0.0, step=1.0)

    CoapplicantIncome = st.number_input('CoapplicantIncome', min_value=0.0, step=1.0)

    LoanAmount = st.number_input('LoanAmount', min_value=0.0, step=1.0)
    Loan_Amount_Term = st.number_input('Loan_Amount_Term', min_value=0.0, step=1.0)
    Credit_History = st.number_input('Credit_History: Yes=1 No=0', min_value=0.0, step=1.0)
    st.header("Type  1 for YES and 0 for NO in any one box below")
    Urban = st.number_input('Urban: Yes=1 No=0', min_value=0.0, step=1.0)

    Semi_Urban = st.number_input('Semi_Urban: Yes=1 No=0', min_value=0.0, step=1.0)

    Rural = st.number_input('Rural: Yes=1 No=0', min_value=0.0, step=1.0)

    
    if st.button("submit"):
        to_add = {"Loan_ID":[Loan_ID], "Gender": [Gender],"Married": [Married], "Education":[Education], "Self_Employed":[Self_Employed],
       'ApplicantIncome':[ApplicantIncome], 'CoapplicantIncome':[CoapplicantIncome], 'LoanAmount':[LoanAmount],
       'Loan_Amount_Term':[Loan_Amount_Term], 'Credit_History':[Credit_History], 'Urban':[Urban], 'Semi_Urban':[Semi_Urban], 'Rural':[Rural]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("data//expenditure.csv", mode='a', header=False, index=False)
        st.success("Submitted")

if nav=='Insights':
    st.title('Insights from the dataset')
    st.image('data//ED.jpg')
    st.markdown('''Graduated People has greater possibilities of getting  Home Loan Approved''')
    st.image('data//EM.jpg')
    st.markdown('''People working in company  has greater possibilities of getting  Home Loan Approved 
    when the people who are selfemployed have less possibilites because Occupation ''')
    st.image('data//Gender.jpg')
    st.markdown('''Male has higher chance of getting home loan rather than Female''')
    st.image('data//marital.jpg')
    st.markdown('''Married People are have higher chance of approval of home loan 
    while Unmarried people are less likely to be approved ''')
    st.image('data//propertyarea.jpg')
    st.markdown('''Semi-Urban People have higher chances of getting their loan approved when comparitively the Urban and Rural people are less likely to get approved''')
    
if nav=='Feedback':
    st.title('Please provide with your feedback about the project')
    feedback = st.text_area("enter text here",height = 100)
    if st.button("submit"):
        to_addtext ={'Feedback':[feedback]}
        to_addtext = pd.DataFrame(to_addtext)
        to_addtext.to_csv("data//feedback.csv",mode='a',header=False,index=False)
        st.sucess("submitted")
    
    
    
