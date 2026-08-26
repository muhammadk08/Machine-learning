# Stock Data Project
#Extracting Stock Data Using a Python Library

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. APPLE STOCK OBJECT
# ============================================================

# AAPL is Apple's stock ticker symbol.
apple = yf.Ticker("AAPL")


# ============================================================
# 2. APPLE INFORMATION
# ============================================================

# Get Apple's general company information.
# The result is a Python dictionary.
apple_info = apple.info

print("Apple information type:")
print(type(apple_info))


# Get Apple's country.
apple_country = apple_info.get(
    "country",
    "Country unavailable"
)

print("\nApple country:")
print(apple_country)


# ============================================================
# 3. APPLE HISTORICAL PRICES
# ============================================================

# Download Apple's maximum available historical data.
apple_share_price_data = apple.history(
    period="max"
)

print("\nApple historical data:")
print(apple_share_price_data.head())


# Move Date from the index to a normal column.
apple_share_price_data.reset_index(
    inplace=True
)


# ============================================================
# 4. APPLE OPENING-PRICE GRAPH
# ============================================================

# Plot Apple's opening price over time.
apple_share_price_data.plot(
    x="Date",
    y="Open",
    title="Apple Opening Price"
)

plt.show()


# ============================================================
# 5. APPLE DIVIDENDS
# ============================================================

# Get Apple's historical dividends.
apple_dividends = apple.dividends

print("\nApple dividends:")
print(apple_dividends.head())


# Plot Apple's dividends.
apple_dividends.plot(
    title="Apple Dividends"
)

plt.show()


# ============================================================
# 6. AMD STOCK OBJECT
# ============================================================

# AMD is Advanced Micro Devices' ticker symbol.
amd = yf.Ticker("AMD")


# ============================================================
# 7. AMD INFORMATION
# ============================================================

# Get AMD's general company information.
amd_info = amd.info

print("\nAMD information type:")
print(type(amd_info))


# Find AMD's country.
amd_country = amd_info.get(
    "country",
    "Country unavailable"
)

print("\nAMD country:")
print(amd_country)


# Find AMD's sector.
amd_sector = amd_info.get(
    "sector",
    "Sector unavailable"
)

print("\nAMD sector:")
print(amd_sector)


# ============================================================
# 8. AMD HISTORICAL PRICES
# ============================================================

# Download AMD's maximum available historical data.
amd_share_price_data = amd.history(
    period="max"
)

print("\nAMD historical data:")
print(amd_share_price_data.head())


# ============================================================
# 9. AMD FIRST-DAY VOLUME
# ============================================================

# Select the Volume column and first row.
first_volume = (
    amd_share_price_data["Volume"].iloc[0]
)

print("\nAMD volume on the first available day:")
print(first_volume)