import pandas as pd

print("=== STEP 1: Load CSV ===")

csv_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"
df = pd.read_csv(csv_url)

print("\nFirst 5 rows from CSV:")
print(df.head())


print("\n=== STEP 2: Load Excel ===")

xlsx_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n9LOuKI9SlUa1b5zkaCMeg/Product-sales.xlsx"
df = pd.read_excel(xlsx_path)

print("\nFirst 5 rows from Excel:")
print(df.head())


print("\n=== STEP 3: Select specific columns ===")

y = df[["Product", "Category", "Quantity"]]
print(y)


print("\n=== STEP 4: Access elements with iloc ===")

print("df.iloc[0, 0]  (1st row, 1st col):", df.iloc[0, 0])
print("df.iloc[1, 0]  (2nd row, 1st col):", df.iloc[1, 0])
print("df.iloc[0, 2]  (1st row, 3rd col):", df.iloc[0, 2])
print("df.iloc[1, 2]  (2nd row, 3rd col):", df.iloc[1, 2])


print("\n=== STEP 5: Access elements with loc ===")

print("df.loc[0, 'Product']:", df.loc[0, "Product"])
print("df.loc[1, 'Product']:", df.loc[1, "Product"])
print("df.loc[1, 'CustomerCity']:", df.loc[1, "CustomerCity"])
print("df.loc[1, 'Total']:", df.loc[1, "Total"])


print("\n=== STEP 6: Slicing with iloc (rows 0–1, cols 0–2) ===")

print(df.iloc[0:2, 0:3])


print("\n=== STEP 7: Slicing with loc (rows 0–2, 'OrderID' to 'Category') ===")

print(df.loc[0:2, "OrderID":"Category"])