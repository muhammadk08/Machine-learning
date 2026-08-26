# Revenue Data and Dashboard Project
# Extract Tesla and GameStop stock prices and revenue,
# then create historical price and revenue graphs.

import warnings
from io import StringIO

import matplotlib.pyplot as plt
import pandas as pd
import requests
import yfinance as yf
from bs4 import BeautifulSoup


# Hide unnecessary FutureWarning messages.
warnings.filterwarnings(
    "ignore",
    category=FutureWarning
)


# ============================================================
# HELPER FUNCTION: REMOVE TIMEZONE
# ============================================================

def make_timezone_naive(series):
    """
    Convert a date Series into timezone-naive datetime values.

    Yahoo Finance often returns timezone-aware dates.
    Revenue tables usually return timezone-naive dates.
    Removing the timezone allows both types to be compared.
    """

    # Convert values into datetime objects.
    dates = pd.to_datetime(
        series,
        errors="coerce"
    )

    # If the dates have a timezone, remove it.
    if hasattr(dates.dt, "tz") and dates.dt.tz is not None:
        dates = dates.dt.tz_localize(None)

    return dates


# ============================================================
# HELPER FUNCTION: CLEAN REVENUE TABLE
# ============================================================

def clean_revenue_table(tables, table_index=1):
    """
    Select and clean a revenue table.

    The assignment uses table index 1.
    The first column is Date.
    The second column is Revenue.
    """

    # Select the requested table and make a copy.
    revenue = tables[table_index].copy()

    print("\nOriginal revenue columns:")
    print(revenue.columns)

    # Keep the first two columns.
    # This avoids problems caused by long table-title headers.
    revenue = revenue.iloc[:, :2].copy()

    # Give the columns simple names.
    revenue.columns = [
        "Date",
        "Revenue"
    ]

    # Remove commas and dollar signs.
    revenue["Revenue"] = (
        revenue["Revenue"]
        .astype(str)
        .str.replace(",", "", regex=True)
        .str.replace("$", "", regex=False)
        .str.strip()
    )

    # Convert revenue into numeric values.
    revenue["Revenue"] = pd.to_numeric(
        revenue["Revenue"],
        errors="coerce"
    )

    # Convert dates to timezone-naive datetime values.
    revenue["Date"] = make_timezone_naive(
        revenue["Date"]
    )

    # Remove rows with missing data.
    revenue.dropna(
        subset=["Date", "Revenue"],
        inplace=True
    )

    # Sort the data from oldest to newest.
    revenue.sort_values(
        "Date",
        inplace=True
    )

    # Reset the index.
    revenue.reset_index(
        drop=True,
        inplace=True
    )

    return revenue


# ============================================================
# GRAPHING FUNCTION
# ============================================================

def makegraph(stockdata, revenuedata, stock):
    """
    Create two graphs for one company:

    1. Historical closing stock price.
    2. Historical quarterly revenue.
    """

    # Make copies so the original DataFrames stay unchanged.
    stockdata = stockdata.copy()
    revenuedata = revenuedata.copy()

    # Convert both date columns to timezone-naive datetimes.
    stockdata["Date"] = make_timezone_naive(
        stockdata["Date"]
    )

    revenuedata["Date"] = make_timezone_naive(
        revenuedata["Date"]
    )

    # Remove invalid dates.
    stockdata.dropna(
        subset=["Date"],
        inplace=True
    )

    revenuedata.dropna(
        subset=["Date"],
        inplace=True
    )

    # Create timezone-naive comparison dates.
    stock_end_date = pd.Timestamp(
        "2021-06-14"
    )

    revenue_end_date = pd.Timestamp(
        "2021-04-30"
    )

    # Filter stock data.
    stockdata_specific = stockdata[
        stockdata["Date"] <= stock_end_date
    ]

    # Filter revenue data.
    revenuedata_specific = revenuedata[
        revenuedata["Date"] <= revenue_end_date
    ]

    # Create two graphs.
    fig, axes = plt.subplots(
        2,
        1,
        figsize=(12, 8),
        sharex=False
    )

    # --------------------------------------------------------
    # Graph 1: Historical closing stock price
    # --------------------------------------------------------

    axes[0].plot(
        stockdata_specific["Date"],
        stockdata_specific["Close"],
        label="Share Price",
        color="blue"
    )

    axes[0].set_ylabel(
        "Price US$"
    )

    axes[0].set_title(
        f"{stock} - Historical Share Price"
    )

    axes[0].legend()
    axes[0].grid(True)

    # --------------------------------------------------------
    # Graph 2: Historical revenue
    # --------------------------------------------------------

    axes[1].plot(
        revenuedata_specific["Date"],
        revenuedata_specific["Revenue"],
        label="Revenue",
        color="green",
        marker="o"
    )

    axes[1].set_ylabel(
        "Revenue US Millions"
    )

    axes[1].set_xlabel(
        "Date"
    )

    axes[1].set_title(
        f"{stock} - Historical Revenue"
    )

    axes[1].legend()
    axes[1].grid(True)

    # Prevent labels from overlapping.
    plt.tight_layout()

    # Display the graphs.
    plt.show()


