import pandas as pd

# Read hourly power prices from CSV
hourly_power_prices_df = pd.read_csv('/Users/luigibottecchia/Dev/PhD/graphs_pyplot/dataprices/power_prices.csv')

# Convert the 'Timestamp' column to datetime if it's not already
hourly_power_prices_df['time'] = pd.to_datetime(hourly_power_prices_df['time'])

# Extract date from timestamp
hourly_power_prices_df['Date'] = hourly_power_prices_df['time'].dt.date

# Calculate daily average power prices
daily_average_power_prices_df = hourly_power_prices_df.groupby('Date')['Prices'].mean().reset_index()

daily_average_power_prices_df = daily_average_power_prices_df["Prices"].repeat(24)

# Save the daily average power prices to a new CSV file
daily_average_power_prices_df.to_csv('daily_average_power_prices.csv', index=False)
