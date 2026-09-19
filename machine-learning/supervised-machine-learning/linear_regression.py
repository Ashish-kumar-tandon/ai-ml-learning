import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "marks": [35, 40, 45, 50, 55, 62, 68, 72, 78, 85]
}
df = pd.DataFrame(data)
x = df[["hours"]]
y = df["marks"]
x_learn, x_test, y_learn, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_learn, y_learn)
print(model.predict([[13]]))