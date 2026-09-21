# University Motor Pool - Fuel Consumption Dataset

## Overview

This repository contains the dataset and preprocessing files used for the University Motor Pool / Fleet Management System.

The dataset supports the development of a Machine Learning model for predicting vehicle fuel consumption based on trip and vehicle information.

## Dataset

The dataset contains **10,000 trip records**.

### Features

| Feature | Description |
|---|---|
| Distance_km | Trip distance in kilometers |
| Vehicle_Type | Type of vehicle |
| Passengers | Number of passengers |
| Nominal_L_per_100km | Nominal fuel consumption in liters per 100 km |
| Duration_min | Trip duration in minutes |
| Fuel_Consumed_L | Fuel consumed in liters (Target) |

### Vehicle Types

- Sedan
- SUV
- Van
- Bus

## Data Type

**Note:** This is a **synthetic dataset** generated for the project. It is not collected from real vehicles.

## Preprocessing

The following preprocessing steps were performed:

1. Checked the dataset structure and data types.
2. Checked for missing values.
3. Checked for duplicate records.
4. Encoded the `Vehicle_Type` categorical feature.
5. Separated features from the target variable.
6. Split the dataset into training and testing sets.
7. Used an 80/20 train-test split.
8. Applied `StandardScaler` to numerical features.
9. Fitted the scaler using training data only to avoid data leakage.
10. Saved the processed datasets for the AI team.

## Train/Test Split

| Dataset | Number of Records |
|---|---:|
| Training Set | 8,000 |
| Testing Set | 2,000 |
| Total | 10,000 |

## Output Files

```text
dataset/
├── fleet_fuel_dataset_10000.csv
├── X_train.csv
├── X_test.csv
├── y_train.csv
└── y_test.csv

preprocessing/
└── preprocessing.ipynb

scaler.pkl
```

### File Description

- `fleet_fuel_dataset_10000.csv` - Original synthetic dataset.
- `X_train.csv` - Training features.
- `X_test.csv` - Testing features.
- `y_train.csv` - Training target values.
- `y_test.csv` - Testing target values.
- `scaler.pkl` - Saved StandardScaler used during preprocessing.
- `preprocessing.ipynb` - Notebook containing the preprocessing steps.

## Target Variable

The target variable is:

```text
Fuel_Consumed_L
```

The Machine Learning model will use the processed features to predict the expected fuel consumption of a trip.

## Project Context

This dataset is part of the University Motor Pool / Fleet Management System, which manages university vehicles, trip requests, vehicle availability, drivers, and trip information.

The prepared dataset will be used by the AI team for Machine Learning model development.


## Machine Learning Model

A Linear Regression model was trained using the prepared dataset.

The model was evaluated using MAE, RMSE, and R².

A baseline model using the mean target value was also used for comparison.

### Evaluation Results

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Baseline | 1.769871 | 2.507892 | -0.000113 |
| Linear Regression | 0.634576 | 0.952300 | 0.855795 |

The Linear Regression model achieved an R² of approximately 0.856 on the test set.

## FastAPI

The trained Machine Learning model is exposed through a FastAPI REST API.

### API Endpoint

```text
POST /predict
Input Example
{
  "Distance_km": 30,
  "Vehicle_Type": "Sedan",
  "Passengers": 4,
  "Nominal_L_per_100km": 7.5,
  "Duration_min": 50
}
Model Files
fuel_model.pkl - Trained Machine Learning model.
scaler.pkl - Saved feature scaler.
main.py - FastAPI application.

The API receives trip and vehicle information and returns the estimated fuel consumption.

## Status

- [x] Dataset preparation
- [x] Data inspection
- [x] Missing value check
- [x] Duplicate check
- [x] Categorical encoding
- [x] Train/Test split
- [x] Feature scaling
- [x] Preprocessed files saved
- [x] Machine Learning model training
- [x] Model evaluation
- [x] FastAPI model integration
- [ ] Model integration with ASP.NET Core MVC MVC
