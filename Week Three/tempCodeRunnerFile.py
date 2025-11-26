import pandas as pd

df = pd.read_csv("sales_dataset.csv")

print("First 5 Rows: \n",df.head(5))
print(" ")
print("Last 5 Rows: \n",df.tail(5))
print(" ")
print("Shape/Size of Dataset: \n",df.shape)
print(" ")
print("Columns in the Dataset: ",df.columns)
print(" ")
print("Statitics Summary: ",df.describe())
print(" ")
print("Total Sales: ",df["total_amount"].sum())
print(" ")
print("Best Selling Product: ")
qyt_sum = df.groupby("product")["quantity"].sum()
best_selling_product = 1