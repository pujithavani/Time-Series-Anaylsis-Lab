# -*- coding: utf-8 -*-
"""exp 4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jpKILkIpkHag4YTJjkD_QyxIRwAqVQKW
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

# Load the dataset
file_path = "/content/108,110.csv"
df = pd.read_csv(file_path)

# Rename columns for clarity
df.columns = ['Date', 'Value']

# Convert Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m')

# Set Date as index
df.set_index('Date', inplace=True)
df.sort_index(inplace=True)

# Plot the time series
plt.figure(figsize=(10, 5))
plt.plot(df['Value'], label='Original Time Series', color='blue')
plt.title('Original Time Series')
plt.legend()
plt.show()

# Function to check stationarity
def check_stationarity(series):
    result = adfuller(series.dropna())
    print("ADF Statistic:", result[0])
    print("p-value:", result[1])
    print("Critical Values:")
    for key, value in result[4].items():
        print(f"   {key}: {value}")
    if result[1] <= 0.05:
        print("Conclusion: The time series is stationary.")
    else:
        print("Conclusion: The time series is NOT stationary.")

# Apply stationarity test
check_stationarity(df['Value'])