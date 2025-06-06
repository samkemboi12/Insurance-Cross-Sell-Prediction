


# TruSecure Insurance Cross-Sell Prediction                                                                                               

This project aims to help TruSecure Insurance Company identify which health insurance customers 
are likely to also purchase vehicle insurance.
The solution involves exploratory data analysis (EDA), feature engineering, and predictive 
modeling using machine learning.
>>>>>>> f5f33de (Update README.md)

# Business Problem
TruSecure is launching a new vehicle insurance product and wants to:
Identify key customer characteristics that influence purchase decisions.
Segment customers for targeted marketing.
Predict customer conversion using a classification model.

# Exploratory Data Analysis (EDA)
## Annual_premium level and Insurance status vs customer response rate.:
![download](https://github.com/user-attachments/assets/d508b816-c64e-4145-8597-2cd0fc5c847a)

## Response Rate By Age group and Gender
Most customers are middle-aged, with a higher interest in vehicle insurance seen in younger groups.


![download](https://github.com/user-attachments/assets/e374fe01-21aa-4702-abc3-2b2e439609c6)

## Top 10 Policy Channels Vs Response Rate

Certain policy sales channels show higher conversion rates.
![download](https://github.com/user-attachments/assets/2ca6de67-f84c-498d-8eaa-2d8e637320ed)

# Data Preparation
Cleaned and standardized categorical fields

Encoded features using One-Hot and Ordinal Encoding

Scaled numerical variables like age and premium

Split data into training and validation sets


# Models Trained  
Logistic Regression	  
Random Forest          
LightGBM	                                                                                                                                                                                                   

XGBoost

LightGBM had the best ability to detect interested customers (high recall), which is critical in marketing use cases.


# Model Performance Comparison

| Model               | Accuracy | Class 1 Recall | Class 1 Precision | F1 Score (Class 1) | ROC AUC |
|--------------------|----------|----------------|--------------------|---------------------|---------|
| Logistic Regression| 0.88     | 0.00           | 0.40               | 0.00                | 0.8342  |
| XGBoost            | 0.72     | 0.90           | 0.29               | 0.44                | 0.8558  |
| Random Forest      | 0.69     | 0.94           | 0.28               | 0.43                | 0.8548  |
| LightGBM           | 0.70     | 0.93           | 0.28               | 0.43                | 0.8578  |


# Recommendations
Prioritize outreach to customers with a history of vehicle damage.

Focus marketing on high-performing sales channels.

Use the model's probabilities to rank and target top prospects.

Consider using SHAP for model explainability in future phases.

# Tech Stack
Python, Pandas, NumPy

Matplotlib, Seaborn

Scikit-learn, LightGBM

Jupyter Notebook


>>>>>>> 585b548 (Create README.md)
