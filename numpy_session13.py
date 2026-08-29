import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()


# Task 1: 
tips_df = sns.load_dataset("tips")

pair_grid = sns.pairplot(tips_df)
pair_grid.fig.suptitle("Pairplot of Numeric Variables in the Tips Dataset", y=1.02)
pair_grid.savefig("tips_pairplot.png", dpi=150, bbox_inches="tight")
plt.close(pair_grid.fig)
print("Task 1: Saved tips_pairplot.png")

# Task 2:
flights_df = sns.load_dataset("flights")
flights_pivot = flights_df.pivot_table(index="month", columns="year", values="passengers")

plt.figure(figsize=(10, 6))
sns.heatmap(flights_pivot, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title("Passenger Counts by Month and Year (Flights Dataset)")
plt.xlabel("Year")
plt.ylabel("Month")
plt.savefig("flights_heatmap.png", dpi=150, bbox_inches="tight")
plt.close()
print("Task 2: Saved flights_heatmap.png")


# Task 3: 
fmri_df = sns.load_dataset("fmri")

rel_grid = sns.relplot(
    data=fmri_df, x="timepoint", y="signal",
    hue="event", kind="line", errorbar="sd"
)
rel_grid.fig.suptitle("FMRI Signal Over Time by Event Type", y=1.02)
rel_grid.savefig("fmri_relplot.png", dpi=150, bbox_inches="tight")
plt.close(rel_grid.fig)
print("Task 3: Saved fmri_relplot.png")

# Task 4: 
titanic_df = sns.load_dataset("titanic")

cat_grid = sns.catplot(
    data=titanic_df, x="class", y="survived",
    kind="bar", errorbar="ci"
)
cat_grid.fig.suptitle("Survival Rate by Passenger Class (Titanic Dataset)", y=1.02)
cat_grid.set_axis_labels("Passenger Class", "Survival Rate")
cat_grid.savefig("titanic_survival_catplot.png", dpi=150, bbox_inches="tight")
plt.close(cat_grid.fig)
print("Task 4: Saved titanic_survival_catplot.png")


# Task 5: 
penguins_df = sns.load_dataset("penguins").dropna(subset=["bill_length_mm", "flipper_length_mm"])

joint_grid = sns.jointplot(
    data=penguins_df, x="bill_length_mm", y="flipper_length_mm",
    kind="reg", color="teal"
)
joint_grid.fig.suptitle("Bill Length vs Flipper Length (Penguins Dataset)", y=1.02)
joint_grid.savefig("penguins_jointplot_reg.png", dpi=150, bbox_inches="tight")
plt.close(joint_grid.fig)
print("Task 5: Saved penguins_jointplot_reg.png")
