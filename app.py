import streamlit as st
from predict import predict
from utils import generate_summary, recommendations

st.set_page_config(page_title="Placement Risk AI", layout="centered")

st.title("🎓 Placement Risk Predictor (AI System)")

st.write("Predict placement chances, salary, and risk level")

# Inputs
cgpa = st.slider("CGPA", 5.0, 10.0, 7.0)
internships = st.number_input("Internships", 0, 5, 1)
skills = st.slider("Skills Score", 1, 10, 5)
tier = st.selectbox("Institute Tier", [1, 2, 3])
placement_rate = st.slider("Institute Placement Rate", 0.0, 1.0, 0.7)
job_demand = st.slider("Job Market Demand", 0.0, 1.0, 0.6)

if st.button("🚀 Predict"):
    data = [cgpa, internships, skills, tier, placement_rate, job_demand]

    p3, p6, p12, salary, risk = predict(data)

    st.subheader("📊 Prediction Results")

    st.write(f"Placement in 3 months: {p3:.2f}")
    st.write(f"Placement in 6 months: {p6:.2f}")
    st.write(f"Placement in 12 months: {p12:.2f}")

    st.write(f"💰 Expected Salary: ₹{int(salary)}")
    st.write(f"⚠️ Risk Level: {risk}")

    st.subheader("🧠 AI Explanation")
    st.write(generate_summary(data, risk))

    st.subheader("📌 Recommendations")
    for rec in recommendations(data):
        st.write("✔", rec)