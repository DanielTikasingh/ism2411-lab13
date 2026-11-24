"""
# ISM2411 Lab 13 — First DataFrame — Retail Sales Explorer
Name: [Daniel Tikasingh]
Command to run: python explore.py

--- SELF-ASSESSMENT REFLECTION ANSWERS ---

1. Without looking at your code, can you explain what a boolean filter does in plain English?
   A boolean filter evaluates a given condition row by row, generating a series of True and False 
   values. Pandas then applies this mask to the DataFrame, keeping only the rows where 
   the condition evaluates to True and dropping the rest.

2. What is the difference between df["revenue"] and df[["revenue"]]? When does the distinction matter?
   - df["revenue"] extracts a single column and returns a pandas Series.
   - df[["revenue"]] extracts columns using a list and returns a pandas DataFrame.
   The distinction matters when passing data into functions, machine learning models, or plotting 
   libraries that specifically expect a 2D table structure rather than a 1D Series.

3. If a colleague who only knows Excel asked you to explain why you would choose pandas for this task, what is the single most compelling reason you would give?
   Automation, reproducibility, and scalability. Pandas allows you to process thousands or millions 
   of rows instantly with clean, scriptable code, whereas Excel requires manual clicking and can 
   slow down, freeze, or corrupt when handling large datasets.
"""

import pandas as pd

# EXERCISE 1: Load it

print("=== EXERCISE 1: Load it ===")
df = pd.read_csv('data/retail_sales.csv')
print("First 5 rows (.head()):")
print(df.head())
print("\nShape:", df.shape)
print("Columns:", df.columns.tolist())
print("Data Types:\n", df.dtypes)


# EXERCISE 2: Filter by region

print("\n=== EXERCISE 2: Filter by region ===")
south = df[df['region'] == 'South']
print(f"Total rows in South region: {len(south)}")
print("South region head:")
print(south.head())


# EXERCISE 3: Top 5 by revenue

print("\n=== EXERCISE 3: Top 5 by revenue ===")
top_revenue = df.sort_values('revenue', ascending=False).head(5)
print(top_revenue)
print("\n(Note: The index values above are preserved from the original DataFrame and are not 0-4 because the index was not reset.)")


# EXERCISE 4: Two-condition filter

print("\n=== EXERCISE 4: Two-condition filter ===")
big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]
print(f"Total rows matching both conditions: {len(big_south)}")
print("Big South head:")
print(big_south.head())


# EXERCISE 5: A new column

print("\n=== EXERCISE 5: A new column ===")
df['per_unit'] = df['revenue'] / df['quantity']
print("Updated DataFrame head:")
print(df.head())
mean_per_unit = df['per_unit'].mean()
print(f"Mean per-unit price across all rows: {mean_per_unit:.2f}")


# EXERCISE 6: Unique values

print("\n=== EXERCISE 6: Unique values ===")
print("Unique regions:", df['region'].unique())
print("\nRegion value counts:\n", df['region'].value_counts())


# EXERCISE 7: Select columns

print("\n=== EXERCISE 7: Select columns ===")
subset = df[['region', 'product', 'revenue']]
print("Subset shape:", subset.shape)
print("Subset head:")
print(subset.head())


# EXERCISE 8: Save

print("\n=== EXERCISE 8: Save ===")
df.to_csv('data/explored.csv', index=False)
print("Successfully saved updated DataFrame to 'data/explored.csv'.")