import pandas as pd

start_date = '2021-01-01 00:00:00'
end_date = '2021-12-31 23:00:00'
datetime_range = pd.date_range(start=start_date, end=end_date, freq='H')

# Read hourly power prices from CSV
hourly_power_prices_df = pd.read_csv('/Users/luigibottecchia/Dev/PhD/graphs_pyplot/dataprices/power_prices.csv')

# Read daily average gas prices from CSV
daily_average_gas_prices_df = pd.read_csv('/Users/luigibottecchia/Dev/PhD/graphs_pyplot/dataprices/gaspricesdaily.csv')

# Repeat daily average gas prices for each hour
daily_average_gas_prices_df = pd.DataFrame(daily_average_gas_prices_df['Prices'].repeat(24))
daily_average_gas_prices_df.index = datetime_range


hourly_power_prices_df = hourly_power_prices_df.drop(columns='time')
hourly_power_prices_df.index = datetime_range

daily_average_power_prices_df = hourly_power_prices_df.resample('D').mean()

daily_average_power_prices_df = pd.DataFrame(daily_average_power_prices_df['Prices'].repeat(24))

power_prices = pd.DataFrame()

power_prices['Hourly Prices'] = hourly_power_prices_df['Prices']
daily_average_power_prices_df.index = datetime_range
power_prices["Daily Avg"] = daily_average_power_prices_df['Prices']

power_prices['Scaling Factors'] = power_prices['Hourly Prices']/power_prices['Daily Avg']

daily_average_gas_prices_df['Hourly_Prices'] = daily_average_gas_prices_df['Prices']*power_prices['Scaling Factors']

hourly_gas_prices = pd.DataFrame(daily_average_gas_prices_df['Hourly_Prices'])
hourly_gas_prices['time']=hourly_gas_prices.index
hourly_gas_prices = hourly_gas_prices[['time','Hourly_Prices']]

hourly_gas_prices.to_csv('/Users/luigibottecchia/Dev/PhD/graphs_pyplot/dataprices/hourly_gas_prices.csv', index=False)

