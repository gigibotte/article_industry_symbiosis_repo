
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Data
locations = ['X1', 'X2', 'X3']
categories = ['Heat Pump', "DH Industry"]
heatpump = [[100,0], [100,0], [100,0]]
dh = [[0,100], [0,100], [0,100]]

# Define colors for each category
colors = {
    'Heat Pump': '#56B4E9',
    'DH Industry': '#D55E00'
}

# Create subplots
fig = make_subplots(rows=1, cols=2, subplot_titles=("No DH Scenario", "DH Scenario"))

# Add traces for Subplot 1 (Heat Pump Scenario)
for i, category in enumerate(categories):
    fig.add_trace(go.Bar(
        x=locations,
        y=[heatpump[j][i] for j in range(len(locations))],
        name=category,
        marker_color=colors[category],
        legendgroup=category
    ), row=1, col=1)

# Add traces for Subplot 2 (District Heating Scenario)
for i, category in enumerate(categories):
    fig.add_trace(go.Bar(
        x=locations,
        y=[dh[j][i] for j in range(len(locations))],
        name=category,
        marker_color=colors[category],
        legendgroup=category,
        showlegend=False
    ), row=1, col=2)

# Update layout
fig.update_xaxes(title_text="Locations", row=1, col=1)
fig.update_xaxes(title_text="Locations", row=1, col=2)
fig.update_yaxes(title_text="%", row=1, col=1)
fig.update_layout(font=dict(size=20), barmode='stack')

# Show plot
fig.show()

#DONE