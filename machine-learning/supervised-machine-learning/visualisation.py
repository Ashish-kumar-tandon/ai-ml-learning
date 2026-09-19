import pandas as pd
import matplotlib.pyplot as plt
data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "marks": [35, 40, 45, 50, 55, 62, 68, 72, 78, 85]
}
df = pd.DataFrame(data)
plt.scatter(df["hours"], df["marks"])
plt.title("Plot of Hours vs Marks")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.show()