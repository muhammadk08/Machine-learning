import numpy as np
import pandas as pd


# Store the webpage URL.
URL = (
    "https://web.archive.org/web/20230902185326/"
    "https://en.wikipedia.org/wiki/"
    "List_of_countries_by_GDP_(nominal)"
)


# Read all HTML tables from the webpage.
tables = pd.read_html(URL)

print("Number of tables found:", len(tables))


# Select the table containing IMF GDP information.
df = tables[3]

print("\nOriginal table:")
print(df.head())


# Replace column names with numbers.
df.columns = range(df.shape[1])


# Keep country name and IMF GDP columns.
df = df[[0, 2]]


# Keep the top 10 countries.
df = df.iloc[1:11, :]


# Rename the columns.
df.columns = [
    "Country",
    "GDP Million USD"
]


print("\nTop 10 countries in million USD:")
print(df)


# Convert GDP values from text to integers.
df["GDP Million USD"] = (
    df["GDP Million USD"].astype(int)
)


# Convert million USD to billion USD.
df["GDP Million USD"] = (
    df["GDP Million USD"] / 1000
)


# Round GDP values to two decimal places.
df["GDP Million USD"] = np.round(
    df["GDP Million USD"],
    2
)


# Rename the column because values are now in billions.
df.rename(
    columns={
        "GDP Million USD": "GDP Billion USD"
    },
    inplace=True
)


# Display the final table.
print("\nFinal GDP table:")
print(df)


# Save the final DataFrame as a CSV file.
df.to_csv(
    "Largesteconomies.csv",
    index=False
)


print(
    "\nFinished! "
    "The file Largesteconomies.csv was created."
)