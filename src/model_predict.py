import joblib
import pandas as pd
import os
from src.data_preprocessing import load_and_preprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def predict_with_model(model_name, new_data):
    # Load trained model (trained on dummy-encoded features)
    model = joblib.load(os.path.join(BASE_DIR, "models", f"{model_name}.pkl"))

    # Get training features to know the dummy columns
    X_train, _ = load_and_preprocess()
    all_columns = pd.get_dummies(X_train).columns

    # Encode new data with same dummy logic
    new_data_encoded = pd.get_dummies(new_data)

    # Align columns with training (missing columns filled with 0)
    new_data_encoded = new_data_encoded.reindex(columns=all_columns, fill_value=0)

    # Predict
    predictions = model.predict(new_data_encoded)
    return predictions

if __name__ == "__main__":
    new_data = pd.DataFrame({
        'month': [12],
        'day': [28],
        'hour': [13],
        'borough': ['Manhattan'],
        'payment_method': ['Omny']
    })

    rf_results = predict_with_model("RandomForest", new_data)
    gb_results = predict_with_model("GradientBoosting", new_data)

    print("RandomForest prediction:", [round(num) for num in rf_results])
    print("GradientBoost prediction:", [round(num) for num in gb_results])
