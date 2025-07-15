from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and expected columns
model = joblib.load("house_model.pkl")
columns = joblib.load("columns.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if request.method == "POST":
            form_data = request.form.to_dict()
            df = pd.DataFrame([form_data], dtype=float)
            df = df.reindex(columns=columns, fill_value=0)
            prediction = round(model.predict(df)[0], 2)
            return render_template("index.html", prediction=prediction)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True, port=5050)
