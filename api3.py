from bs4 import BeautifulSoup
import requests
import pandas as pd

# Example HTML page.
html = """
<html>
<head>
    <title>Example Page</title>
</head>
<body>
    <h3><b id="boldest">LeBron James</b></h3>
    <p>Salary: $92,000,000</p>

    <table>
        <tr>
            <td>Flight No</td>
            <td>Launch site</td>
            <td>Payload mass</td>
        </tr>
        <tr>
            <td>1</td>
            <td>Florida</td>
            <td>300 kg</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Texas</td>
            <td>94 kg</td>
        </tr>
    </table>
</body>
</html>
"""

# Parse the HTML.
soup = BeautifulSoup(html, "html.parser")

# Get the page title.
print("Title:", soup.title.get_text(strip=True))

# Get the player's name.
player = soup.find(id="boldest")
print("Player:", player.get_text(strip=True))

# Find the table.
table = soup.find("table")

# Store rows here.
table_data = []

# Extract each row.
for row in table.find_all("tr"):

    # Extract each cell.
    cells = row.find_all("td")

    # Convert cells to text.
    values = [
        cell.get_text(strip=True)
        for cell in cells
    ]

    # Store the row.
    table_data.append(values)

# Convert the table into a DataFrame.
df = pd.DataFrame(
    table_data[1:],
    columns=table_data[0]
)

# Display the DataFrame.
print(df)