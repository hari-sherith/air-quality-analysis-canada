
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Air Quality CO Dashboard", layout="wide")

st.title("🇨🇦 Canadian Air Quality CO Analysis – 2023")
st.markdown("This dashboard visualizes carbon monoxide (CO) pollution levels across Canadian regions using data from the NAPS program.")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("Dataset/air_quality_co_2023.csv")

df = load_data()

# Sidebar filters
regions = df["Region"].unique()
selected_regions = st.sidebar.multiselect("Select Region(s)", options=regions, default=list(regions))

df_filtered = df[df["Region"].isin(selected_regions)]

# Plot 1: National/Regional Monthly CO Trend
monthly_cols = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

st.subheader("📈 Monthly CO Trend")
monthly_avg = df_filtered[monthly_cols].mean()

fig, ax = plt.subplots(figsize=(10, 4))
sns.lineplot(data=monthly_avg, marker='o', ax=ax)
ax.set_title("Average CO Levels by Month")
ax.set_ylabel("CO (ppm)")
ax.set_xlabel("Month")
ax.grid(True)
st.pyplot(fig)

# Plot 2: Top Polluted Regions by Annual Mean
st.subheader("🏙️ Top Polluted Regions by Annual Mean")
top_regions = df.sort_values("Mean", ascending=False).head(10)

fig2, ax2 = plt.subplots(figsize=(8, 6))
sns.barplot(y="Region", x="Mean", data=top_regions, palette="Reds_r", ax=ax2)
ax2.set_title("Top 10 Most Polluted Regions (Mean CO)")
ax2.set_xlabel("CO (ppm)")
ax2.set_ylabel("Region")
st.pyplot(fig2)

# Show raw data (optional)
if st.checkbox("Show raw data"):
    st.write(df_filtered)
