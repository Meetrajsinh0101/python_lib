import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

# Task 1: 
ipl_df = pd.read_csv("data14/ipl_matches.csv")

print("Task 1: Univariate analysis of 'total_runs'")
print("Mean:", ipl_df["total_runs"].mean())
print("Median:", ipl_df["total_runs"].median())
print("Min:", ipl_df["total_runs"].min())
print("Max:", ipl_df["total_runs"].max())
print("Std Dev:", ipl_df["total_runs"].std())
print()
print("Full describe() for reference:")
print(ipl_df["total_runs"].describe())

print()

# Task 2: 
flipkart_df = pd.read_csv("data14/flipkart_reviews.csv")

plt.figure(figsize=(7, 5))
sns.countplot(data=flipkart_df, x="rating", order=[1, 2, 3, 4, 5], color="tab:blue")
plt.title("Number of Flipkart Reviews per Rating")
plt.xlabel("Rating (stars)")
plt.ylabel("Number of Reviews")
plt.savefig("flipkart_rating_countplot.png", dpi=150, bbox_inches="tight")
plt.close()
print("Task 2: Saved flipkart_rating_countplot.png")

print()

# Task 3: 
zomato_df = pd.read_csv("data14/zomato_listings.csv")

plt.figure(figsize=(8, 5))
sns.scatterplot(data=zomato_df, x="average_cost_for_two", y="user_rating", color="tab:red")
plt.title("Average Cost for Two vs User Rating (Zomato)")
plt.xlabel("Average Cost for Two (₹)")
plt.ylabel("User Rating")
plt.savefig("zomato_cost_vs_rating_scatter.png", dpi=150, bbox_inches="tight")
plt.close()
print("Task 3: Saved zomato_cost_vs_rating_scatter.png")
print("Correlation between cost and rating:", zomato_df["average_cost_for_two"].corr(zomato_df["user_rating"]))

print()

# Task 4: 
bms_df = pd.read_csv("data14/bookmyshow_movies.csv")

genre_avg_collection = (
    bms_df.groupby("genre")["box_office_collection"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

print("Task 4: Average box office collection by genre (sorted, ₹ Crores)")
print(genre_avg_collection)

print()


# Task 5: 
spotify_df = pd.read_csv("data14/spotify_songs.csv")

feature_cols = ["danceability", "energy", "valence", "popularity"]
pair_grid = sns.pairplot(spotify_df[feature_cols])
pair_grid.fig.suptitle("Pairwise Relationships - Spotify Song Features", y=1.02)
pair_grid.savefig("spotify_features_pairplot.png", dpi=150, bbox_inches="tight")
plt.close(pair_grid.fig)
print("Task 5: Saved spotify_features_pairplot.png")


observation = """
Observation: 'popularity' shows a visibly positive relationship with both
'danceability' and 'energy' in the scatter panels - songs with higher
danceability and energy tend to cluster toward higher popularity scores.
'valence' (musical positivity), on the other hand, looks much more spread
out against popularity, suggesting mood/positivity alone isn't a strong
driver of popularity in this dataset - rhythm and intensity matter more.
"""
print(observation)
