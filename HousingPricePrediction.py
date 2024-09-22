import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

file_path = 'Housing.csv'
data = pd.read_csv(file_path)


print(data[['price', 'area', 'bedrooms', 'bathrooms', 'stories', 'furnishingstatus']].head())

# One-hot encoding for the 'furnishingstatus' categorical feature
data = pd.get_dummies(data, columns=['furnishingstatus'], drop_first=True)

# Define features (include 'furnishingstatus' columns along with other features)
X = data[['area', 'bedrooms', 'bathrooms', 'stories', 'furnishingstatus_semi-furnished', 'furnishingstatus_unfurnished']]
y = data['price']   # Target variable (house price)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"Intercept: {model.intercept_}")

# Plotting the area vs predicted prices with color coding for furnishing status
plt.figure(figsize=(10, 6))

# Use the furnishingstatus columns to color-code the scatter plot
colors = {
    'furnishingstatus_semi-furnished': 'orange',
    'furnishingstatus_unfurnished': 'blue'
}

# Correct furnishing status mapping
furnishing_status = X_test[['furnishingstatus_semi-furnished', 'furnishingstatus_unfurnished']].idxmax(axis=1)

# Scatter plot of area vs predicted prices, colored by furnishingstatus
plt.scatter(X_test['area'], y_pred, c=furnishing_status.map(colors), label='Predicted Prices')

# Add a trendline
z = np.polyfit(X_test['area'], y_pred, 1)
p = np.poly1d(z)
plt.plot(X_test['area'], p(X_test['area']), color='red', linestyle='--', label='Trendline')

# Add labels and title
plt.xlabel('Area')
plt.ylabel('Predicted Prices')
plt.title('Predicted House Prices vs Area (Colored by Furnishing Status)')
plt.legend()

# Show plot
plt.show()
