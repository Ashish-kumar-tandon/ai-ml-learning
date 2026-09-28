#Student Performance Prediction System
import pandas as pd

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


data = pd.read_csv("students.csv")
df = pd.DataFrame(data)

TRAINING_SIZE = 20

features = [
    "attendance",
    "study_hours",
    "internal_marks",
    "assignment_score",
    "previous_marks"
]


def calculate_risk(student):

    risk_score = 0

    if student["attendance"] > 75:
        risk_score += 1
    elif student["attendance"] >= 60:
        risk_score += 2
    else:
        risk_score += 3

    if student["study_hours"] > 3:
        risk_score += 1
    elif student["study_hours"] >= 2:
        risk_score += 2
    else:
        risk_score += 3

    if student["internal_marks"] > 35:
        risk_score += 1
    elif student["internal_marks"] >= 25:
        risk_score += 2
    else:
        risk_score += 3

    if student["assignment_score"] > 10:
        risk_score += 1
    elif student["assignment_score"] >= 7:
        risk_score += 2
    else:
        risk_score += 3

    if risk_score <= 6:
        risk_level = "LOW RISK"
    elif risk_score <= 9:
        risk_level = "MEDIUM RISK"
    else:
        risk_level = "HIGH RISK"

    return risk_score, risk_level


def train_models():

    training_data = df.head(TRAINING_SIZE)

    X = training_data[features]

    y_final_marks = training_data["final_marks"]
    y_result = training_data["result"]

    linear_model = LinearRegression()
    linear_model.fit(X, y_final_marks)

    logistic_model = LogisticRegression()
    logistic_model.fit(X, y_result)

    knn_model = KNeighborsClassifier(n_neighbors=3)
    knn_model.fit(X, y_result)

    decision_tree_model = DecisionTreeClassifier()
    decision_tree_model.fit(X, y_result)

    random_forest_model = RandomForestClassifier(
        n_estimators=20,
        random_state=42
    )
    random_forest_model.fit(X, y_result)

    return (
        linear_model,
        logistic_model,
        knn_model,
        decision_tree_model,
        random_forest_model
    )


def add_student():

    global df

    name = input("Enter student name: ")

    while True:
        try:
            age = int(input("Enter age: "))

            if age >= 0:
                break

            print("Invalid age. Please enter a valid age.")

        except ValueError:
            print("Please enter a valid integer for age.")

    while True:
        try:
            attendance = int(
                input("Enter attendance percentage (0-100): ")
            )

            if 0 <= attendance <= 100:
                break

            print(
                "Invalid attendance. "
                "Please enter a value between 0 and 100."
            )

        except ValueError:
            print("Please enter a valid integer for attendance.")

    while True:
        try:
            study_hours = int(
                input("Enter daily study hours (0-24): ")
            )

            if 0 <= study_hours <= 24:
                break

            print(
                "Invalid study hours. "
                "Please enter a value between 0 and 24."
            )

        except ValueError:
            print("Please enter a valid integer for study hours.")

    while True:
        try:
            internal_marks = int(
                input("Enter internal marks (0-50): ")
            )

            if 0 <= internal_marks <= 50:
                break

            print(
                "Invalid internal marks. "
                "Please enter a value between 0 and 50."
            )

        except ValueError:
            print("Please enter a valid integer for internal marks.")

    while True:
        try:
            assignment_score = int(
                input("Enter assignment score (0-15): ")
            )

            if 0 <= assignment_score <= 15:
                break

            print(
                "Invalid assignment score. "
                "Please enter a value between 0 and 15."
            )

        except ValueError:
            print("Please enter a valid integer for assignment score.")

    while True:
        try:
            previous_marks = int(
                input("Enter previous examination marks (0-100): ")
            )

            if 0 <= previous_marks <= 100:
                break

            print(
                "Invalid previous marks. "
                "Please enter a value between 0 and 100."
            )

        except ValueError:
            print("Please enter a valid integer for previous marks.")

    while True:
        try:
            assignments_completed = int(
                input("Enter assignments completed (0-5): ")
            )

            if 0 <= assignments_completed <= 5:
                break

            print(
                "Invalid assignments completed. "
                "Please enter a value between 0 and 5."
            )

        except ValueError:
            print(
                "Please enter a valid integer "
                "for assignments completed."
            )

    new_student = {
        "name": name,
        "age": age,
        "attendance": attendance,
        "study_hours": study_hours,
        "internal_marks": internal_marks,
        "assignment_score": assignment_score,
        "previous_marks": previous_marks,
        "assignments_completed": assignments_completed,
    }

    new_student_df = pd.DataFrame([new_student])

    df = pd.concat(
        [df, new_student_df],
        ignore_index=True
    )

    df.to_csv("students.csv", index=False)

    print("\nStudent added successfully!")


