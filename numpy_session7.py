import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Task 1: 
zomato_df = pd.read_csv("data7/zomato_ratings.csv")

Q1 = zomato_df["user_rating"].quantile(0.25)
Q3 = zomato_df["user_rating"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outlier_mask = (zomato_df["user_rating"] < lower_bound) | (zomato_df["user_rating"] > upper_bound)
outlier_indices = zomato_df[outlier_mask].index.tolist()

print("Task 1: Outlier detection using IQR method")
print(f"Q1={Q1}, Q3={Q3}, IQR={IQR}, bounds=({lower_bound:.2f}, {upper_bound:.2f})")
print("Indices of detected outliers:", outlier_indices)
print(zomato_df.loc[outlier_indices])

print()

# Task 2: 
swiggy_df = pd.read_csv("data7/swiggy_orders.csv")

plt.figure(figsize=(6, 5))
plt.boxplot(swiggy_df["order_amount"], vert=True)
plt.title("Swiggy Order Amounts - Boxplot")
plt.ylabel("Order Amount (₹)")
plt.xticks([1], ["order_amount"])
plt.savefig("swiggy_order_amount_boxplot.png", dpi=150, bbox_inches="tight")
plt.close()

print("Task 2: Boxplot saved as 'swiggy_order_amount_boxplot.png'")
print("Points above the top whisker (visually the dots) are the outliers - "
      "in this dataset that corresponds to the unusually large orders around "
      f"{swiggy_df['order_amount'].max():.0f}.")

print()

# Task 3: 
paytm_df = pd.read_csv("data7/paytm_amounts.csv")

print("Task 3: Winsorizing 'transaction_amount'")
print("Stats before winsorization:")
print(paytm_df["transaction_amount"].describe())

lower_cap = paytm_df["transaction_amount"].quantile(0.05)
upper_cap = paytm_df["transaction_amount"].quantile(0.95)

paytm_df["transaction_amount_winsorized"] = paytm_df["transaction_amount"].clip(
    lower=lower_cap, upper=upper_cap
)

print(f"5th percentile: {lower_cap:.2f}, 95th percentile: {upper_cap:.2f}")
print("Stats after winsorization:")
print(paytm_df["transaction_amount_winsorized"].describe())

print()

# Task 4: 
flipkart_df = pd.read_csv("data7/flipkart_prices.csv")

print("Task 4: Flipkart prices before conversion")
print(flipkart_df)
print("dtype before:", flipkart_df["price"].dtype)

flipkart_df["price"] = (
    flipkart_df["price"]
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

print("Flipkart prices after conversion")
print(flipkart_df)
print("dtype after:", flipkart_df["price"].dtype)

print()

# Task 5: 
spotify_df = pd.read_csv("data7/spotify_users.csv")

print("Task 5: 'is_premium' column before cleanup")
print(spotify_df)
print("Unique raw values:", spotify_df["is_premium"].unique())

true_values = {"true", "1", "yes"}   


def normalize_to_bool(value):
    return str(value).strip().lower() in true_values


spotify_df["is_premium"] = spotify_df["is_premium"].apply(normalize_to_bool)

print("'is_premium' column after cleanup")
print(spotify_df)
print("dtype after:", spotify_df["is_premium"].dtype)
