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
total_sales = df["total_amount"].sum()

qty_sum = df.groupby("product")["quantity"].sum()
best_product_qty = qty_sum.idxmax()
best_qty = qty_sum.max()

rev_sum = df.groupby("product")["total_amount"].sum()
best_product_rev = rev_sum.idxmax()
best_rev = rev_sum.max()


print("\n===== SALES REPORT =====\n")

print(f"Total Sales: ₹{total_sales}")

print(f"\nBest Selling Product (By Quantity):")
print(f"{best_product_qty} — {best_qty} units")

print(f"\nBest Selling Product (By Revenue):")
print(f"{best_product_rev} — ₹{best_rev}")
