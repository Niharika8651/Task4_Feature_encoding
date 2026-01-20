# Task 4: Feature Encoding & Scaling
# Dataset: Adult Income Dataset

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler


# 1. Load Dataset

df = pd.read_csv("data/adult.csv")

print("Original Dataset")
print(df.head())
print("\nDataset Info:")
print(df.info())


# 2. Identify Categorical and Numerical Features

categorical_cols = df.select_dtypes(include='object').columns
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns

print("\nCategorical Columns:")
print(categorical_cols)

print("\nNumerical Columns:")
print(numerical_cols)


# 3. Apply Label Encoding

label_encoder = LabelEncoder()

for col in categorical_cols:
    df[col] = label_encoder.fit_transform(df[col])

print("\nDataset After Label Encoding:")
print(df.head())


# 4. Apply Feature Scaling

scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

print("\nDataset After Feature Scaling:")
print(df.head())


# 5. Save Processed Dataset

df.to_csv("data/adult_processed.csv", index=False)

print("\n✅ Feature Encoding and Scaling Completed Successfully!")
print("✅ Processed dataset saved as data/adult_processed.csv")
