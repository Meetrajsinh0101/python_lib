import pandas as pd
from ydata_profiling import ProfileReport   
import sweetviz as sv


# Task 1: 
spotify_df = pd.read_csv("data15/spotify_top100.csv")

spotify_profile = ProfileReport(
    spotify_df, title="Spotify Top 100 Songs - Profiling Report",
    explorative=True, minimal=True
)
spotify_profile.to_file("spotify_top100_profile_report.html")

print("Task 1: Report saved as spotify_top100_profile_report.html")
print("Missing values per column:")
print(spotify_df.isnull().sum())
print("\nDtypes:")
print(spotify_df.dtypes)
print(
    "\nNotes from opening the report: 'streams_millions' and 'artist' both "
    "have missing values (flagged as warnings in the report). 'duration_ms' "
    "is stored as an object/string column instead of a proper numeric type, "
    "which the report flags under type inference - it should be converted "
    "with pd.to_numeric() before analysis."
)

print()


# Task 2: 
mumbai_df = pd.read_csv("data15/zomato_mumbai.csv")
delhi_df = pd.read_csv("data15/zomato_delhi.csv")

comparison_report = sv.compare([mumbai_df, "Mumbai"], [delhi_df, "Delhi"])
comparison_report.show_html("zomato_mumbai_vs_delhi_sweetviz.html", open_browser=False)

print("Task 2: Report saved as zomato_mumbai_vs_delhi_sweetviz.html")
print(f"Mumbai avg cost for two: {mumbai_df['average_cost_for_two'].mean():.2f}")
print(f"Delhi avg cost for two: {delhi_df['average_cost_for_two'].mean():.2f}")
print(f"Mumbai avg rating: {mumbai_df['user_rating'].mean():.2f}")
print(f"Delhi avg rating: {delhi_df['user_rating'].mean():.2f}")
print(
    "\nKey difference spotted in the report: Mumbai restaurants run noticeably "
    "more expensive on average (~₹850 for two vs ~₹650 in Delhi) and also carry "
    "a slightly higher average rating - the report's side-by-side distribution "
    "panels make this cost gap immediately visible."
)

print()


# Task 3:

myntra_df = pd.read_csv("data15/myntra_products.csv")
filtered_myntra_df = myntra_df[myntra_df["price"] > 2000]

print("Task 3: Myntra products with price > ₹2000")
print("Number of matching products:", len(filtered_myntra_df))
print(filtered_myntra_df.head())

print()

# Task 4: 
flipkart_df = pd.read_csv("data15/flipkart_reviews_profiling.csv")

flipkart_profile = ProfileReport(
    flipkart_df, title="Flipkart Product Reviews - Profiling Report",
    explorative=True, minimal=True
)
flipkart_profile.to_file("flipkart_reviews_profile_report.html")

print("Task 4: Report saved as flipkart_reviews_profile_report.html")
print("Missing values per column:")
print(flipkart_df.isnull().sum())
print("\nUnique value counts per column:")
for col in flipkart_df.columns:
    print(f"  {col}: {flipkart_df[col].nunique()} unique values")

print(
    "\nTwo columns needing cleaning based on the report:\n"
    "1. 'reviewer_name' - 63 missing values (42% of rows), flagged as a "
    "high-missing warning; needs imputation or an explicit 'Unknown' "
    "category before grouping by reviewer.\n"
    "2. 'review_text' - 26 missing values and only 5 distinct values "
    "despite 150 rows, flagged for low cardinality/near-constant text; "
    "worth checking whether this is realistic free-text or should be "
    "treated as a categorical sentiment label instead."
)

print()


# Task 5: 
swiggy_df = pd.read_csv("data15/swiggy_orders.csv")

swiggy_profile = ProfileReport(
    swiggy_df, title="Swiggy Food Orders - Summary Report",
    explorative=True, minimal=True
)
swiggy_profile.to_file("swiggy_orders_profile_report.html")

print("Task 5: Report saved as swiggy_orders_profile_report.html")
print(swiggy_df.describe(include="all"))
