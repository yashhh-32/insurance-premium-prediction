import streamlit as st
from prediction_helper import predict

# Page config
st.set_page_config(page_title="Health Insurance Cost Predictor", page_icon="💰", layout="centered")

# Title with subtitle
st.markdown(
    """
    <h1 style="text-align:center; color:#2C3E50;">🏥 Health Insurance Cost Predictor</h1>
    <p style="text-align:center; color:gray; font-size:18px;">
        Enter your details to estimate your expected insurance cost 💡
    </p>
    <hr>
    """,
    unsafe_allow_html=True,
)

# Dropdown options
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease',
        'Diabetes & Thyroid', 'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# --- Inputs grouped in sections ---
st.markdown("### 👤 Personal Information")
col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input('Age', min_value=18, max_value=100, step=1)
with col2:
    gender = st.selectbox('Gender', categorical_options['Gender'])
with col3:
    marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])

st.markdown("### 💼 Lifestyle & Financial")
col4, col5, col6 = st.columns(3)
with col4:
    number_of_dependants = st.number_input('Number of Dependants', min_value=0, max_value=20, step=1)
with col5:
    income_lakhs = st.number_input('Income in Lakhs', min_value=0, max_value=200, step=1)
with col6:
    employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

st.markdown("### 🩺 Health Information")
col7, col8, col9 = st.columns(3)
with col7:
    bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])
with col8:
    smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
with col9:
    genetical_risk = st.number_input('Genetical Risk (0-5)', min_value=0, max_value=5, step=1)

st.markdown("### 🌍 Insurance & Region")
col10, col11, col12 = st.columns(3)
with col10:
    insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
with col11:
    region = st.selectbox('Region', categorical_options['Region'])
with col12:
    medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

# Collect input dictionary
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Predict button
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🔮 Predict Insurance Cost", use_container_width=True):
    prediction = predict(input_dict)

    st.markdown(
        f"""
        <div style="background-color:#ECF0F1; padding:20px; border-radius:15px; text-align:center; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <h2 style="color:#27AE60;">💰 Predicted Cost: {prediction}</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )
