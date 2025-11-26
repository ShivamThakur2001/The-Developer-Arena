import pandas as pd

# Loading dataset
df = pd.read_csv("student_academic.csv") 

# Top 5 and last 5
print("First Five and Last Five Records: ")
print(df.head(5))
print("*******************************")
print(df.tail(5))

# Basic information
print("Basic information of dataset: ")
print("Rows count: ",df.shape[0])
print("Column count: ",df.shape[0])
print("Data Types Of Columns: ",df.dtypes,"\n")

# checking null values
print("Checking null values: ", df.isnull().sum())

# handling missing value 
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].mean())

# Check after Handling missing values
print("\nChecking null values After handling missing values: ", df.isnull().sum())

# Average of numrical values
print("\nAverage values:")
print(df.select_dtypes(include='number').mean())

# Highest of numrical Value
print("\nHighest values:")
print(df.select_dtypes(include='number').max())

# Lowest of numrical value
print("\nLowest values:")
print(df.select_dtypes(include='number').min())