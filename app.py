
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Fraud Detection AI",
    page_icon="🛡️",
    layout="centered"
)

@st.cache_resource
def load_model():
    return joblib.load("fraud_detection_model.pkl")

model = load_model()

st.title("🛡️ Credit Card Fraud Detection")
st.write(
    "Enter transaction details to estimate whether "
    "the transaction may be fraudulent."
)

st.info(
    "This is an ML demonstration, not a real banking "
    "security system. Predictions may be incorrect."
)

with st.form("transaction_form"):
    amount = st.number_input(
        "Transaction amount", min_value=0.0, value=100.0
    )

    transaction_hour = st.slider(
        "Transaction hour", 0, 23, 12
    )

    merchant_category = st.text_input(
        "Merchant category",
        value="grocery",
        help="Use a category found in your training dataset."
    )

    foreign_transaction = st.selectbox(
        "Foreign transaction?",
        options=[0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    location_mismatch = st.selectbox(
        "Location mismatch?",
        options=[0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    device_trust_score = st.number_input(
        "Device trust score", value=50.0
    )

    velocity_last_24h = st.number_input(
        "Transactions in the last 24 hours",
        min_value=0,
        value=3
    )

    cardholder_age = st.number_input(
        "Cardholder age", min_value=18, max_value=120, value=30
    )

    submitted = st.form_submit_button("Analyze Transaction")

if submitted:
    transaction = pd.DataFrame([{
        "amount": amount,
        "transaction_hour": transaction_hour,
        "merchant_category": merchant_category,
        "foreign_transaction": foreign_transaction,
        "location_mismatch": location_mismatch,
        "device_trust_score": device_trust_score,
        "velocity_last_24h": velocity_last_24h,
        "cardholder_age": cardholder_age
    }])

    try:
        prediction = int(model.predict(transaction)[0])
        fraud_probability = float(
            model.predict_proba(transaction)[0, 1]
        )

        st.subheader("Analysis Result")
        st.metric(
            "Model-estimated fraud probability",
            f"{fraud_probability:.2%}"
        )

        if prediction == 1:
            st.error("The model flagged this transaction as potentially fraudulent.")
        else:
            st.success("The model classified this transaction as genuine.")

        st.caption(
            "This is a model prediction, not proof of fraud. "
            "Do not use it alone to approve or reject real transactions."
        )

    except Exception as error:
        st.error(
            "Could not process these inputs. Check that the input "
            "types and merchant category match the training data."
        )
        st.exception(error)