def view_students():

    global df

    results = df.copy()
    results = results.drop(
        columns=["final_marks", "result"]
    )

    risk_scores = []
    risk_levels = []

    for i in range(len(results)):

        student = results.iloc[i]

        score, level = calculate_risk(student)

        risk_scores.append(score)
        risk_levels.append(level)

    results["risk_score"] = risk_scores
    results["risk_level"] = risk_levels

    X = results[features]

    results["predicted_final_marks"] = (
        linear_model.predict(X).round(2)
    )

    results["logistic_result"] = (
        logistic_model.predict(X)
    )

    results["knn_result"] = (
        knn_model.predict(X)
    )

    results["decision_tree_result"] = (
        decision_tree_model.predict(X)
    )

    results["random_forest_result"] = (
        random_forest_model.predict(X)
    )

    print("\n" + "=" * 160)
    print("                                                   STUDENT PERFORMANCE")
    print("=" * 160)

    print(results.to_string(index=False))


def analyze_student_risk():

    if len(df) == 0:
        print("No students available.")
        return

    print("\nStudents:")

    for i in range(len(df)):
        print(i + 1, "-", df.iloc[i]["name"])

    while True:
        try:
            choice = int(
                input("Enter student number: ")
            )

            if 1 <= choice <= len(df):
                break

            print("Invalid student number.")

        except ValueError:
            print("Please enter a valid integer.")

    student = df.iloc[choice - 1]

    score, level = calculate_risk(student)

    print("\nStudent:", student["name"])
    print("Risk Score:", score)
    print("Risk Level:", level)


def predict_final_marks():

    name = input("Enter student name: ")

    while True:
        try:
            attendance = int(
                input("Enter attendance percentage (0-100): ")
            )

            if 0 <= attendance <= 100:
                break

            print(
                "Invalid attendance. "
                "Please enter a value between 0 and 100."
            )

        except ValueError:
            print("Please enter a valid integer for attendance.")

    while True:
        try:
            study_hours = int(
                input("Enter daily study hours (0-24): ")
            )

            if 0 <= study_hours <= 24:
                break

            print(
                "Invalid study hours. "
                "Please enter a value between 0 and 24."
            )

        except ValueError:
            print("Please enter a valid integer for study hours.")

    while True:
        try:
            internal_marks = int(
                input("Enter internal marks (0-50): ")
            )

            if 0 <= internal_marks <= 50:
                break

            print(
                "Invalid internal marks. "
                "Please enter a value between 0 and 50."
            )

        except ValueError:
            print("Please enter a valid integer for internal marks.")

    while True:
        try:
            assignment_score = int(
                input("Enter assignment score (0-15): ")
            )

            if 0 <= assignment_score <= 15:
                break

            print(
                "Invalid assignment score. "
                "Please enter a value between 0 and 15."
            )

        except ValueError:
            print("Please enter a valid integer for assignment score.")

    while True:
        try:
            previous_marks = int(
                input("Enter previous examination marks (0-100): ")
            )

            if 0 <= previous_marks <= 100:
                break

            print(
                "Invalid previous marks. "
                "Please enter a value between 0 and 100."
            )

        except ValueError:
            print("Please enter a valid integer for previous marks.")

    new_student = pd.DataFrame([{
        "attendance": attendance,
        "study_hours": study_hours,
        "internal_marks": internal_marks,
        "assignment_score": assignment_score,
        "previous_marks": previous_marks
    }])

    prediction = linear_model.predict(new_student)

    print("\nStudent:", name)
    print(
        "Predicted Final Marks:",
        round(prediction[0], 2)
    )


