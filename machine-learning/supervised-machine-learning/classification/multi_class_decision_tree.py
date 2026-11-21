import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = {
    "weight": [5, 6, 7, 20, 22, 25, 3, 4, 5, 8, 9, 10, 30, 35, 40, 2, 3, 4],
    "height": [25, 28, 30, 70, 75, 80, 20, 22, 25, 35, 38, 40, 90, 100, 110, 15, 18, 20],
    "speed": [30, 32, 35, 45, 48, 50, 35, 38, 40, 20, 22, 25, 60, 65, 70, 10, 12, 15],
    "animal": [
        "Cat", "Cat", "Cat",
        "Dog", "Dog", "Dog",
        "Rabbit", "Rabbit", "Rabbit",
        "Goat", "Goat", "Goat",
        "Horse", "Horse", "Horse",
        "Mouse", "Mouse", "Mouse"
    ]
}

df = pd.DataFrame(data)

model = DecisionTreeClassifier()

model.fit(
    df[["weight", "height", "speed"]],
    df["animal"]
)

prediction = model.predict([[7, 30, 34]])

print(f"The predicted animal is: {prediction[0]}")
