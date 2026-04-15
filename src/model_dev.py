import os
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from data_preprocessing import load_and_preprocess

def train_and_save_model():
    # Load features and labels
    X, y = load_and_preprocess()

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    models = {
    
        "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42),
        "GradientBoosting": GradientBoostingRegressor(random_state=42),
    }

    results = {}
    model_dir = "../models"
    os.makedirs(model_dir, exist_ok=True)

    for name, model in models.items():
        # Train model
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Evaluate
        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        results[name] = {"R²": r2, "RMSE": rmse}

        # Save model in loop
        model_path = os.path.join(model_dir, f"{name}.pkl")
        joblib.dump(model, model_path)
        print(f" {name} saved to {model_path}")

    print("\n Model Comparison:")
    for name, metrics in results.items():
        print(f"{name}: R²={metrics['R²']:.3f}, RMSE={metrics['RMSE']:.3f}")

if __name__ == "__main__":
    train_and_save_model()
