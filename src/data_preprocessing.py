
import pandas as pd
import os 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define your custom data path
DATA_DIR = os.path.join(BASE_DIR, "data", "raw_combined")

# Example: load a CSV file
file_path = os.path.join(DATA_DIR, "data.csv")
df = pd.read_csv(file_path)

print("Data Loaded Successfully!!!!")


#Data Cleaning 

print("Loading Data Cleaning!!!!!!!!!!!!!!!!!")
# change transit_timestamp to datetime object
df['transit_timestamp'] = pd.to_datetime(df['transit_timestamp'])

# check the earliest and latest time of the data
print(df['transit_timestamp'].min())
print(df['transit_timestamp'].max())

# Check for NaN values in each column
df.isnull().sum()
# Drop columns with NaN values
df.dropna(axis=1, inplace=True)

# Check is there is any NaN values
df.isnull().sum()

df.info()

df.shape

#get unique values of column borough. update value M into Manhattan, Q to Queens, BK to Brooklyn, BX to Bronx, SI to Staten Island
df['borough'] = df['borough'].replace({
    'M': 'Manhattan',
    'Q': 'Queens',
    'BK': 'Brooklyn',
    'BX': 'Bronx',
    'SI': 'Staten Island'
})

#get unique values of column borough.
unique_boroughs = df['borough'].unique()
print(unique_boroughs)

# remove the () and everything in between the () from each station_complex row in the df
df['station_complex'] = df['station_complex'].str.replace(r'\(.*\)', '', regex=True)

print(df.head())

df.to_csv(os.path.join(BASE_DIR, "data", "processed", "ridership_clean.csv"), index=False)
df_sample = df.sample(n=1000, random_state=42)

sample_dir = os.path.join(BASE_DIR, "data", "sample_data")
os.makedirs(sample_dir, exist_ok=True)

output_path = os.path.join(sample_dir, "sample.csv")
df_sample.to_csv(output_path, index=False)
print(df.columns.tolist())
