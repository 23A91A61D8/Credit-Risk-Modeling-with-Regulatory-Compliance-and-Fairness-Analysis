# Credit Risk Modeling with Regulatory Compliance and Fairness Analysis

## 📌 Project Overview
This project implements an end-to-end credit risk modeling framework to predict the probability of loan default while ensuring regulatory compliance, fairness, and interpretability.  
The solution is designed for real-world financial decision-making and follows industry best practices in model risk management.

The project demonstrates the complete lifecycle of a regulated data science system, from exploratory analysis to deployment-ready dashboards.

---

## 🎯 Objectives
- Predict loan default risk with high accuracy
- Maintain interpretability and transparency of model decisions
- Ensure fairness across demographic groups
- Align with SR 11-7 Model Risk Management guidance
- Provide actionable insights for non-technical users (loan officers)

---

## 🧠 Models Used
- **Logistic Regression**  
  - Baseline model for interpretability and regulatory transparency
- **LightGBM**  
  - Advanced model for improved predictive performance

Model evaluation was performed using stratified cross-validation and AUC-ROC metrics.

---

## ⚖️ Fairness & Interpretability
- **Fairness Metrics**
  - Disparate Impact (approval rate parity)
  - Equal Opportunity (true positive rate parity)
- **Interpretability**
  - SHAP-style feature contribution analysis
  - Individual-level explanations for declined applications
- **Adverse Action Reason Codes**
  - High credit amount relative to profile
  - Long loan duration increasing repayment risk
  - Limited income or employment stability

---

## 📊 Interactive Dashboard
A Streamlit-based dashboard was developed for loan officers to:
- Input applicant details
- View risk score and decision (Approve / Review / Reject)
- Understand key risk drivers
- Receive clear decision recommendations

The dashboard prioritizes clarity, actionability, and non-technical usability.

---

## 📁 Project Structure
.
├── dashboard/
│ └── app.py # Streamlit underwriting dashboard
├── data/
│ ├── raw/ # Raw input data
│ └── processed/ # Processed datasets
├── notebooks/
│ ├── 01_eda.ipynb # Exploratory Data Analysis
│ ├── 02_feature_engineering.ipynb
│ ├── 03_modeling.ipynb
│ └── 04_fairness_analysis.ipynb
├── reports/
│ ├── regulatory_report.pdf
│ ├── executive_summary.pdf
│ └── fairness_report.pdf
├── src/
│ ├── preprocessing.py # Data preprocessing logic
│ ├── features.py # Feature engineering functions
│ ├── train.py # Model training pipeline
│ └── predict.py # Prediction / scoring functions
├── requirements.txt
└── README.md

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt

2️⃣ Run Notebooks

Open Jupyter Notebook and run notebooks in this order:

01_eda.ipynb

02_feature_engineering.ipynb

03_modeling.ipynb

04_fairness_analysis.ipynb

3️⃣ Run the Dashboard
cd dashboard
streamlit run app.py

The dashboard will open in your browser at:
http://localhost:8501

📄 Reports

Regulatory Compliance Report
Aligned with SR 11-7 Model Risk Management guidance

Executive Summary
Translates model performance into business outcomes

Fairness Analysis Report
Demonstrates compliance with fair lending principles

🚀 Key Highlights

End-to-end regulated ML workflow

Strong focus on fairness and transparency

Business-oriented dashboard for decision support

Audit-ready documentation

Modular, production-style code structure
