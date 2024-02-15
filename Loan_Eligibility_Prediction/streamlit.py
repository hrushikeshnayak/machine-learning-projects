import streamlit as st
import pandas as pd
import joblib
import requests

# map age categories
def map_age(age):
    age_mapping = {
        '<25': 1,
        '25-34': 2,
        '35-44': 3,
        '45-54': 4,
        '55-64': 5,
        '65-74': 6,
        '>74': 7
    }
    return age_mapping.get(age, 0)

# Load model

# Function to download file from GitHub
def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

# URL of the raw file on GitHub
github_raw_url = 'https://raw.githubusercontent.com/hrushikeshnayak/machine-learning-projects/main/Loan_Eligibility_Prediction/model.joblib
'

local_filename = 'model.joblib'

# Download the file
download_file(github_raw_url, local_filename)

model = joblib.load(local_filename)

st.title('Loan Eligibility Prediction App')

st.write("""
This app evaluates loan eligibility using key banking metrics. By analyzing input parameters like loan amount, upfront charges, property value, income, credit score, loan term, loan-to-value ratio, and debt-to-income ratio, it provides insights into loan approval likelihood.
""")

# Sidebar for user input
st.sidebar.header('Input Parameters')

# Input fields in the sidebar
age = st.sidebar.selectbox('Age Range', ['<25', '25-34', '35-44', '45-54', '55-64', '65-74', '>74'], index=2)
loan_amount = st.sidebar.text_input('Loan Amount', '0', help="Total loan amount")
upfront_charges = st.sidebar.text_input('Upfront Charges', '0.0', help="Initial charges for the loan")
property_value = st.sidebar.text_input('Property Value', '0', help="Value of the property associated with the loan")
income = st.sidebar.text_input('Income', '0', help="Loan applicant income")
term = st.sidebar.slider('Term (Months)', value=0, min_value=0, max_value=500, step=1, format='%d', help="Loan duration in months")
credit_score = st.sidebar.slider('Credit Score', value=300, min_value=300, max_value=900, step=1, format='%d', help="Credit score of the applicant")
ltv = st.sidebar.slider('Loan to Value (LTV)', value=0.0, min_value=0.0, max_value=100.0, step=0.01, format='%f', help="(Loan to Value): Ratio of loan amount to property value")
dtir1 = st.sidebar.slider('Debt to Income Ratio (DTI)', value=0, min_value=0, max_value=100, step=1, format='%d', help="(Debt to Income Ratio): Debt/income ratio of the applicant")

# Map age to numerical category
age_mapped = map_age(age)


if st.sidebar.button('Predict'):
    input_data = pd.DataFrame({
        'age': [age_mapped],
        'loan_amount': [float(loan_amount)],
        'Upfront_charges': [float(upfront_charges)],
        'term': [term],
        'property_value': [float(property_value)],
        'income': [float(income)],
        'Credit_Score': [credit_score],
        'LTV': [ltv],
        'dtir1': [dtir1]
    })

    prediction = model.predict(input_data)
    
    # Display prediction result
    st.subheader('Prediction Result')
    if prediction[0] == 1:
        st.write('Based on the provided information, the prediction suggests that the loan is likely to be granted.')
    else:
        st.write('Based on the provided information, the prediction suggests that the loan is unlikely to be granted.')
