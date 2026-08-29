import matplotlib.pyplot as plt


# Task 1: 
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
daily_steps = [7200, 8500, 6100, 9300, 7800, 10500, 6900]

plt.figure(figsize=(8, 5))
plt.plot(days, daily_steps, marker="o", color="tab:blue")
plt.title("Daily Steps - Last 7 Days")
plt.xlabel("Day")
plt.ylabel("Steps")
plt.grid(True, alpha=0.3)
plt.savefig("steps_lineplot.png", dpi=150, bbox_inches="tight")
plt.close()
print("Task 1: Saved steps_lineplot.png")

# Task 2:
restaurant_ratings = [4.2, 3.8, 4.5, 4.0, 3.5, 4.7, 4.1, 3.9, 4.3, 4.6]
avg_meal_price = [350, 280, 550, 400, 220, 650, 380, 300, 420, 600]

plt.figure(figsize=(8, 5))
plt.scatter(restaurant_ratings, avg_meal_price, color="tab:orange")
plt.title("Zomato Rating vs Average Meal Price")
plt.xlabel("Zomato Rating")
plt.ylabel("Average Meal Price (₹)")
plt.grid(True, alpha=0.3)
plt.savefig("zomato_rating_vs_price_scatter.png", dpi=150, bbox_inches="tight")
plt.close()
print("Task 2: Saved zomato_rating_vs_price_scatter.png")


# Task 3: 
platforms = ["Swiggy", "Zomato", "Domino's"]
order_counts = [12, 9, 5]
bar_colors = ["tab:orange", "tab:red", "tab:blue"]

plt.figure(figsize=(7, 5))
bars = plt.bar(platforms, order_counts, color=bar_colors, label=platforms)
plt.title("Orders Placed Last Month by Platform")
plt.xlabel("Platform")
plt.ylabel("Number of Orders")
plt.legend(bars, platforms, title="Platform")
plt.savefig("orders_by_platform_bar.png", dpi=150, bbox_inches="tight")
plt.close()
print("Task 3: Saved orders_by_platform_bar.png")

# Task 4: 
session_durations = [35, 42, 20, 55, 60, 15, 48, 33, 27, 50,
                       62, 18, 45, 39, 30, 58, 22, 41, 36, 25]

plt.figure(figsize=(8, 5))
plt.hist(session_durations, bins=5, color="tab:green", edgecolor="black")
plt.title("Spotify Listening Session Durations (Last 20 Sessions)")
plt.xlabel("Duration (minutes)")
plt.ylabel("Frequency")
plt.savefig("spotify_sessions_histogram.png", dpi=150, bbox_inches="tight")
plt.close()
print("Task 4: Saved spotify_sessions_histogram.png")

# Task 5: 
screen_time_minutes = [90, 120, 75, 140, 100, 160, 130]
posts_liked = [15, 22, 10, 28, 18, 35, 25]

fig, axes = plt.subplots(2, 1, figsize=(8, 9))

axes[0].plot(days, screen_time_minutes, marker="o", color="tab:purple")
axes[0].set_title("Daily Instagram Screen Time")
axes[0].set_xlabel("Day")
axes[0].set_ylabel("Screen Time (minutes)")
axes[0].grid(True, alpha=0.3)

axes[1].bar(days, posts_liked, color="tab:pink")
axes[1].set_title("Posts Liked Each Day")
axes[1].set_xlabel("Day")
axes[1].set_ylabel("Number of Likes")

fig.suptitle("Weekly Instagram Usage Summary")
fig.tight_layout()
fig.savefig("social_media_usage.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Task 5: Saved social_media_usage.png")
