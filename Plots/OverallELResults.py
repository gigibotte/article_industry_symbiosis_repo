import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Data
locations = ['X1', 'X2', 'X3']
categories = ['Import', 'PV', 'Heat Pump', "Export PV", "Battery"]
heatpump = [[134,43,-83,-66,0], [143,57,-104,-66,-2], [169,49,-120,-34,-1]]
dh = [[60,40,0,-70,0], [48,50,0,-74,-2], [55,43,0,-40,-2]]

# Define colors for each category
colors = {
    'Import': '#B0B0B0',
    'PV': '#F9D956',
    'Heat Pump': '#56B4E9',
    'Export PV': '#F7E489',
    'Battery': '#FF5733'
}

# Calculate maximum value among all data
max_value = 200
min_value = -200
fig = make_subplots(rows=1, cols=2, subplot_titles=("No DH Scenario", "DH Scenario"))

# Add bar charts for Subplot 1 (Heat Pump Scenario)
for i, category in enumerate(categories):
    fig.add_trace(go.Bar(
        x=locations,
        y=[heatpump[j][i] for j in range(len(locations))],
        name=category,
        marker_color=colors[category]
    ), row=1, col=1)

# Add bar charts for Subplot 2 (District Heating Scenario)
for i, category in enumerate(categories):
    fig.add_trace(go.Bar(
        x=locations,
        y=[dh[j][i] for j in range(len(locations))],
        name=category,
        marker_color=colors[category],
        showlegend=False
    ), row=1, col=2)

# Set the y-axis range for both subplots
fig.update_yaxes(range=[min_value *1.1, max_value * 1.1], row=1, col=1)
fig.update_yaxes(range=[min_value *1.1, max_value * 1.1], row=1, col=2)

# Update layout
fig.update_xaxes(title_text="Locations", row=1)
fig.update_yaxes(title_text="%", row=1, col=1)
fig.update_layout(font=dict(size=20), barmode='relative')

# Show plot
fig.show()

#DONE
