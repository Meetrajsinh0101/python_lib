import pandas as pd
import numpy as np


# Task 1: 
delivery_timestamps = ['2024-06-01 14:30', '2024-06-02 09:15', '2024-06-03 20:45']
delivery_datetimes = pd.to_datetime(delivery_timestamps)

print("Task 1: Delivery timestamps converted to datetime")
print(delivery_datetimes)

print()

# Task 2: 
flipkart_df = pd.read_csv("data9/flipkart_order_history.csv")
flipkart_df["order_date"] = pd.to_datetime(flipkart_df["order_date"])

flipkart_df["order_year"] = flipkart_df["order_date"].dt.year
flipkart_df["order_month"] = flipkart_df["order_date"].dt.month
flipkart_df["order_weekday"] = flipkart_df["order_date"].dt.day_name()

print("Task 2: Flipkart orders with year, month, weekday columns")
print(flipkart_df.head())

print()

# Task 3: 
flipkart_indexed_df = flipkart_df.set_index("order_date").sort_index()
weekly_order_counts = flipkart_indexed_df.resample("W").size()

print("Task 3: Total orders placed each week")
print(weekly_order_counts)

print()


# Task 4:
insta_df = pd.read_csv("data9/instagram_posts.csv")
insta_df["posted_at"] = pd.to_datetime(insta_df["posted_at"])  

insta_df["posted_at_ist"] = insta_df["posted_at"].dt.tz_convert("Asia/Kolkata")

print("Task 4: Instagram post times converted to Asia/Kolkata (first 5)")
print(insta_df[["post_id", "posted_at", "posted_at_ist"]].head())

print()

# Task 5: 
# dt.dayofweek: Monday=0 ... Sunday=6, so Saturday=5 and Sunday=6
flipkart_df["is_weekend"] = np.where(flipkart_df["order_date"].dt.dayofweek >= 5, True, False)

print("Task 5: 'is_weekend' feature added")
print(flipkart_df[["order_date", "order_weekday", "is_weekend"]].head(10))