def predict_pass_fail():

    name = input("Enter student name: ")

    while True:
        try:
            attendance = int(
                input("Enter attendance percentage (0-100): ")
            )

            if 0 <= attendance <= 100:
                break

            print(
                "Invalid attendance. "
                "Please enter a value between 0 and 100."
            )

        except ValueError:
            print("Please enter a valid integer for attendance.")

    while True:
        try:
            study_hours = int(
                input("Enter daily study hours (0-24): ")
            )

            if 0 <= study_hours <= 24:
                break

            print(
                "Invalid study hours. "
                "Please enter a value between 0 and 24."
            )

        except ValueError:
            print("Please enter a valid integer for study hours.")

    while True:
        try:
            internal_marks = int(
                input("Enter internal marks (0-50): ")
            )

            if 0 <= internal_marks <= 50:
                break

            print(
                "Invalid internal marks. "
                "Please enter a value between 0 and 50."
            )

        except ValueError:
            print("Please enter a valid integer for internal marks.")

    while True:
        try:
            assignment_score = int(
                input("Enter assignment score (0-15): ")
            )

            if 0 <= assignment_score <= 15:
                break

            print(
                "Invalid assignment score. "
                "Please enter a value between 0 and 15."
            )

        except ValueError:
            print("Please enter a valid integer for assignment score.")

    while True:
        try:
            previous_marks = int(
                input("Enter previous examination marks (0-100): ")
            )

            if 0 <= previous_marks <= 100:
                break

            print(
                "Invalid previous marks. "
                "Please enter a value between 0 and 100."
            )

        except ValueError:
            print("Please enter a valid integer for previous marks.")

    new_student = pd.DataFrame([{
        "attendance": attendance,
        "study_hours": study_hours,
        "internal_marks": internal_marks,
        "assignment_score": assignment_score,
        "previous_marks": previous_marks
    }])

    logistic_result = logistic_model.predict(
        new_student
    )[0]

    knn_result = knn_model.predict(
        new_student
    )[0]

    decision_tree_result = decision_tree_model.predict(
        new_student
    )[0]

    random_forest_result = random_forest_model.predict(
        new_student
    )[0]

    print("\nStudent:", name)

    print(
        "Logistic Regression:",
        logistic_result
    )

    print(
        "KNN:",
        knn_result
    )

    print(
        "Decision Tree:",
        decision_tree_result
    )

    print(
        "Random Forest:",
        random_forest_result
    )


