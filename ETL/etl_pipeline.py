# ETL Pipeline for Customer Churn Dataset

import pandas as pd


def load_data(file_path):
    """Load the dataset."""
    df = pd.read_csv(file_path)
    print("Dataset Loaded Successfully!")
    print("Dataset Shape:", df.shape)
    return df


def clean_data(df):
    """Clean the dataset."""
    
    # Convert TotalCharges to Numeric
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    print("\nData Type of TotalCharges:")
    print(df["TotalCharges"].dtype)

    # Check Missing Values
    print("\nMissing Values Before Cleaning:")
    print(df.isnull().sum())

    # Remove Missing Values
    df.dropna(inplace=True)

    print("\nMissing Values After Cleaning:")
    print(df.isnull().sum())

    print("\nUpdated Dataset Shape:", df.shape)

    return df


def save_data(df, output_path):
    """Save cleaned dataset."""
    df.to_csv(output_path, index=False)
    print("\nCleaned Dataset Saved Successfully!")


def main():
    input_file = "Dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv"
    output_file = "Dataset/cleaned_customer_churn.csv"

    df = load_data(input_file)
    df = clean_data(df)
    save_data(df, output_file)


if __name__ == "__main__":
    main()