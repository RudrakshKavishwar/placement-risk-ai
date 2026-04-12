# 🎓 AI-Powered Placement Risk Modeling System

An AI-driven system that predicts student placement outcomes, estimates salary, and identifies employability risks to support education loan decisions.

🔗 **Live Project Repo:**  
https://github.com/RudrakshKavishwar/placement-risk-ai

🔗 **App Link:** 

https://rudrakshkavishwar-placement-risk-ai-app-fmex4b.streamlit.app/
---

## 🚀 Problem Statement

Design an intelligent system that can:

- Predict placement within **3 / 6 / 12 months**
- Estimate **expected starting salary**
- Identify students at **risk of delayed placement**

This helps lenders proactively manage risk and provide targeted student support.

---

## 🧠 Key Features

- 📊 Multi-time placement prediction (3m, 6m, 12m)
- 💰 Salary estimation using regression
- ⚠️ Risk classification (Low / Medium / High)
- 🧠 Explainable AI insights
- 📌 Personalized recommendations
- 🌐 Interactive UI built with Streamlit

---

## 🏗️ Tech Stack

| Category | Technology |
|--------|----------|
| Language | Python |
| ML | Scikit-learn |
| Data | Pandas, NumPy |
| UI | Streamlit |
| Models | Random Forest |

---

## 📁 Project Structure
placement-risk-ai/
│
├── data/
│ └── placement_dataset.csv
│
├── models/
│ ├── model_3m.pkl
│ ├── model_6m.pkl
│ ├── model_12m.pkl
│ └── salary_model.pkl
│
├── train.py
├── predict.py
├── utils.py
├── app.py
├── requirements.txt
