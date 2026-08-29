import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(5)


# Task 1: 
delivery_times = np.random.normal(35, 8, 50)   # minutes
delivery_times = np.clip(delivery_times, 10, None)

plt.figure(figsize=(8, 5))
sns.histplot(delivery_times, bins=10, color="tab:orange")
plt.title("Distribution of Zomato Delivery Times (50 Orders)")
plt.xlabel("Delivery Time (minutes)")
plt.ylabel("Count")
plt.savefig("zomato_delivery_histplot.png", dpi=150, bbox_inches="tight")
plt.close()
print("Task 1: Saved zomato_delivery_histplot.png")


# Task 2: 
tips_df = sns.load_dataset("tips")

plt.figure(figsize=(8, 5))
sns.boxplot(data=tips_df, x="day", y="total_bill")
plt.title("Total Bill Amount by Day of the Week (tips dataset)")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.savefig("tips_total_bill_boxplot.png", dpi=150, bbox_inches="tight")
plt.close()
print("Task 2: Saved tips_total_bill_boxplot.png")

# Task 3: 
sns.set_theme(style="darkgrid")

teams = [f"Team {letter}" for letter in "ABCDEFGH"]
records = []
for team in teams:
    mean_score = np.random.randint(150, 200)
    scores = np.random.normal(mean_score, 20, 15)   # 15 matches per team
    for score in scores:
        records.append({"team": team, "runs": max(score, 60)})

ipl_scores_df = pd.DataFrame(records)

plt.figure(figsize=(10, 6))
sns.violinplot(data=ipl_scores_df, x="team", y="runs")
plt.title("IPL Run Distribution by Team")
plt.xlabel("Team")
plt.ylabel("Runs")
plt.savefig("ipl_runs_violinplot.png", dpi=150, bbox_inches="tight")
plt.close()
print("Task 3: Saved ipl_runs_violinplot.png")

sns.set_theme()   # reset theme before the next plots

# Task 4: 
genres = ["Pop", "Hip-Hop", "Bollywood", "Rock", "Indie"]
track_genres = np.random.choice(genres, size=40, p=[0.3, 0.25, 0.25, 0.1, 0.1])
spotify_tracks_df = pd.DataFrame({"genre": track_genres})

plt.figure(figsize=(8, 5))
sns.countplot(data=spotify_tracks_df, x="genre", order=genres)
plt.title("Number of Songs per Genre (40 Spotify Tracks)")
plt.xlabel("Genre")
plt.ylabel("Number of Songs")
plt.savefig("spotify_genre_countplot.png", dpi=150, bbox_inches="tight")
plt.close()
print("Task 4: Saved spotify_genre_countplot.png")

# Task 5: 
sns.set_theme(style="whitegrid")

daily_steps = np.random.normal(8000, 1500, 7)
daily_steps = np.clip(daily_steps, 3000, None)

plt.figure(figsize=(8, 5))
sns.kdeplot(daily_steps, color="tab:green", fill=True)
plt.title("KDE of Daily Step Counts (1 Week)")
plt.xlabel("Steps")
plt.ylabel("Density")
plt.savefig("daily_steps_kdeplot.png", dpi=150, bbox_inches="tight")
plt.close()
print("Task 5: Saved daily_steps_kdeplot.png")
