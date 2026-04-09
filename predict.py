import pickle
import numpy as np

# Load models
model_3m = pickle.load(open("models/model_3m.pkl", "rb"))
model_6m = pickle.load(open("models/model_6m.pkl", "rb"))
model_12m = pickle.load(open("models/model_12m.pkl", "rb"))
salary_model = pickle.load(open("models/salary_model.pkl", "rb"))

def predict(data):
    data = np.array(data).reshape(1, -1)

    p3 = model_3m.predict_proba(data)[0][1]
    p6 = model_6m.predict_proba(data)[0][1]
    p12 = model_12m.predict_proba(data)[0][1]

    salary = salary_model.predict(data)[0]

    # Risk logic
    if p3 > 0.7:
        risk = "Low"
    elif p6 > 0.5:
        risk = "Medium"
    else:
        risk = "High"

    return p3, p6, p12, salary, risk