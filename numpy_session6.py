import pandas as pd


# Task 1: 
ipl_df = pd.read_csv("data6/ipl_player_stats.csv")
print("Task 1: IPL player stats - raw data")
print(ipl_df)
print()
print("Missing values per column (isnull().sum()):")
print(ipl_df.isnull().sum())
print()
print("Non-missing values per column (notnull().sum()):")
print(ipl_df.notnull().sum())

print()

# Task 2: 
print("Task 2: Dropping rows with any missing data")
print("Shape before dropping:", ipl_df.shape)

ipl_dropped_df = ipl_df.dropna(axis=0, how="any")
print("Shape after dropping:", ipl_dropped_df.shape)
print(ipl_dropped_df)

print()

# Task 3:
ipl_filled_df = ipl_df.copy()
runs_mean = ipl_filled_df["runs"].mean()
ipl_filled_df["runs"] = ipl_filled_df["runs"].fillna(runs_mean)

print("Task 3: 'runs' column after filling missing values with the mean")
print(f"Mean of 'runs' (excluding NaNs): {runs_mean:.2f}")
print(ipl_filled_df["runs"])

print()

# Task 4: 
zomato_ratings_df = pd.DataFrame({
    "restaurant_name": ["Spice Villa", "Curry House", "Pizza Point", "Sushi Zen",
                          "Burger Hub", "Biryani Palace", "Tandoori Nights"],
    "rating": [4.2, None, None, 4.0, None, 4.7, None]
})

print("Task 4: Zomato ratings - before filling")
print(zomato_ratings_df)

zomato_filled_df = zomato_ratings_df.copy()
zomato_filled_df["rating"] = zomato_filled_df["rating"].ffill()   
zomato_filled_df["rating"] = zomato_filled_df["rating"].bfill()   
print("Zomato ratings - after ffill then bfill")
print(zomato_filled_df)

print()

# Task 5: 
explanation = """
Task 5: Missingness mechanism for the 'strike_rate' column

The 'strike_rate' values are missing mostly for bowlers (Jasprit Bumrah,
Mohammed Shami, Yuzvendra Chahal) rather than being scattered randomly
across all players. Strike rate is a batting metric, so it tends to go
unrecorded or be less meaningful specifically for players whose primary
role is bowling. This makes the missingness dependent on another observed
variable in the dataset (the player's role/batting involvement), which
points to MAR (Missing At Random) rather than MCAR - the "randomness" is
conditional on player type, not truly independent of the data.
"""
print(explanation)
