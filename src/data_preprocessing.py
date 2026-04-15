# src/data_preprocessing.py

import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_and_preprocess():
    data_path = os.path.join(BASE_DIR, "data", "processed", "ridership_clean.csv")
    df = pd.read_csv(data_path, parse_dates=['transit_timestamp'])

    # Feature engineering
    model_df = pd.DataFrame()
    model_df['month'] = df['transit_timestamp'].dt.month
    model_df['day'] = df['transit_timestamp'].dt.day
    model_df['hour'] = df['transit_timestamp'].dt.hour
    model_df['borough'] = df['borough']
    model_df['payment_method'] = df['payment_method']
    model_df['ridership'] = df['ridership']

    # Aggregate ridership by time + categorical features
    model_df = model_df.groupby(['month', 'day', 'hour', 'borough', 'payment_method'])['ridership'].sum().reset_index()

    # Encode categorical features
    X = pd.get_dummies(model_df[['month', 'day', 'hour', 'borough', 'payment_method']],drop_first=True)
    y = model_df['ridership']

    return X, y


if __name__ == "__main__":
    DATA_DIR = os.path.join(BASE_DIR, "data", "raw_combined")
    file_path = os.path.join(DATA_DIR, "data.csv")
    df = pd.read_csv(file_path)

    # Cleaning steps...
    df['transit_timestamp'] = pd.to_datetime(df['transit_timestamp'])
    df.dropna(axis=1, inplace=True)
    df['borough'] = df['borough'].replace({
        'M': 'Manhattan', 'Q': 'Queens', 'BK': 'Brooklyn',
        'BX': 'Bronx', 'SI': 'Staten Island'
    })
    df['station_complex'] = df['station_complex'].str.replace(r'\(.*\)', '', regex=True)

    # Save cleaned dataset
    df.to_csv(os.path.join(BASE_DIR, "data", "processed", "ridership_clean.csv"), index=False)
    print(list(df.columns))


    # Save sample
    df_sample = df.sample(n=1000, random_state=42)
    sample_dir = os.path.join(BASE_DIR, "data", "sample_data")
    os.makedirs(sample_dir, exist_ok=True)
    df_sample.to_csv(os.path.join(sample_dir, "sample.csv"), index=False)

    print("Preprocessing complete. Cleaned and sample data saved.")
