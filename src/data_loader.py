import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings('ignore')

file_path = r"C:\Users\neba\Desktop\brent_oil\data\raw\BrentOilPrices_Yearly.csv"
df = pd.read_csv(file_path)

# Display basic information about the dataset
print("Data overview:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())
print("\nBasic statistics:")
print(df.describe())