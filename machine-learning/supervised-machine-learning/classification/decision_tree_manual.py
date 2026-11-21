# Manual Decision Tree Implementation for Loan Approval Prediction
new_customer = {
    "salary": 70000,
    "credit_score": 710,
    "age": 29
}

def manual_decision_tree_all(customer):
    if customer["credit_score"] >= 670:
        if customer["salary"] >= 50000:
            if customer["age"] >= 24 and customer["age"] <= 50:
                return "Yes"
            else:
                return "No"
        else:
            return "No"
    else:
        return "No"

prediction = manual_decision_tree_all(new_customer)
print("Loan Prediction (Using All Features):", prediction)