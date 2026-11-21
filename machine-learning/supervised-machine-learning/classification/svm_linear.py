
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC

data = {
    'study_hours': [1, 2, 3, 2, 4, 5, 6, 7, 8, 9, 3, 6, 8, 4, 9],
    'attendance': [30, 40, 50, 35, 55, 70, 80, 85, 90, 95, 45, 75, 95, 60, 98],
    'result': ['Fail', 'Fail', 'Fail', 'Fail', 'Fail', 'Pass', 'Pass', 'Pass', 'Pass', 'Pass', 'Fail', 'Pass', 'Pass', 'Pass', 'Pass']
}

df = pd.DataFrame(data)

X = df[['study_hours', 'attendance']]
y = df['result']

model = SVC(kernel='linear')

model.fit(X, y)

new_student = [[4, 60]]

prediction = model.predict(new_student)

print("Student Result:", prediction[0])

# Visualisation

plt.scatter(df['study_hours'], df['attendance'], c=y.map({'Pass': 0, 'Fail': 1}))
plt.scatter(new_student[0][0], new_student[0][1], color='green', marker='*', s=200)
plt.title("Linear SVM Classification")
plt.xlabel("Study Hours")
plt.ylabel("Attendance")
plt.show()
