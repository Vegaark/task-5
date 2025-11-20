import pandas as pd
import matplotlib.pyplot as plt

# ===============================
#  Task 5 – Data Analysis Program
# ===============================

# 1. Load CSV File
df = pd.read_csv("sales.csv")   # Rename if your file has a different name
print("First 5 rows:")
print(df.head())

# 2. Show basic details
print("\nData Shape:", df.shape)
print("\nColumns:", df.columns)

# 3. Check missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Remove missing rows (optional)
df = df.dropna()

# 4. Group by Product and calculate total sales
sales_summary = df.groupby("Product")["Sales"].sum()
print("\nSales Summary (Total Sales per Product):")
print(sales_summary)

# 5. Plot the bar chart
sales_summary.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()
