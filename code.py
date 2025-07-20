import sqlite3
import pandas as pd
import json

# Connect to your database
conn = sqlite3.connect('corr.db')

# Load data into a DataFrame
df = pd.read_sql_query("SELECT Net_Sales, Returns, Promo_Spend FROM retail_data", conn)

# Calculate correlations
corr_ns_ret = df['Net_Sales'].corr(df['Returns'])
corr_ns_promo = df['Net_Sales'].corr(df['Promo_Spend'])
corr_ret_promo = df['Returns'].corr(df['Promo_Spend'])

# Store results in a dictionary
results = {
    "Net_Sales-Returns": corr_ns_ret,
    "Net_Sales-Promo_Spend": corr_ns_promo,
    "Returns-Promo_Spend": corr_ret_promo
}

# Find the strongest correlation (by absolute value)
strongest_pair = max(results, key=lambda k: abs(results[k]))
output = {
    "pair": strongest_pair,
    "correlation": results[strongest_pair]
}

# Save as JSON for GitHub Pages
with open("correlation_result.json", "w") as f:
    json.dump(output, f)