import pandas as pd
import math
data = {
    "hours": [2, 5, 1, 4, 3, 6, 1, 2, 7, 0],
    "attendance": [85, 92, 65, 88, 75, 95, 58, 70, 90, 50],
    "result": ["Pass", "Pass", "Fail", "Pass", "Pass", "Pass", "Fail", "Pass", "Pass", "Fail"]
}
df = pd.DataFrame(data)
new_hours = 8
new_attendance = 70
distances = []
for i in range(len(df)):
    distance = math.sqrt((df['hours'][i] - new_hours) ** 2 + (df['attendance'][i] - new_attendance) ** 2)
    distances.append(distance)
df["distance"]= distances
a = df.sort_values("distance")
# print(a)
k = 3
nearest_neighbors = a.head(k)
# print(nearest_neighbors)
pass_count = (nearest_neighbors["result"] == "Pass").sum()
fail_count = (nearest_neighbors["result"] == "Fail").sum()

if pass_count > fail_count:
    print("The predicted result is: Pass")
else:
    print("The predicted result is: Fail")
