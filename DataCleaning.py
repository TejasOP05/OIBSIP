import pandas as pd

# Load the dataset
file_path = 'AB_NYC_2019.csv'  # Update this path if necessary
data = pd.read_csv(file_path)

# 1. Handle missing values
# Fill missing 'reviews_per_month' with 0
data['reviews_per_month'] = data['reviews_per_month'].fillna(0)

# Remove rows with missing 'last_review'
data = data.dropna(subset=['last_review'])

# 2. Remove duplicates
data = data.drop_duplicates()

# 3. Ensure proper data types
data['last_review'] = pd.to_datetime(data['last_review'])

# Save the cleaned dataset
cleaned_file_path = 'cleaned_AB_NYC_2019.csv'
data.to_csv(cleaned_file_path, index=False)

print(f"Cleaned dataset saved to: {cleaned_file_path}")
