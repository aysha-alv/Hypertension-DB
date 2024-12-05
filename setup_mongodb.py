from pymongo import MongoClient
import pandas as pd
import os

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["lang_patient_db"]

# Load processed data
data_folder = "data"
processed_file = os.path.join(data_folder, "processed_data.csv")
processed_data = pd.read_csv(processed_file)

# Insert data into MongoDB
collection = db["patient_data"]
data_dict = processed_data.to_dict(orient="records")
collection.insert_many(data_dict)

print("Data uploaded to MongoDB.")