def compare_models():

    training_data = df.head(TRAINING_SIZE)

    X_regression = training_data[features]
    y_regression = training_data["final_marks"]

    X_reg_train, X_reg_test, y_reg_train, y_reg_test = train_test_split(
        X_regression,
        y_regression,
        test_size=0.2,
        random_state=42
    )

    linear_comparison_model = LinearRegression()

    linear_comparison_model.fit(
        X_reg_train,
        y_reg_train
    )

    linear_prediction = linear_comparison_model.predict(
        X_reg_test
    )

    mae = mean_absolute_error(
        y_reg_test,
        linear_prediction
    )

    mse = mean_squared_error(
        y_reg_test,
        linear_prediction
    )

    rmse = mean_squared_error(
        y_reg_test,
        linear_prediction
    ) ** 0.5

    r2 = r2_score(
        y_reg_test,
        linear_prediction
    )

    X_classification = training_data[features]
    y_classification = training_data["result"]

    X_cls_train, X_cls_test, y_cls_train, y_cls_test = train_test_split(
        X_classification,
        y_classification,
        test_size=0.2,
        random_state=42,
    )

    logistic_comparison_model = LogisticRegression()
    logistic_comparison_model.fit(
        X_cls_train,
        y_cls_train
    )

    knn_comparison_model = KNeighborsClassifier(n_neighbors=3)
    knn_comparison_model.fit(
        X_cls_train,
        y_cls_train
    )

    decision_tree_comparison_model = DecisionTreeClassifier(
        random_state=42
    )
    decision_tree_comparison_model.fit(
        X_cls_train,
        y_cls_train
    )

    random_forest_comparison_model = RandomForestClassifier(
        n_estimators=20,
        random_state=42
    )
    random_forest_comparison_model.fit(
        X_cls_train,
        y_cls_train
    )

    logistic_prediction = logistic_comparison_model.predict(
        X_cls_test
    )

    knn_prediction = knn_comparison_model.predict(
        X_cls_test
    )

    decision_tree_prediction = decision_tree_comparison_model.predict(
        X_cls_test
    )

    random_forest_prediction = random_forest_comparison_model.predict(
        X_cls_test
    )

    logistic_accuracy = accuracy_score(
        y_cls_test,
        logistic_prediction
    )

    logistic_precision = precision_score(
        y_cls_test,
        logistic_prediction,
        pos_label="Pass",
    )

    logistic_recall = recall_score(
        y_cls_test,
        logistic_prediction,
        pos_label="Pass",
    )

    logistic_f1 = f1_score(
        y_cls_test,
        logistic_prediction,
        pos_label="Pass",
    )

    logistic_matrix = confusion_matrix(
        y_cls_test,
        logistic_prediction,
        labels=["Pass", "Fail"]
    )

    knn_accuracy = accuracy_score(
        y_cls_test,
        knn_prediction
    )

    knn_precision = precision_score(
        y_cls_test,
        knn_prediction,
        pos_label="Pass",
    )

    knn_recall = recall_score(
        y_cls_test,
        knn_prediction,
        pos_label="Pass",
    )

    knn_f1 = f1_score(
        y_cls_test,
        knn_prediction,
        pos_label="Pass",
    )

    knn_matrix = confusion_matrix(
        y_cls_test,
        knn_prediction,
        labels=["Pass", "Fail"]
    )

    decision_tree_accuracy = accuracy_score(
        y_cls_test,
        decision_tree_prediction
    )

    decision_tree_precision = precision_score(
        y_cls_test,
        decision_tree_prediction,
        pos_label="Pass",
    )

    decision_tree_recall = recall_score(
        y_cls_test,
        decision_tree_prediction,
        pos_label="Pass",
    )

    decision_tree_f1 = f1_score(
        y_cls_test,
        decision_tree_prediction,
        pos_label="Pass",
    )

    decision_tree_matrix = confusion_matrix(
        y_cls_test,
        decision_tree_prediction,
        labels=["Pass", "Fail"]
    )

    random_forest_accuracy = accuracy_score(
        y_cls_test,
        random_forest_prediction
    )

    random_forest_precision = precision_score(
        y_cls_test,
        random_forest_prediction,
        pos_label="Pass",
    )

    random_forest_recall = recall_score(
        y_cls_test,
        random_forest_prediction,
        pos_label="Pass",
    )

    random_forest_f1 = f1_score(
        y_cls_test,
        random_forest_prediction,
        pos_label="Pass",
    )

    random_forest_matrix = confusion_matrix(
        y_cls_test,
        random_forest_prediction,
        labels=["Pass", "Fail"]
    )

    print("\n" + "=" * 80)
    print("                    MODEL COMPARISON")
    print("=" * 80)

    print("\nLINEAR REGRESSION")
    print("-" * 30)
    print("MAE :", round(mae, 2))
    print("MSE :", round(mse, 2))
    print("RMSE:", round(rmse, 2))
    print("R²  :", round(r2, 2))

    print("\nLOGISTIC REGRESSION")
    print("-" * 30)
    print("Accuracy :", round(logistic_accuracy, 2))
    print("Precision:", round(logistic_precision, 2))
    print("Recall   :", round(logistic_recall, 2))
    print("F1 Score :", round(logistic_f1, 2))
    print("Confusion Matrix [[TP FN], [FP TN]]:")
    print(logistic_matrix)

    print("\nKNN")
    print("-" * 30)
    print("Accuracy :", round(knn_accuracy, 2))
    print("Precision:", round(knn_precision, 2))
    print("Recall   :", round(knn_recall, 2))
    print("F1 Score :", round(knn_f1, 2))
    print("Confusion Matrix [[TP FN], [FP TN]]:")
    print(knn_matrix)

    print("\nDECISION TREE")
    print("-" * 30)
    print("Accuracy :", round(decision_tree_accuracy, 2))
    print("Precision:", round(decision_tree_precision, 2))
    print("Recall   :", round(decision_tree_recall, 2))
    print("F1 Score :", round(decision_tree_f1, 2))
    print("Confusion Matrix [[TP FN], [FP TN]]:")
    print(decision_tree_matrix)

    print("\nRANDOM FOREST")
    print("-" * 30)
    print("Accuracy :", round(random_forest_accuracy, 2))
    print("Precision:", round(random_forest_precision, 2))
    print("Recall   :", round(random_forest_recall, 2))
    print("F1 Score :", round(random_forest_f1, 2))
    print("Confusion Matrix [[TP FN], [FP TN]]:")
    print(random_forest_matrix)


(
    linear_model,
    logistic_model,
    knn_model,
    decision_tree_model,
    random_forest_model
) = train_models()


while True:

    print("\n========================================")
    print("   STUDENT PERFORMANCE PREDICTION SYSTEM")
    print("========================================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Analyze Student Risk")
    print("4. Predict Final Marks")
    print("5. Predict Pass/Fail")
    print("6. Compare Models")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_student()

    elif choice == "2":

        view_students()

    elif choice == "3":

        analyze_student_risk()

    elif choice == "4":

        predict_final_marks()

    elif choice == "5":

        predict_pass_fail()

    elif choice == "6":

        compare_models()

    elif choice == "7":

        print("Thank you!")
        break

    else:

        print("Invalid choice")
