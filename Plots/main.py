import pandas as pd
import plotly.express as px

# Read CSV files for each location
locations = ['X1', 'X2', 'X3']
dfs = {}

for location in locations:
    file_path = f'/Users/luigibottecchia/Dev/PhD/graphs_pyplot/data/results/eco_results_{location}_df_el.csv'
    dfs[location] = pd.read_csv(file_path)

# Convert negative values to positive before calculating the sum
for location, df in dfs.items():
    if 'soc' in df.columns:
        df['soc'] = df['soc'].abs()

# Calculate the sum of each column (excluding 'electricity_balance' and 'soc') for each location
sums_by_location = {
    location: df.drop(columns=['electricity_balance', 'soc'], errors='ignore').sum() for location, df in dfs.items()
}

# Create a DataFrame from the sums
sums_df = pd.DataFrame(sums_by_location).T.abs()  # Transpose the DataFrame

print(sums_df.head())

# Filter legend entries to include only variables with a sum greater than 0
legend_labels = [col for col in sums_df.columns if sums_df[col].sum() > 0]

# Create a stacked bar plot using Plotly
fig = px.bar(sums_df[legend_labels], barmode='stack',
             labels={'index': 'Location', 'value': 'Total Cost (€)'},
             category_orders={'index': locations})

# Show the plot
fig.show()
fig.write_image('/Users/luigibottecchia/Dev/PhD/graphs_pyplot/data/Overall_Sys_Costs_NoDH.jpg', format='jpeg')



