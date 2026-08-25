import numpy as np

# Task 1: ratings (out of 5) given by 4 users to 5 food items on Zomato
ratings = np.array([
    [4, 5, 3, 2, 4],   # user 1
    [3, 4, 5, 5, 2],   # user 2
    [2, 3, 4, 4, 5],   # user 3
    [5, 5, 4, 3, 3]    # user 4
])
print("Full ratings matrix:\n", ratings)

# slicing to get rows for 2nd and 3rd users (index 1 and 2)
user_2_3_ratings = ratings[1:3]
print("Ratings by user 2 and user 3:\n", user_2_3_ratings)

print()

# Task 2: daily steps for 10 days, select days with steps > 8000
steps = np.array([7500, 8200, 9000, 6800, 8100, 7999, 10500, 8000, 9200, 7300])
high_step_days = steps[steps > 8000]
print("Steps array:", steps)
print("Days with steps > 8000:", high_step_days)

print()

# Task 3: IPL team scores for 8 matches, fancy indexing for matches 2, 5, 7
ipl_scores = np.array([180, 165, 210, 195, 172, 205, 188, 199])
selected_matches = ipl_scores[[2, 5, 7]]
print("IPL scores:", ipl_scores)
print("Scores from matches 2, 5, 7:", selected_matches)

print()

# Task 4: Flipkart product prices, apply 10% discount using broadcasting (no loops)
prices = np.array([999, 1499, 2499, 599, 3999])
discounted_prices = prices * 0.9
print("Original prices:", prices)
print("Prices after 10% discount:", discounted_prices)

print()

# Task 5: Spotify song ratings, set negative ratings to zero using boolean masking
song_ratings = np.array([3, -2, 5, 0, -4, 1, -1, 4])
song_ratings[song_ratings < 0] = 0
print("Song ratings after masking negatives to zero:", song_ratings)
