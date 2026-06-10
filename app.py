from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [float(request.form[f"f{i}"]) for i in range(13)]
        scaled = scaler.transform([features])
        result = model.predict(scaled)[0]
        message = "Heart Disease Detected" if result == 1 else "No Heart Disease"
        return render_template("index.html", prediction=message)
    except Exception as e:
        return render_template("index.html", prediction=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
