# Task 4: Feature Encoding & Scaling

## Objective
The objective of this task is to understand and implement **feature engineering techniques** such as 
**feature encoding** and **feature scaling** on a dataset, which are essential preprocessing steps in Machine Learning.

## Dataset
- Dataset Name: Adult Income Dataset (Synthetic version)
- File Used: `adult.csv`
- Target Column: `income`

## Tools & Technologies
- Python
- Pandas
- Scikit-learn
- VS Code
  
## Project Structure
Steps Performed

### 1. Loaded the Dataset
The dataset was loaded using Pandas and basic inspection was performed.

### 2. Identified Feature Types
- **Categorical Features**: workclass, education, marital_status, occupation, gender, income
- **Numerical Features**: age, education_num, hours_per_week

### 3. Feature Encoding
- Applied **Label Encoding** to convert categorical values into numerical form.

### 4. Feature Scaling
- Applied **StandardScaler** to numerical features to standardize them.

### 5. Saved the Processed Dataset
- The final preprocessed dataset was saved as `adult_processed.csv`.

## ✅ Output
- Preprocessed dataset ready for machine learning models
- File Generated: `adult_processed.csv`

## Learning Outcome
- Understood the importance of feature encoding
- Learned why feature scaling is required
- Gained hands-on experience with Scikit-learn preprocessing tools
- Improved understanding of feature engineering concepts


