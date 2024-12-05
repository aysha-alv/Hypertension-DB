# Lang Patient Database (lang-patient-db)

This project sets up a MongoDB database containing patient datasets to analyze comorbidities between hypertension and mental health conditions, focusing on depression and anxiety. The database is designed for healthcare analytics and research.

---

## Features

- Preprocessed datasets for hypertension and mental health conditions.
- Python script to automatically load datasets into MongoDB collections.
- Instructions to verify data and use it for analysis.

---

## Prerequisites

Before starting, ensure you have the following installed:

- Python (version 3.8 or higher)
- MongoDB (installed and running locally or accessible remotely)
- Required Python libraries (see `requirements.txt`)

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/lang-patient-db.git
cd lang-patient-db
```

### 2. Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### 3. Load Data into MongoDB

Run the Python script to load the datasets into your MongoDB instance:

```bash
python setup_mongodb.py
```

### 4. Start MongoDB Shell

To confirm the data is loaded successfully, start the MongoDB shell and verify:

```bash
mongosh
```

Then run the following commands:

```javascript
use health_data
show collections
```

You should see:

- `hypertension`
- `depression_anxiety`

---

## Project Structure

```
lang-patient-db/
├── setup_mongodb.py         # Script to load data into MongoDB
├── requirements.txt         # List of required Python libraries
├── README.md                # Project documentation
├── .gitignore               # Git ignore file
├── data/                    # Contains the datasets
│   ├── processed_depression_anxiety.csv
│   ├── final_hypertension_dataset.csv
```

---

## Datasets

### 1. `processed_depression_anxiety.csv`

- Contains data on depression and anxiety patients.
- Attributes: `patient_id`, `age`, `gender`, `anxiety_level`, `depression_level`, etc.

### 2. `final_hypertension_dataset.csv`

- Contains data on hypertension patients.
- Attributes: `patient_id`, `age`, `gender`, `blood_pressure`, `medication_status`, etc.

---

## Usage

1. Once the database is set up, you can access the data programmatically using MongoDB drivers for Python, such as `pymongo`.
   
2. Example query to fetch hypertension data:

```python
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["health_data"]

# Fetch hypertension collection
hypertension_data = db["hypertension"].find()

for record in hypertension_data:
    print(record)
```

3. Replace the query parameters to fit your analysis needs.

---

## Authors

- **Aysha**
- **Shruti**

---

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork this repository and submit a pull request.

---

## License

This project is open source and available under the MIT License. See the `LICENSE` file for details.

---
