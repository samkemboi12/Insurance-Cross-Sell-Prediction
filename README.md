TruSecure Insurance Cross-Sell Prediction
This project aims to help TruSecure Insurance Company identify which health insurance customers are likely to also purchase vehicle insurance.
The solution involves exploratory data analysis (EDA), feature engineering, and predictive modeling using machine learning.

Business Problem
TruSecure is launching a new vehicle insurance product and wants to:
Identify key customer characteristics that influence purchase decisions.
Segment customers for targeted marketing.
Predict customer conversion using a classification model.

Exploratory Data Analysis (EDA)
Demographic Insights:
![download](https://github.com/user-attachments/assets/9071c69c-090d-4595-85e0-3cb98d6a6eb1)

Most customers are middle-aged, with a higher interest in vehicle insurance seen in younger groups.


![download](https://github.com/user-attachments/assets/e374fe01-21aa-4702-abc3-2b2e439609c6)

Risk & Policy Behavior:

Customers with a history of vehicle damage are more likely to convert.

Certain policy sales channels show higher conversion rates.
![download](https://github.com/user-attachments/assets/2ca6de67-f84c-498d-8eaa-2d8e637320ed)

Data Preparation
Cleaned and standardized categorical fields

Encoded features using One-Hot and Ordinal Encoding

Scaled numerical variables like age and premium

Split data into training and validation sets


Models Trained
Model	Accuracy	    Class 1 Recall	ROC AUC
Logistic Regression	   0.88	0.00	~0.50
Random Forest          0.84	~0.35	~0.80
LightGBM	             0.70	 0.93	 0.86  (Best)

LightGBM had the best ability to detect interested customers (high recall), which is critical in marketing use cases.

Business Insights


Previously Uninsured customers are more open to cross-selling.

Certain channels (like Channel 26 and 124) had higher conversion — can be prioritized.

Younger customers and those in specific regions respond more positively.

💼 Recommendations
Prioritize outreach to customers with a history of vehicle damage.

Focus marketing on high-performing sales channels.

Use the model's probabilities to rank and target top prospects.

Consider using SHAP for model explainability in future phases.

🔧 Tech Stack
Python, Pandas, NumPy

Matplotlib, Seaborn

Scikit-learn, LightGBM

Jupyter Notebook


