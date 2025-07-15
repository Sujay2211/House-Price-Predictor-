# 🏠 House Price Prediction App

This is an **end-to-end machine learning web app** that predicts house prices based on input features. Built with **Flask**, styled using **Bootstrap**, and deployable on **Render**, this project includes everything from model training to a working web UI and API.

---

## 🚀 Features

- Trains a regression model using Random Forest
- Web form to enter house details and predict the price
- Styled with responsive Bootstrap dark theme
- API endpoint for integration (`/predict`)
- Deploy-ready on Render or Hugging Face

---

## 📁 Project Structure
house-price-predictor/
├── app.py # Flask application
├── train_model.py # Trains and saves model
├── housing.csv # Dataset
├── house_model.pkl # Trained model
├── columns.pkl # Feature column list
├── requirements.txt # Dependencies
├── render.yaml # Render deployment config
└── templates/
└── index.html # Web form UI (Bootstrap)


## 📊 Dataset

Use any housing dataset (e.g., Ames Housing) with these columns:

- `OverallQual`
- `GrLivArea`
- `GarageCars`
- `GarageArea`
- `TotalBsmtSF`
- `FullBath`
- `YearBuilt`

---

## ⚙️ Local Setup Instructions

1. Clone the repository
git clone https://github.com/yourusername/house-price-predictor.git
cd house-price-predictor
2. Install dependencies
pip install -r requirements.txt
3. Train the model
python train_model.py
4. Start the Flask app
python app.py
Visit: http://127.0.0.1:5050

🌐 Web Interface Preview
Users can enter house details and get a price prediction:
Predicted Price: ₹ 2,19,090.00




