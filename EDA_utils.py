

def check_outliers(df, feature):
    Q1 = df[feature].quantile(0.25)
    Q3 = df[feature].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df[feature] < lower_bound) | (df[feature] > upper_bound)]

    print(f"Feature: {feature}")
    print(f"Number of outliers: {len(outliers)}")
    print(f"Percentage of outliers: {100 * len(outliers) / len(df):.2f}%")
    print(f"IQR bounds: [{lower_bound:.2f}, {upper_bound:.2f}]")

def check_data_quality(df):
    """
    Displays the number of duplicate rows,
    null values per column, and percentage of nulls per column.
    """
    print("Duplicate Rows:", df.duplicated().sum())
    print("\n Null Values per Column:\n", df.isnull().sum())
    print("\n Percentage of Nulls per Column:\n", ((df.isnull().sum() / len(df)) * 100).round(2))
