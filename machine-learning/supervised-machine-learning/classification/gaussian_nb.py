# Gaussian Naive Bayes Classifier
from sklearn.naive_bayes import GaussianNB
# Features = [free, offer]
x = [[1, 1], [1, 0], [0, 1], [0, 0]]
# Target = 1 - Spam, 0 - Not Spam
y = [1, 1, 1, 0]
# Create a Gaussian Naive Bayes Classifier
model = GaussianNB()
model.fit(x, y)
# Predict the class of a new email with features [1, 0]
prediction = model.predict([[0, 0]])
print("Predicted class for the email with features [0, 0]:", prediction[0])