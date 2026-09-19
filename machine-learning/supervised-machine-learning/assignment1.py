from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score

# Study Hours and Attendance Percentage
X = [
   [2, 60],
   [3, 65],
   [4, 70],
   [5, 75],
   [6, 80],
   [7, 85],
   [8, 90],
   [9, 95],
   [1, 50],
   [3, 55]
]

# Pass (1) or Fail (0) Based on the study hours and attendance percentage  
y = [0, 0, 1, 1, 1, 1, 1, 1, 0, 0]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier(n_estimators=20, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Predicted labels:", y_pred)
print("Actual labels:", y_test)
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)

print("Confusion Matrix:\n", cm)
print("Accuracy:", acc)
print("Precision:", prec)

tn = cm[0][0]  
fp = cm[0][1]  
fn = cm[1][0]  
tp = cm[1][1]  

print("TN:", tn)
print("FP:", fp)
print("FN:", fn)
print("TP:", tp)