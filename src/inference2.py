from joblib import dump, load
import pandas as pd
import numpy as np
from .data_processor import log_txf, remap_emp_length
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, r2_score

def get_prediction(featurelist):
# Load your dataset
# Replace 'your_dataset.csv' with the actual path to your dataset
    data = pd.read_csv('data/cars.csv')

# Drop rows with missing values
    data.dropna(inplace=True)

# Define features and target
    X = data[['Age', 'KM', 'FuelType', 'HP', 'Automatic', 'CC', 'Doors', 'Weight']]
    y = data['Price']

# Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing: handle categorical variables
    categorical_features = ['FuelType']
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

# Combine preprocessing steps
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', categorical_transformer, categorical_features)
        ])

# Create the pipeline
    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('regressor', LinearRegression())])

# Fit the model
    pipeline.fit(X_train, y_train)

# Make predictions
    feature_df = pd.DataFrame([featurelist])
    y_pred = pipeline.predict(feature_df)
    return y_pred
