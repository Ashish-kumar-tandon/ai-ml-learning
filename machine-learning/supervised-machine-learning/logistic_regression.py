import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "result": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}
df = pd.DataFrame(data)
model = LogisticRegression()
model.fit(df[["hours"]], df["result"])
print(model.predict([[12]]))