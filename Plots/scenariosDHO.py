from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Data
scenarios = ['Base', 'FIP', 'FIC', 'COMBO']
DCF = [0, 0, 0.87, 2.45]
CDCF = [0, 0, 8.75 , 24.5]


# Define colors for scenarios
colors = ['#adb5bd','#8ecae6',  '#219EBC', '#FB8500']

# Create subplots
fig = make_subplots(rows=1, cols=2)

# Add subplot for DCF
fig.add_trace(go.Bar(
    x=scenarios,
    y=DCF,
    name='Avg Yearly DCF [k€]',
    marker_color=colors,
    showlegend=False
),
    row=1, col=1
)

# Add title for CDCF subplot
fig.update_yaxes(title_text="Avg Yearly DCF [k€]", row=1, col=1)

# Add subplot for CDCF
fig.add_trace(go.Bar(
    x=scenarios,
    y=CDCF,
    name='Cumulated DCF [k€]',
    marker_color=colors,
    showlegend=False
),
    row=1, col=2
)



# Add title for CDCF subplot
fig.update_yaxes(title_text="Cumulated DCF [k€]", row=1, col=2)


fig.update_layout(font=dict(size=20))

# Show plot
fig.show()
# Update layout for the whole figure
