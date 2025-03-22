import streamlit as st
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

# Load the trained model
@st.cache_data
def load_model():
    return pickle.load(open("Credit_card_project.pkl", "rb"))

model = load_model()

# Streamlit UI
st.title("💳 Credit Card Customer Classification")
st.markdown("### Predict whether a customer is **Good** or **Bad** based on their credit details.")

# User Input Form
with st.form("customer_form"):
    st.subheader("📌 Enter Customer Details:")
    
    NCL = st.number_input("🔢 Number of Open Credit Lines & Loans", min_value=0.0, step=0.1)
    NRL = st.number_input("🏡 Number of Real Estate Loans or Lines", min_value=0.0, step=0.1)
    MI = st.number_input("💰 Monthly Income (log-transformed)", min_value=0.0, step=0.1)
    ND = st.number_input("👨‍👩‍👧 Number of Dependents", min_value=0.0, step=1.0)
    
    st.subheader("🌍 Regional Information:")
    RC = st.checkbox("Region: Central")
    RE = st.checkbox("Region: East")
    RN = st.checkbox("Region: North")
    RW = st.checkbox("Region: West")
    
    st.subheader("🎓 Education Level (1-5)")
    Edu = st.slider("📚 Education Level", 1, 5)

    submit_button = st.form_submit_button("🔍 Predict")

# Prediction Logic
if submit_button:
    input_data = [[NCL, NRL, MI, ND, float(RC), float(RE), float(RN), float(RW), Edu]]
    
    # Model Prediction
    prediction = model.predict(input_data)[0]

    # Display Result
    st.subheader("📊 Prediction Result:")

    if prediction == 1:
        st.success("✅ Good Customer")
    else:
        st.error("❌ Bad Customer")
