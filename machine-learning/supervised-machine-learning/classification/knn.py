import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
data = {
    "hours": [2, 5, 1, 4, 3, 6, 1, 2, 7, 0],
    "attendance": [85, 92, 65, 88, 75, 95, 58, 70, 90, 50],
    "result": ["Pass", "Pass", "Fail", "Pass", "Pass", "Pass", "Fail", "Pass", "Pass", "Fail"]
}
df = pd.DataFrame(data)
new_hours = 8
new_attendance = 70
model = KNeighborsClassifier(n_neighbors=3)
model.fit(df[["hours", "attendance"]], df["result"])
prediction = model.predict([[new_hours, new_attendance]])
print(f"The predicted result is: {prediction[0]}")