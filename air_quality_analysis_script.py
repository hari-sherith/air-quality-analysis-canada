
# Air Quality CO Analysis – Canada 2023

# This notebook analyzes ambient carbon monoxide (CO) pollution levels across Canadian regions using 2023 data from the National Air Pollution Surveillance (NAPS) Program.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("air_quality_co_2023.csv")

# Define the monthly columns
monthly_columns = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# National Monthly CO Trend
monthly_avg = df[monthly_columns].mean()

plt.figure(figsize=(10, 5))
sns.lineplot(data=monthly_avg, marker='o')
plt.title("National Average CO Levels by Month (2023)")
plt.ylabel("CO (ppm)")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Top 10 Most Polluted Regions
top_regions = df.sort_values("Mean", ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(y="Region", x="Mean", data=top_regions, palette="Reds_r")
plt.title("Top 10 Most Polluted Regions by Annual CO Mean (2023)")
plt.xlabel("CO (ppm)")
plt.ylabel("Region")
plt.tight_layout()
plt.show()

# Summary Statistics
print("National CO Mean:", df["Mean"].mean().round(3), "ppm")
print("Highest CO Mean:", df["Mean"].max().round(3), "ppm")
print("Lowest CO Mean:", df["Mean"].min().round(3), "ppm")
