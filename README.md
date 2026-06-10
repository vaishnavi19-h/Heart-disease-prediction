❤️ Heart Disease Prediction
A machine learning web app that predicts heart disease risk using a Random Forest classifier, built with Flask.
🚀 Demo
Enter 13 clinical parameters → get instant prediction: Heart Disease Detected or No Heart Disease.
🛠️ Tech Stack

ML Model: Scikit-learn (RandomForestClassifier + StandardScaler)
Backend: Flask
Data: UCI Heart Disease dataset (heart.csv)

📁 Project Structure
├── heart.csv          # Dataset
├── train_model.py     # Train & save model
├── app.py             # Flask web app
├── requirements.txt   # Dependencies
└── templates/
    └── index.html     # UI
⚙️ Setup & Run
bash# Install dependencies
pip install -r requirements.txt

# Train the model (generates model.pkl & scaler.pkl)
python train_model.py

# Run the app
python app.py
Visit http://127.0.0.1:5000
📊 Input Features
The model takes 13 features: age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal

📦 Requirements
flask
scikit-learn
pandas
joblib
markupsafe==2.0.1
werkzeug==2.0.3
