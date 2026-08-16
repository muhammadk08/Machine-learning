# Working With Different File Formats Lab
# This script contains the main runnable code from the lab.
# Put this file in the same folder as your local data files.

import json
import os
import xml.etree.ElementTree as ET

import numpy as np
import pandas as pd

# Optional libraries used later in the lab.
# Install them with:
# python -m pip install openpyxl pillow matplotlib seaborn lxml


# ============================================================
# 1. CSV FILES
# ============================================================

# Read a CSV file that has no header row.
# Change this filename if your file has a different name.
if os.path.exists("addresses.csv"):
    addresses_df = pd.read_csv("addresses.csv", header=None)

    # Add column names manually.
    addresses_df.columns = [
        "First Name",
        "Last Name",
        "Location",
        "City",
        "State",
        "Area Code",
    ]

    print("CSV data:")
    print(addresses_df)

    # Select one column.
    print("\nFirst names:")
    print(addresses_df["First Name"])

    # Select multiple columns.
    print("\nSelected columns:")
    print(addresses_df[["First Name", "Last Name", "City"]])

    # Select the first row using labels.
    print("\nFirst row with loc:")
    print(addresses_df.loc[0])

    # Select rows 0, 1, and 2 from the First Name column.
    print("\nFirst three names with loc:")
    print(addresses_df.loc[[0, 1, 2], "First Name"])

    # Select rows 0, 1, and 2 from column position 0.
    print("\nFirst three names with iloc:")
    print(addresses_df.iloc[[0, 1, 2], 0])
else:
    print("addresses.csv was not found; skipping CSV section.")


# ============================================================
# 2. PANDAS TRANSFORM
# ============================================================

# Create a simple numeric DataFrame.
transform_df = pd.DataFrame(
    np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]),
    columns=["a", "b", "c"],
)

print("\nOriginal DataFrame:")
print(transform_df)

# Add 10 to every value.
added_df = transform_df.transform(lambda value: value + 10)

print("\nAfter adding 10:")
print(added_df)

# Calculate the square root of every value.
square_root_df = added_df.transform(np.sqrt)

print("\nSquare roots:")
print(square_root_df)


# ============================================================
# 3. JSON FILES
# ============================================================

# Create a Python dictionary.
person = {
    "first_name": "Mark",
    "last_name": "abc",
    "age": 27,
    "address": {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100",
    },
}

# Save the dictionary directly to a JSON file.
with open("person.json", "w", encoding="utf-8") as file:
    json.dump(person, file, indent=4)

# Convert the dictionary to a formatted JSON string.
json_text = json.dumps(person, indent=4)

# Save the JSON string to another file.
with open("sample.json", "w", encoding="utf-8") as file:
    file.write(json_text)

print("\nJSON text:")
print(json_text)

# Read JSON back into a Python dictionary.
with open("sample.json", "r", encoding="utf-8") as file:
    loaded_person = json.load(file)

print("\nLoaded JSON object:")
print(loaded_person)
print(type(loaded_person))


# ============================================================
# 4. EXCEL FILES
# ============================================================

# Requires: python -m pip install openpyxl
if os.path.exists("sample.xlsx"):
    excel_df = pd.read_excel("sample.xlsx")
    print("\nExcel data:")
    print(excel_df)
else:
    print("\nsample.xlsx was not found; skipping Excel section.")


# ============================================================
# 5. CREATE AN XML FILE
# ============================================================

# Create the root XML element.
employee = ET.Element("employee")

# Create a child element.
details = ET.SubElement(employee, "details")

# Create fields inside details.
first_name = ET.SubElement(details, "firstname")
last_name = ET.SubElement(details, "lastname")
age = ET.SubElement(details, "age")

# Add text values.
first_name.text = "Shiv"
last_name.text = "Mishra"
age.text = "23"

# Save the XML tree.
xml_tree = ET.ElementTree(employee)
xml_tree.write("new_sample.xml", encoding="utf-8", xml_declaration=True)

print("\nCreated new_sample.xml")


# ============================================================
# 6. READ THE CREATED XML FILE
# ============================================================

xml_tree = ET.parse("new_sample.xml")
xml_root = xml_tree.getroot()

xml_details = xml_root.find("details")

if xml_details is not None:
    xml_record = {
        "firstname": xml_details.findtext("firstname"),
        "lastname": xml_details.findtext("lastname"),
        "age": xml_details.findtext("age"),
    }

    xml_df = pd.DataFrame([xml_record])

    print("\nXML data as a DataFrame:")
    print(xml_df)


# ============================================================
# 7. READ A LARGER XML FILE IF IT EXISTS
# ============================================================

xml_filename = "Sample-employee-XML-file.xml"

if os.path.exists(xml_filename):
    # Pandas can read repeating XML nodes directly.
    employee_df = pd.read_xml(
        xml_filename,
        xpath=".//details",
    )

    print("\nEmployee XML data:")
    print(employee_df)

    # Save the XML DataFrame as CSV.
    employee_df.to_csv("employee.csv", index=False)
    print("Saved employee.csv")
else:
    print(
        f"\n{xml_filename} was not found; skipping larger XML section."
    )


# ============================================================
# 8. GENERAL DATA ANALYSIS
# ============================================================

# If diabetes.csv is in this folder, inspect it.
diabetes_filename = "diabetes.csv"

if os.path.exists(diabetes_filename):
    diabetes_df = pd.read_csv(diabetes_filename)

    print("\nFirst five diabetes rows:")
    print(diabetes_df.head())

    print("\nLast five diabetes rows:")
    print(diabetes_df.tail())

    print("\nDataFrame shape:")
    print(diabetes_df.shape)

    print("\nDataFrame information:")
    diabetes_df.info()

    print("\nStatistical summary:")
    print(diabetes_df.describe())

    print("\nMissing values per column:")
    print(diabetes_df.isnull().sum())

    print("\nData types:")
    print(diabetes_df.dtypes)
else:
    print("\ndiabetes.csv was not found; skipping analysis section.")


# ============================================================
# 9. OPTIONAL VISUALIZATION
# ============================================================

# Requires:
# python -m pip install matplotlib seaborn

try:
    import matplotlib.pyplot as plt
    import seaborn as sns  # noqa: F401

    if os.path.exists(diabetes_filename):
        labels = ["Not Diabetic", "Diabetic"]

        plt.pie(
            diabetes_df["Outcome"].value_counts(),
            labels=labels,
            autopct="%0.02f%%",
        )
        plt.legend()
        plt.title("Diabetes Outcome")
        plt.show()
except ImportError:
    print(
        "\nInstall matplotlib and seaborn to run the visualization section."
    )


# ============================================================
# 10. COMMON READ/SAVE FUNCTIONS
# ============================================================

# CSV:
# df = pd.read_csv("file.csv")
# df.to_csv("file.csv", index=False)

# JSON:
# df = pd.read_json("file.json")
# df.to_json("file.json")

# Excel:
# df = pd.read_excel("file.xlsx")
# df.to_excel("file.xlsx", index=False)

# XML:
# df = pd.read_xml("file.xml")

# SQL:
# df = pd.read_sql("SELECT * FROM table_name", connection)
# df.to_sql("table_name", connection, index=False)