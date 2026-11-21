import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = {
    "salary": [8, 5, 12, 3, 10, 4, 15, 6],
    "credit_score": [750, 650, 800, 580, 720, 600, 780, 680],
    "age": [30, 25, 40, 22, 35, 28, 45, 32],
    "loan_approved": ["Yes", "No", "Yes", "No", "Yes", "No", "Yes", "Yes"]
}

df = pd.DataFrame(data)

X = df[["salary", "credit_score", "age"]]
y = df["loan_approved"]

model = RandomForestClassifier(n_estimators=20, random_state=42)

model.fit(X, y)

new_customer = pd.DataFrame({
    "salary": [7],
    "credit_score": [710],
    "age": [29]
})

prediction = model.predict(new_customer)

print("Loan Prediction:", prediction[0])
