import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("customer_shopping_data.csv")

print("Data Overview:")
print(data.head())

print("\nData Info:")
print(data.info())

print("\nMissing Values:")
print(data.isnull().sum())

print("\nStatistical Summary:")
print(data.describe())


data['Sales'] = data['quantity'] * data['price']

# Convert Date column to datetime format
data['invoice_date'] = pd.to_datetime(data['invoice_date'], dayfirst=True)

# Univariate Analysis - Sales Distribution
plt.figure(figsize=(8, 5))
sns.histplot(data['Sales'], bins=30, kde=True)
plt.title('Sales Distribution')
plt.show()

# Bivariate Analysis - Sales by Product Category
plt.figure(figsize=(10, 6))
sns.boxplot(x='category', y='Sales', data=data)
plt.title('Sales by Product Category')
plt.xticks(rotation=45)
plt.show()

# Group by 'shopping_mall' and sum only numerical columns
grouped_data = data.groupby('shopping_mall')[['Sales']].sum().reset_index()

# Store Performance - Sales by Location
plt.figure(figsize=(10, 6))
sns.barplot(x='shopping_mall', y='Sales', data=grouped_data)
plt.title('Total Sales by Shopping Mall')
plt.xticks(rotation=45)
plt.show()

# Time Series Analysis - Sales Over Time
sales_by_date = data.groupby('invoice_date')['Sales'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.plot(sales_by_date['invoice_date'], sales_by_date['Sales'], marker='o')
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Select only numerical columns for correlation
numerical_columns = ['age', 'quantity', 'price', 'Sales']
corr_matrix = data[numerical_columns].corr()

# Correlation Heatmap - Identify relationships between variables
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Product Performance - Top-Selling Products
top_products = data.groupby('category')['Sales'].sum().sort_values(ascending=False).reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='category', y='Sales', data=top_products)
plt.title('Top-Selling Products')
plt.xticks(rotation=45)
plt.show()

# Promotional Impact - Sales during promotions
if 'Promotion' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Promotion', y='Sales', data=data)
    plt.title('Sales Impact During Promotions')
    plt.xticks(rotation=45)
    plt.show()

# Conclusion - Summary of findings
print("\nSummary of Insights:")
print("1. Key trends in product sales and store performance.")
print("2. Understanding the impact of promotions on sales.")
print("3. Time-based trends for inventory and marketing decisions.")
