import pandas as pd
import plotly.express as px
import os.path

path = os.path.dirname(os.path.abspath("main_article3.py"))
# Read CSV files for each location
locations = ['X1', 'X2', 'X3']
scenarios = ["techsHP", "techsDH"]
dfs = {}

for scenario in scenarios:
    for location in locations:
        for suffix in ['el', 'th']:  # Loop over both possible suffixes
            filename = f"eco_results_{location}_df_{suffix}_{scenario}.csv"
            file_path = os.path.join(path, 'data_article3', 'results', filename)
            if os.path.isfile(file_path):
                # Read CSV files for each location and suffix
                df = pd.read_csv(file_path)

                # Convert negative values to positive before calculating the sum
                if 'soc' in df.columns:
                    df['soc'] = df['soc'].abs()

                # Add the dataframe to the dictionary with a key that includes the suffix
                dfs[f"{location}_{suffix}"] = df

    # Calculate the sum of each column (excluding 'electricity_balance' and 'soc') for each location
    sums_by_location = {
        location: df.drop(columns=['soc', "demand_electricity"], errors='ignore').sum()
        for location, df in dfs.items()
    }

    # Create a DataFrame from the sums
    sums_df = pd.DataFrame(sums_by_location).T.abs()  # Transpose the DataFrame

    # Calculate overall total for each location
    overall_totals = sums_df.sum(axis=1)

    # Filter legend entries to include only variables with a sum greater than 0
    legend_labels = [col for col in sums_df.columns if sums_df[col].sum() > 0]

    # Add overall total as a new column to the DataFrame
    sums_df['overall_total'] = overall_totals
    print(sums_df)

    # Create a stacked bar plot using Plotly
    fig = px.bar(sums_df[legend_labels], barmode='stack',
                 labels={'index': 'Location', 'value': 'Total Cost (€)'},
                 category_orders={'index': locations})

    # Update layout to increase font size
    fig.update_layout(
        font=dict(
            family="Arial, sans-serif",
            size=18,  # Set the font size as desired
            color="black"  # Set the font color if needed
        )
    )

    # Add text annotations for overall total on each bar
    for location in locations:
        total_value = sums_df.loc[location].groupby(level=0)['overall_total'].sum()
        formatted_total = "{:,.0f}".format(total_value).replace(",", " ")  # Use space as a separator
        fig.add_annotation(
            x=location,
            y=total_value * 1.05,  # Adjust the vertical position for better visibility
            text=f'{formatted_total}',
            showarrow=False,
            font=dict(color='black', size=20),
        )

    # Show the plot
    fig.show()

    # fig.write_image(os.path.join(path, 'data_article3', f"Overall_Sys_Costs_{scenario}.jpg"), format='jpeg', engine='kaleido')
