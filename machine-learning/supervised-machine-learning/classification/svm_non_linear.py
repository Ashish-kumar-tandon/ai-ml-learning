
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.datasets import make_circles

X, y = make_circles(n_samples=300, noise=0.08, factor=0.4, random_state=42)

df = pd.DataFrame(X, columns=['study_hours', 'attendance'])

df['result'] = ['Pass' if i == 0 else 'Fail' for i in y]

X = df[['study_hours', 'attendance']]
y = df['result']

model = SVC(kernel='rbf')

model.fit(X, y)

new_student = [[0.2, 0.3]]

prediction = model.predict(new_student)

print("Student Result:", prediction[0])

# Visualisation

plt.scatter(df['study_hours'], df['attendance'], c=y.map({'Pass': 0, 'Fail': 1}))
plt.scatter(new_student[0][0], new_student[0][1], color='green', marker='*', s=200)
plt.title("Non-Linear SVM Dataset")
plt.xlabel("Study Hours")
plt.ylabel("Attendance")
plt.show()