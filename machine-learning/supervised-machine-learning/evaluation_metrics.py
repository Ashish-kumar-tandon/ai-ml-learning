from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

y_true = [1, 1, 1, 1, 0, 0, 0, 0]
y_pred = [1, 1, 0, 0, 1, 0, 0, 0]

acc = accuracy_score(y_true, y_pred)
print(f"Accuracy: {acc:.2f}")

precision = precision_score(y_true, y_pred) # Precision = TP / (TP + FP)
print(f"Precision: {precision:.2f}")

recall = recall_score(y_true, y_pred) # Recall = TP / (TP + FN)
print(f"Recall: {recall:.2f}")

cm = confusion_matrix(y_true, y_pred) # Confusion Matrix: [[TN, FP], [FN, TP]]
print("\nConfusion Matrix:\n", cm)
