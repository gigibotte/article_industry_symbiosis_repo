from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Data
scenarios = ['Base', 'FIP', 'FIC', 'COMBO']
npv = [1, 15.4, 25.98, 35.3]
irr = [9.6, 17.5, 25.8, 31.3]
pbt = [10.2, 6.5, 4.7, 4]

# Define colors for scenarios
colors = ['#adb5bd','#8ecae6',  '#219EBC', '#FB8500']

# Create subplots
fig = make_subplots(rows=1, cols=3)

# Add subplot for NPV
fig.add_trace(go.Bar(
    x=scenarios,
    y=npv,
    name='NPV [k€]',
    marker_color=colors,
    showlegend=False
),
    row=1, col=1
)

# Add title for NPV subplot
fig.update_yaxes(title_text="NPV [k€]", row=1, col=1)

# Add subplot for IRR
fig.add_trace(go.Bar(
    x=scenarios,
    y=irr,
    name='IRR (%)',
    marker_color=colors,
    showlegend=False
),
    row=1, col=2
)

fig.add_trace(go.Scatter(
    x=scenarios,
    y=[9.03] * len(scenarios),  # Y value of 5 for each scenario
    mode='lines',
    name='WACC',  # Name for the line in legend
    line=dict(color='black', dash='dash'),  # Specify color and dash style
    showlegend=False  # Show the line in the legend
),
    row=1, col=2
)


# Add title for IRR subplot
fig.update_yaxes(title_text="IRR (%)", row=1, col=2)

# Add subplot for PBT
fig.add_trace(go.Bar(
    x=scenarios,
    y=pbt,
    name='PBT (Yrs)',
    marker_color=colors,
    showlegend=False
),
    row=1, col=3
)

fig.add_trace(go.Scatter(
    x=scenarios,
    y=[5] * len(scenarios),  # Y value of 5 for each scenario
    mode='lines',
    name='PBT Threshold',  # Name for the line in legend
    line=dict(color='black', dash='dash'),  # Specify color and dash style
    showlegend=False  # Show the line in the legend
),
    row=1, col=3
)

# Add title for PBT subplot
fig.update_yaxes(title_text="PBT (Yrs)", row=1, col=3)
fig.update_layout(font=dict(size=20))

# Show plot
fig.show()
# Update layout for the whole figure
