import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Credit Risk Dashboard", layout="centered")

st.title("💳 Credit Risk Assessment Dashboard")
st.caption("Decision-support tool for Loan Officers")

st.divider()

# ===============================
# Applicant Inputs
# ===============================
st.header("👤 Applicant Information")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age (years)", 18, 70, 45)
    employment_years = st.slider("Years of Employment", 0, 40, 7)

with col2:
    credit_amount = st.number_input("Credit Amount (₹)", 500, 20000, 5000)
    duration = st.slider("Loan Duration (Months)", 6, 60, 28)

st.divider()

# ===============================
# Risk Score Calculation
# ===============================
risk_score = (credit_amount / duration) / age
risk_score = round(risk_score, 2)

st.header("📊 Risk Assessment")
st.metric("Estimated Risk Score", risk_score)

# ===============================
# Risk Level Decision
# ===============================
if risk_score >= 10:
    decision = "REJECT"
    risk_level = "High Risk"
    st.error("❌ High Risk – Loan Not Recommended")
elif risk_score >= 6:
    decision = "REVIEW"
    risk_level = "Medium Risk"
    st.warning("⚠️ Medium Risk – Manual Review Required")
else:
    decision = "APPROVE"
    risk_level = "Low Risk"
    st.success("✅ Low Risk – Loan Can Be Approved")

st.divider()

# ===============================
# Risk Score Visualization
# ===============================
st.subheader("📈 Risk Score Visualization")

fig, ax = plt.subplots()

ax.barh(["Risk Score"], [risk_score], color="green" if risk_score < 6 else "orange" if risk_score < 10 else "red")
ax.axvline(6, color="orange", linestyle="--", label="Review Threshold")
ax.axvline(10, color="red", linestyle="--", label="Reject Threshold")
ax.set_xlim(0, 15)
ax.set_xlabel("Risk Level")
ax.legend()

st.pyplot(fig)

st.divider()

# ===============================
# Explainability (Simple Contributions)
# ===============================
st.header("🔍 Key Risk Drivers")

contributions = {
    "Credit Amount": credit_amount / 1000,
    "Loan Duration": duration / 10,
    "Age Factor": 70 - age,
    "Employment Stability": 10 - employment_years
}

contrib_df = pd.DataFrame({
    "Factor": contributions.keys(),
    "Impact Score": contributions.values()
}).sort_values(by="Impact Score", ascending=True)

fig2, ax2 = plt.subplots()
ax2.barh(contrib_df["Factor"], contrib_df["Impact Score"])
ax2.set_title("Factors Influencing Risk Decision")

st.pyplot(fig2)

st.divider()

# ===============================
# Officer Recommendation
# ===============================
st.header("💼 Officer Recommendation")

if decision == "REJECT":
    st.write("📌 Recommend rejection or request collateral / guarantor.")
elif decision == "REVIEW":
    st.write("📌 Recommend additional document and income verification.")
else:
    st.write("📌 Recommend approval with standard interest rate.")

st.divider()

# ===============================
# Application Summary
# ===============================
summary = pd.DataFrame({
    "Attribute": ["Age", "Credit Amount", "Duration", "Employment Years", "Risk Level", "Decision"],
    "Value": [age, credit_amount, duration, employment_years, risk_level, decision]
})

st.subheader("📄 Application Summary")
st.table(summary)