# ============================================================
# TESLA STOCK DATA
# ============================================================

print("Downloading Tesla stock data...")

# TSLA is Tesla's ticker symbol.
tesla = yf.Ticker("TSLA")

# Download Tesla's maximum available history.
tesladata = tesla.history(
    period="max"
)

# Stop if no stock data was returned.
if tesladata.empty:
    raise RuntimeError(
        "Tesla stock data could not be downloaded."
    )

# Move Date from the index to a normal column.
tesladata.reset_index(
    inplace=True
)

# Remove timezone information from Tesla dates.
tesladata["Date"] = make_timezone_naive(
    tesladata["Date"]
)

print("\nTesla stock data:")
print(tesladata.head())


# ============================================================
# TESLA REVENUE DATA
# ============================================================

print("\nDownloading Tesla revenue data...")

# Tesla revenue webpage.
tesla_revenue_url = (
    "https://cf-courses-data.s3.us.cloud-object-storage."
    "appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-"
    "SkillsNetwork/labs/project/revenue.htm"
)

# Download the webpage.
tesla_response = requests.get(
    tesla_revenue_url,
    timeout=30
)

# Stop if the request failed.
tesla_response.raise_for_status()

# Store the HTML text.
htmldata = tesla_response.text

# Parse the HTML with BeautifulSoup.
soup = BeautifulSoup(
    htmldata,
    "html.parser"
)

# Read all HTML tables.
# StringIO tells Pandas this is HTML content,
# not a filename.
tesla_tables = pd.read_html(
    StringIO(htmldata)
)

print(
    "Tesla tables found:",
    len(tesla_tables)
)

# Clean Tesla's revenue table.
teslarevenue = clean_revenue_table(
    tesla_tables,
    table_index=1
)

print("\nClean Tesla revenue data:")
print(teslarevenue.tail())


# ============================================================
# GAMESTOP STOCK DATA
# ============================================================

print("\nDownloading GameStop stock data...")

# GME is GameStop's ticker symbol.
gme = yf.Ticker("GME")

# Download GameStop's maximum available history.
gmedata = gme.history(
    period="max"
)

# Stop if no stock data was returned.
if gmedata.empty:
    raise RuntimeError(
        "GameStop stock data could not be downloaded."
    )

# Move Date from the index to a normal column.
gmedata.reset_index(
    inplace=True
)

# Remove timezone information from GameStop dates.
gmedata["Date"] = make_timezone_naive(
    gmedata["Date"]
)

print("\nGameStop stock data:")
print(gmedata.head())


# ============================================================
# GAMESTOP REVENUE DATA
# ============================================================

print("\nDownloading GameStop revenue data...")

# GameStop revenue webpage.
gme_revenue_url = (
    "https://cf-courses-data.s3.us.cloud-object-storage."
    "appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-"
    "SkillsNetwork/labs/project/stock.html"
)

# Download the webpage.
gme_response = requests.get(
    gme_revenue_url,
    timeout=30
)

# Stop if the request failed.
gme_response.raise_for_status()

# Store the HTML text.
htmldata2 = gme_response.text

# Parse the HTML with BeautifulSoup.
soup_gme = BeautifulSoup(
    htmldata2,
    "html.parser"
)

# Read all HTML tables.
gme_tables = pd.read_html(
    StringIO(htmldata2)
)

print(
    "GameStop tables found:",
    len(gme_tables)
)

# Clean GameStop's revenue table.
gmerevenue = clean_revenue_table(
    gme_tables,
    table_index=1
)

print("\nClean GameStop revenue data:")
print(gmerevenue.tail())


# ============================================================
# CREATE THE GRAPHS
# ============================================================

print("\nCreating Tesla graphs...")

makegraph(
    tesladata,
    teslarevenue,
    "Tesla"
)

print("\nCreating GameStop graphs...")

makegraph(
    gmedata,
    gmerevenue,
    "GameStop"
)