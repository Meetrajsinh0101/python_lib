import pandas as pd

# Task 1: 
zomato_orders_df = pd.read_csv("data8/zomato_order_history.csv")

print("Task 1: Zomato order history")
print(zomato_orders_df)

duplicate_mask = zomato_orders_df.duplicated(subset=["restaurant_name", "order_date"], keep=False)
duplicate_orders = zomato_orders_df[duplicate_mask]

print("\nDuplicate orders (same restaurant + same date):")
print(duplicate_orders)

print()

# Task 2: 
flipkart_reviews = [
    "Great product, works as expected",
    "Value for money",
    "Great product, works as expected",
    "Delivery was late",
    "Value for money",
    "Great product, works as expected",
    "Not satisfied with the quality",
    "Value for money",
    "Excellent build quality",
    "Delivery was late",
    "Great product, works as expected",
]
reviews_series = pd.Series(flipkart_reviews)

review_counts = reviews_series.value_counts()
print("Task 2: Review text frequency counts")
print(review_counts)

print("\nTop 3 most common (repeated) reviews:")
print(review_counts.head(3))

print()


# Task 3: 
spotify_playlists_df = pd.DataFrame({
    "playlist_name": ["Chill Vibes", "Workout Mix", "Chill Vibes", "Road Trip",
                        "Workout Mix", "Study Beats", "Road Trip"],
    "creator_username": ["priya_s", "aman_v", "priya_s", "rahul_k",
                           "aman_v", "neha_p", "rahul_k"]
})

print("Task 3: Spotify playlists before removing duplicates")
print(spotify_playlists_df)

spotify_playlists_clean_df = spotify_playlists_df.drop_duplicates()
print("\nSpotify playlists after drop_duplicates()")
print(spotify_playlists_clean_df)

print()


# Task 4: 
instagram_usernames_df = pd.DataFrame({
    "username": ["insta_queen", "insta-queen", "instaqueen", "InstaQueen",
                  "insta.queen", "insta_queen_official"]
})

print("Task 4: Instagram usernames before standardizing")
print(instagram_usernames_df)

variant_map = {
    "insta_queen": "instaqueen",
    "insta-queen": "instaqueen",
    "InstaQueen": "instaqueen",
    "insta.queen": "instaqueen",
}
instagram_usernames_df["username"] = instagram_usernames_df["username"].replace(variant_map)

print("\nInstagram usernames after standardizing common variants")
print(instagram_usernames_df)


print()

# Task 5: 
paytm_status_df = pd.DataFrame({
    "transaction_id": [f"TXN{3000+i}" for i in range(8)],
    "payment_status": ["Yes", " yes", "Y", "No ", "no", "N", " Yes ", "NO"]
})

print("Task 5: Paytm payment status before cleanup")
print(paytm_status_df)

cleaned_status = paytm_status_df["payment_status"].str.strip().str.lower()

paid_values = {"yes", "y"}
unpaid_values = {"no", "n"}

paytm_status_df["payment_status_unified"] = cleaned_status.map(
    lambda status: 1 if status in paid_values else (0 if status in unpaid_values else pd.NA)
)

print("\nPaytm payment status after unifying (1 = paid, 0 = unpaid)")
print(paytm_status_df)
