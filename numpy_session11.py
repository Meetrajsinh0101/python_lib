import matplotlib.pyplot as plt


# Task 1: 
fig1, axes1 = plt.subplots(2, 2, figsize=(10, 8))


days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperatures = [30, 32, 29, 31, 33]
axes1[0, 0].plot(days, temperatures, marker="o", color="tab:blue")
axes1[0, 0].set_title("Line: Daily Temperature")
axes1[0, 0].set_xlabel("Day")
axes1[0, 0].set_ylabel("Temp (°C)")


fruits = ["Apple", "Banana", "Mango", "Grapes"]
fruit_sales = [40, 55, 30, 25]
axes1[0, 1].bar(fruits, fruit_sales, color="tab:green")
axes1[0, 1].set_title("Bar: Fruit Sales")
axes1[0, 1].set_xlabel("Fruit")
axes1[0, 1].set_ylabel("Units Sold")

study_hours = [1, 2, 3, 4, 5, 6, 7]
exam_scores = [50, 55, 65, 70, 78, 85, 90]
axes1[1, 0].scatter(study_hours, exam_scores, color="tab:orange")
axes1[1, 0].set_title("Scatter: Study Hours vs Score")
axes1[1, 0].set_xlabel("Study Hours")
axes1[1, 0].set_ylabel("Exam Score")

expense_categories = ["Rent", "Food", "Travel", "Savings"]
expense_share = [40, 25, 15, 20]
axes1[1, 1].pie(expense_share, labels=expense_categories, autopct="%1.0f%%")
axes1[1, 1].set_title("Pie: Monthly Expense Split")

fig1.tight_layout()
fig1.savefig("subplots_2x2_grid.png", dpi=150, bbox_inches="tight")
plt.close(fig1)
print("Task 1: Saved subplots_2x2_grid.png")

# Task 2: 
platforms = ["Zomato", "Swiggy", "Domino's"]
avg_delivery_minutes = [38, 32, 25]
bar_colors = ["tab:red", "tab:orange", "tab:blue"]
edge_styles = ["solid", "dashed", "dotted"]
edge_widths = [2, 3, 2.5]

fig2, ax2 = plt.subplots(figsize=(7, 5))
for i, (platform, minutes, color, style, width) in enumerate(
    zip(platforms, avg_delivery_minutes, bar_colors, edge_styles, edge_widths)
):
    ax2.bar(platform, minutes, color=color, edgecolor="black",
            linestyle=style, linewidth=width)

ax2.set_title("Average Delivery Time by Platform")
ax2.set_xlabel("Platform")
ax2.set_ylabel("Average Delivery Time (minutes)")
fig2.savefig("delivery_time_styled_bar.png", dpi=150, bbox_inches="tight")
plt.close(fig2)
print("Task 2: Saved delivery_time_styled_bar.png")

# Task 3: 
influencers = ["Inf A", "Inf B", "Inf C", "Inf D", "Inf E"]
followers_millions = [2.5, 5.1, 1.2, 8.7, 3.9]
avg_daily_posts = [1.2, 0.8, 2.5, 0.5, 1.8]

fig3, ax3_left = plt.subplots(figsize=(8, 5))
ax3_left.plot(influencers, followers_millions, color="tab:blue", marker="o", label="Followers (M)")
ax3_left.set_xlabel("Influencer")
ax3_left.set_ylabel("Followers (Millions)", color="tab:blue")
ax3_left.tick_params(axis="y", labelcolor="tab:blue")

ax3_right = ax3_left.twinx()
ax3_right.plot(influencers, avg_daily_posts, color="tab:red", marker="s", label="Avg Daily Posts")
ax3_right.set_ylabel("Average Daily Posts", color="tab:red")
ax3_right.tick_params(axis="y", labelcolor="tab:red")

fig3.suptitle("Instagram Followers vs Average Daily Posts")
fig3.tight_layout()
fig3.savefig("followers_vs_posts_dualaxis.png", dpi=150, bbox_inches="tight")
plt.close(fig3)
print("Task 3: Saved followers_vs_posts_dualaxis.png")

# Task 4: 
movie_names = ["Movie Alpha", "Movie Beta", "Movie Gamma", "Movie Delta", "Movie Epsilon"]
tickets_sold_lakhs = [12, 25, 8, 30, 18]
imdb_ratings = [6.5, 8.1, 5.9, 8.7, 7.2]

fig4, ax4 = plt.subplots(figsize=(9, 6))
ax4.scatter(tickets_sold_lakhs, imdb_ratings, color="tab:purple", s=80)

for name, tickets, rating in zip(movie_names, tickets_sold_lakhs, imdb_ratings):
    ax4.annotate(name, (tickets, rating), textcoords="offset points",
                 xytext=(0, 10), ha="center", fontsize=9)

ax4.set_title("Tickets Sold vs IMDB Rating")
ax4.set_xlabel("Tickets Sold (Lakhs)")
ax4.set_ylabel("IMDB Rating")
fig4.savefig("movies_tickets_vs_rating_scatter.png", dpi=150, bbox_inches="tight")
plt.close(fig4)
print("Task 4: Saved movies_tickets_vs_rating_scatter.png")


# Task 5: 
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
monthly_sales_crores = [45, 42, 48, 50, 47, 53, 55, 58, 60, 210, 90, 65]

fig5, ax5 = plt.subplots(figsize=(10, 6))
ax5.plot(months, monthly_sales_crores, marker="o", color="tab:blue")

peak_index = monthly_sales_crores.index(max(monthly_sales_crores))
peak_month = months[peak_index]
peak_value = monthly_sales_crores[peak_index]

ax5.annotate(
    "Big Billion Days",
    xy=(peak_month, peak_value),
    xytext=(peak_index - 2, peak_value + 30),
    arrowprops=dict(facecolor="black", arrowstyle="->"),
    fontsize=10,
    fontweight="bold"
)

ax5.set_title("Flipkart Monthly Sales")
ax5.set_xlabel("Month")
ax5.set_ylabel("Sales (₹ Crores)")
fig5.savefig("flipkart_monthly_sales_annotated.png", dpi=150, bbox_inches="tight")
plt.close(fig5)
print("Task 5: Saved flipkart_monthly_sales_annotated.png")
