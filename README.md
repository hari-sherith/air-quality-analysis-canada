# Canadian Air Quality CO Dashboard

Streamlit-powered, pandas-analyzed, and matplotlib-visualized data analysis of carbon monoxide (CO) levels across Canada in 2023.

Data source: NAPS (National Air Pollution Surveillance) program.

---

## Overview

This project provides an interactive dashboard to explore regional and national CO pollution trends across Canada. Built using a lightweight, reproducible Python stack with a focus on quick analytics and public reporting.

---

## Features

- Monthly CO trendline across Canada
- Region-level filter and comparison
- Top 10 most polluted regions by annual average
- Interactive visualizations with Streamlit
- Structured preprocessing pipeline

---

## Stack

- Python 3.12+
- pandas
- matplotlib
- seaborn
- Streamlit

---

## Dataset

Source: [Canada Open Data – NAPS CO Annual Data (2023)](https://data.ec.gc.ca/data/air/monitor/national-air-pollution-surveillance-naps-program/)

---

## Running Locally

```bash
git clone https://github.com/hari-sherith/air-quality-analysis-canada.git
cd air-quality-analysis-canada
pip install -r requirements.txt
streamlit run app.py

