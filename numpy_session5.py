import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine



# Task 1: 
engine = create_engine("sqlite:///data5/zomato_demo.db")

restaurants_df = pd.read_sql("restaurants", engine)
print("Task 1: 'restaurants' table - first 5 rows")
print(restaurants_df.head())

print()


# Task 2: 
query = "SELECT name, rating FROM movies WHERE rating > 8"
top_movies_df = pd.read_sql_query(query, engine)
print("Task 2: Movies with rating above 8")
print(top_movies_df)

print()

# Task 3: 
api_url = "https://jsonplaceholder.typicode.com/users"
try:
    users_api_df = pd.read_json(api_url)
except Exception as e:
    print(f"Could not reach {api_url} directly ({e.__class__.__name__}); "
          f"using a locally saved copy of the same response instead.")
    users_api_df = pd.read_json("data5/users_api_fallback.json")

print("Task 3: Usernames from the users API")
print(users_api_df["username"])

print()

# Task 4: 
data_dir = Path("data5")
orders_path = data_dir / "orders.csv"
users_path = data_dir / "users.csv"

orders_df = pd.read_csv(orders_path)
users_df = pd.read_csv(users_path)

merged_df = pd.merge(orders_df, users_df, on="user_id")
merged_df = merged_df[["order_id", "username", "amount"]]

print("Task 4: Orders merged with usernames")
print(merged_df)

print()

# Task 5: 
today_orders = pd.DataFrame({
    "order_id": [201, 202, 203],
    "item": ["Pizza", "Burger", "Pasta"],
    "price": [350, 220, 400]
})

yesterday_orders = pd.DataFrame({
    "order_id": [198, 199, 200],
    "item": ["Sushi", "Biryani", "Noodles"],
    "price": [600, 280, 250]
})

combined_orders = pd.concat([today_orders, yesterday_orders]).reset_index(drop=True)
print("Task 5: Combined today's and yesterday's orders")
print(combined_orders)
