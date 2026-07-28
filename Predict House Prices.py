from sklearn.linear_model import LinearRegression

# 1. Provide the data (Features must be 2D array)
X = [[1000], [1500], [2000], [2500]]  # Size in sq ft
y = [200000, 300000, 400000, 500000]  # Price in $

# 2. Initialize and train the model
model = LinearRegression()
model.fit(X, y)

# 3. Predict price for a 1,800 sq ft house
new_house = [[1800]]
predicted_price = model.predict(new_house)

print(f"Estimated Price is: ${predicted_price[0]:,.2f}")
# Output: Estimated Price: $360,000.00