from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score

# Age and Annual Income
X = [
    [25, 25000],
    [30, 40000],
    [35, 50000],
    [40, 60000],
    [28, 30000],
    [45, 70000],
    [50, 80000],
    [23, 20000],
    [32, 45000],
    [38, 55000]
]

# Loan Approved (1) or Rejected (0)
y = [0, 0, 1, 1, 0, 1, 1, 0, 1, 1]

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