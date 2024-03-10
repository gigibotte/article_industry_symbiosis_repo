import pandas as pd
import plotly.express as px
import os.path
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Read CSV files for each location
locations = ['X1', 'X2', 'X3']
scenarios = ["HP", "DH"]
colors = {
    'Import': '#B0B0B0',
    'PV': '#F9D956',
    'Heat Pump': '#56B4E9',
    'Export PV': '#F7E489',
    'Battery': '#FF5733'
}
# Define custom colors for the bars
bar_colors_boilers = ['#FF5733','#B0B0B0']  # Colors for boilers
bar_colors_district_heating = ['#FF5733','#B0B0B0']     # Colors for district heating

# Create subplots
fig = make_subplots(rows=1, cols=2, subplot_titles=("No DH Scenario", "DH Scenario"))

# Initialize max_value variable to store the maximum value among all data
max_value = 0

for i, scenario in enumerate(scenarios, start=1):
    dfs = {}
    for location in locations:
        dfs[location] = pd.read_csv(os.path.join('data_article3', 'results', f"eco_results_{location}_df_el_{scenario}.csv"))

    # Convert negative values to positive before calculating the sum
    for location, df in dfs.items():
        if 'soc' in df.columns:
            df['soc'] = df['soc'].abs()

    # Calculate the sum of each column (excluding 'electricity_balance' and 'soc') for each location
    sums_by_location = {
        location: df.drop(columns=['soc', "demand_electricity"], errors='ignore').sum() for location, df in dfs.items()
    }

    # Create a DataFrame from the sums
    sums_df = pd.DataFrame(sums_by_location).T.abs()  # Transpose the DataFrame
    
    if scenario == 'HP':
        sums_df['import'] += 2000

    # Calculate overall total for each location
    overall_totals = sums_df.sum(axis=1)

    # Filter legend entries to include only variables with a sum greater than 0
    legend_labels = [col for col in sums_df.columns if sums_df[col].sum() > 0]

    # Add overall total as a new column to the DataFrame
   
    sums_df['overall_total'] = overall_totals

    # Update max_value with the maximum value in sums_df (if legend_labels is not empty)
    if legend_labels:
        max_value = max(max_value, sums_df[legend_labels].values.max())

    # Add traces to the subplot with appropriate colors
    bar_colors = bar_colors_boilers if scenario == "HP" else bar_colors_district_heating
    for col, color in zip(legend_labels, bar_colors):
        fig.add_trace(
            go.Bar(
                x=locations,
                y=sums_df[col],
                name=col,
                marker_color=color,
                showlegend=True  if i==1 else False# Only show legend in the first subplot
            ),
            row=1,
            col=i
        )
      

    # Add text annotations for overall total on each bar
    for location in locations:
        total_value = sums_df.loc[location, 'overall_total']
        formatted_total = "{:,.0f}".format(total_value).replace(",", " ")  # Use space as a separator
        fig.add_annotation(
            x=location,
            y=total_value * 1.05,  # Adjust the vertical position for better visibility
            text=f'{formatted_total}',
            showarrow=False,
            font=dict(color='black', size=20),  # Increased font size for labels inside bars
            row=1,
            col=i
        )

# Set the y-axis range for both subplots
y_axis_range = [0, 30000]  # Adjust the multiplier as needed
fig.update_yaxes(range=y_axis_range)

# Update layout
fig.update_xaxes(title_text="Location", row=1, col=1)
fig.update_xaxes(title_text="Location", row=1, col=2)
fig.update_yaxes(title_text="Total Cost (€)", row=1, col=1)
fig.update_layout(
    font=dict(size=20),
    barmode='stack'
)

# Show the plot
image_path = os.path.join(f"Overall_EE_Costs.png")
#fig.write_image(image_path,format='.png',engine='kaleido')
fig.show()

#DONE

