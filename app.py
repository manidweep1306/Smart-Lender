from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model, scaler and label encoders
model = joblib.load("smart_lender_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoders = joblib.load("label_encoders.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    gender = label_encoders["Gender"].transform([request.form["Gender"]])[0]
    married = label_encoders["Married"].transform([request.form["Married"]])[0]
    dependents = label_encoders["Dependents"].transform([request.form["Dependents"]])[0]
    education = label_encoders["Education"].transform([request.form["Education"]])[0]
    self_employed = label_encoders["Self_Employed"].transform([request.form["Self_Employed"]])[0]
    property_area = label_encoders["Property_Area"].transform([request.form["Property_Area"]])[0]

    applicant_income = float(request.form["ApplicantIncome"])
    coapplicant_income = float(request.form["CoapplicantIncome"])
    loan_amount = float(request.form["LoanAmount"])
    loan_term = float(request.form["Loan_Amount_Term"])
    credit_history = float(request.form["Credit_History"])

    features = np.array([[
        gender,
        married,
        dependents,
        education,
        self_employed,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        credit_history,
        property_area
    ]])

    # Scale the features
    features = scaler.transform(features)

    # Predict
    prediction = model.predict(features)

    # Prediction probabilities
    probability = model.predict_proba(features)

    approved_probability = probability[0][1] * 100
    rejected_probability = probability[0][0] * 100

    if prediction[0] == 1:
        result = "✅ Loan Approved"
        confidence = approved_probability
    else:
        result = "❌ Loan Rejected"
        confidence = rejected_probability

    return render_template(
        "index.html",
        prediction=result,
        confidence=round(confidence, 2)
    )


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)