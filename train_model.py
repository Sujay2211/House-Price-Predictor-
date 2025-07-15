import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("housing.csv")

# Features and target
features = ["OverallQual", "GrLivArea", "GarageCars", "GarageArea", "TotalBsmtSF", "FullBath", "YearBuilt"]
target = "SalePrice"

X = df[features]
y = df[target]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and columns
joblib.dump(model, "house_model.pkl")
joblib.dump(X.columns.tolist(), "columns.pkl")

print("✅ Model and columns saved!")
