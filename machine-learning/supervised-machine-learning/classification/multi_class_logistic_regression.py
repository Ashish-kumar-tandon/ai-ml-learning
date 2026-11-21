import pandas as pd
from sklearn.linear_model import LogisticRegression
data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "attendance": [50, 55, 60, 65, 70, 75, 80, 85, 90],
    "result": [
        "Poor",
        "Poor",
        "Poor",
        "Average",
        "Average",
        "Average",
        "Excellent",
        "Excellent",
        "Excellent"
    ]
}
df = pd.DataFrame(data)
model = LogisticRegression()
model.fit(df[["hours", "attendance"]], df["result"])
prediction = model.predict([[5, 70]])
print(f"The predicted result is: {prediction[0]}")
