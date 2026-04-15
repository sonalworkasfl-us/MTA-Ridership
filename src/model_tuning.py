# src/model_tuning.py

import os
import joblib
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

from data_preprocessing import load_and_preprocess

def tune_and_save_models():
    X, y = load_and_preprocess()

    param_grids = {
        "RandomForest": {
            "n_estimators": [100, 200, 300],
            "max_depth": [None, 10, 20],
            "max_features": ["auto", "sqrt"]
        },
        "GradientBoosting": {
            "n_estimators": [100, 200],
            "learning_rate": [0.01, 0.1, 0.2],
            "max_depth": [3, 5, 7]
        }
    }

    models = {
        
        "RandomForest": RandomForestRegressor(random_state=42),
        "GradientBoosting": GradientBoostingRegressor(random_state=42),
    }

    model_dir = "../models"
    os.makedirs(model_dir, exist_ok=True)

    for name, model in models.items():
        print(f" Tuning {name}...")
        grid_search = GridSearchCV(
            estimator=model,
            param_grid=param_grids[name],
            cv=5,
            scoring="r2",
            n_jobs=-1
        )
        grid_search.fit(X, y)

        print(f"Best params for {name}: {grid_search.best_params_}")
        print(f"Best CV R²: {grid_search.best_score_:.3f}")

        
        model_path = os.path.join(model_dir, f"{name}_tuned.pkl")
        joblib.dump(grid_search.best_estimator_, model_path)
        print(f"💾 Saved tuned {name} to {model_path}")

if __name__ == "__main__":
    tune_and_save_models()
