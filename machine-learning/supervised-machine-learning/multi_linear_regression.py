import pandas as pd;
from sklearn.model_selection import train_test_split;
from sklearn.linear_model import LinearRegression;
import matplotlib.pyplot as plt;

data = {
    "square_foot": [
        650, 720, 800, 850, 900, 950, 1000, 1050, 1100, 1150,
        1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650,
        1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150,
        2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650,
        2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150,
        3200, 3250, 3300, 3350, 3400, 3450, 3500, 3550, 3600, 3650,
        3700, 3750, 3800, 3850, 3900, 3950, 4000, 4050, 4100, 4150,
        4200, 4250, 4300, 4350, 4400, 4450, 4500, 4550, 4600, 4650,
        4700, 4750, 4800, 4850, 4900, 4950, 5000, 5050, 5100, 5150,
        5200, 5250, 5300, 5350, 5400, 5450, 5500, 5550, 5600, 5650
    ],

    "bhk": [
        1, 1, 2, 2, 2, 2, 2, 2, 2, 2,
        2, 2, 2, 2, 2, 3, 3, 3, 3, 3,
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        3, 3, 3, 3, 4, 4, 4, 4, 4, 4,
        4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
        4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
        4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
        4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
        4, 4, 4, 4, 4, 4, 4, 4, 4, 4
    ],

    "house_age": [
        5, 10, 8, 15, 12, 7, 20, 10, 5, 18,
        12, 6, 25, 15, 9, 7, 10, 20, 5, 12,
        18, 8, 15, 10, 22, 7, 5, 12, 20, 9,
        15, 6, 18, 25, 10, 8, 14, 5, 20, 12,
        7, 15, 10, 22, 8, 5, 18, 12, 25, 10,
        6, 15, 20, 8, 12, 5, 18, 10, 7, 22,
        15, 9, 20, 12, 5, 18, 10, 7, 25, 15,
        8, 20, 12, 6, 18, 10, 5, 22, 15, 9,
        20, 12, 7, 18, 10, 5, 25, 15, 8, 20,
        12, 6, 18, 10, 5, 22, 15, 9, 20, 12
    ],

    "price_lakhs": [
        35, 40, 48, 52, 55, 60, 65, 68, 72, 75,
        78, 82, 85, 88, 92, 100, 105, 110, 115, 120,
        125, 130, 135, 140, 145, 150, 155, 160, 165, 170,
        175, 180, 185, 190, 195, 200, 205, 210, 215, 220,
        225, 230, 235, 240, 250, 255, 260, 265, 270, 275,
        280, 285, 290, 295, 300, 305, 310, 315, 320, 325,
        330, 335, 340, 345, 350, 355, 360, 365, 370, 375,
        380, 385, 390, 395, 400, 405, 410, 415, 420, 425,
        430, 435, 440, 445, 450, 455, 460, 465, 470, 475,
        480, 485, 490, 495, 500, 505, 510, 515, 520, 525
    ]
}

df = pd.DataFrame(data)
x = df[["square_foot", "bhk", "house_age"]]
y = df["price_lakhs"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10)
model = LinearRegression()
model.fit(x_train, y_train)
prediction = model.predict([[1800, 3, 5]])
print(f"Predicted price for 1800 sq ft, 3 BHK, 5 years old house: {prediction[0]:.2f} lakhs")

# Actual vs Predicted plot
y_pred = model.predict(x_test)
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices (lakhs)")
plt.ylabel("Predicted Prices (lakhs)")
plt.title("Actual vs Predicted Prices")
plt.show()

# Actual vs Predicted table
results = x_test.copy()

results["actual_price"] = y_test
results["predicted_price"] = y_pred

results["difference"] = (
    results["actual_price"] - results["predicted_price"]
)

results["error"] = abs(
    results["difference"]
)

print(results)