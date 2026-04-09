import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

# Load dataset
df = pd.read_csv("data/placement_dataset.csv")

# Features
X = df[['cgpa','internships','skills_score','institute_tier','placement_rate','job_demand']]

# Targets
y_3m = df['placed_3m']
y_6m = df['placed_6m']
y_12m = df['placed_12m']
y_salary = df['salary']

# Split
X_train, X_test, y3_train, y3_test = train_test_split(X, y_3m, test_size=0.2)

# Models
model_3m = RandomForestClassifier()
model_6m = RandomForestClassifier()
model_12m = RandomForestClassifier()
salary_model = RandomForestRegressor()

# Train
model_3m.fit(X_train, y3_train)
model_6m.fit(X_train, y_6m.loc[y3_train.index])
model_12m.fit(X_train, y_12m.loc[y3_train.index])
salary_model.fit(X_train, y_salary.loc[y3_train.index])

# Save models
pickle.dump(model_3m, open("models/model_3m.pkl", "wb"))
pickle.dump(model_6m, open("models/model_6m.pkl", "wb"))
pickle.dump(model_12m, open("models/model_12m.pkl", "wb"))
pickle.dump(salary_model, open("models/salary_model.pkl", "wb"))

print("✅ All models trained and saved!")