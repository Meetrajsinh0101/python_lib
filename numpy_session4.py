import pandas as pd

# Task 1: 

ipl_df = pd.read_csv("data/ipl_scores.csv")
print("Task 1: IPL match scores - first 5 rows")
print(ipl_df.head())

print()

# Task 2: 
songs_df = pd.read_json("data/trending_songs.json")
print("Task 2: Trending songs - column names and dtypes")
print("Columns:", list(songs_df.columns))
songs_df.info()

print()

# Task 3: 
zomato_df = pd.read_csv("data/zomato_data.tsv", sep="\t")
print("Task 3: Zomato TSV data - summary statistics")
print(zomato_df.describe(include="all"))

print()

# Task 4: 
flipkart_df = pd.read_excel("data/flipkart_products.xlsx", engine="openpyxl")
print("Task 4: Flipkart product listings - iterating in chunks of 2000 rows")
print("Total rows in file:", len(flipkart_df))

chunk_size = 2000
for start in range(0, len(flipkart_df), chunk_size):
    chunk = flipkart_df.iloc[start:start + chunk_size]
    print(f"Chunk starting at row {start}: {len(chunk)} rows")

print()

# Task 5: 
paytm_df = pd.read_csv("data/paytm_transactions.csv", sep=";")
print("Task 5: Paytm transactions - missing value check")
print(paytm_df.head())

null_counts = paytm_df.isnull().sum()
print("Null values per column:")
print(null_counts)

columns_with_nulls = null_counts[null_counts > 0]
print("Columns that have missing values:", list(columns_with_nulls.index))
