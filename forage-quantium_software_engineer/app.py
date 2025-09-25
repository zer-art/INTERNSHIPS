from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('data/final.csv')
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year

app = Dash()

# Requires Dash 2.17.0 or later
app.layout = [
    html.H1(children='Sales data visualisation over time', style={'textAlign':'center'}),
    html.Div([
        html.Label('Select Region:'),
        dcc.Dropdown(df.region.unique(), 'north', id='dropdown-selection'),
    ], style={'width': '48%', 'display': 'inline-block'}),
    html.Div([
        html.Label('Select Year:'),
        dcc.Dropdown(sorted(df.year.unique()), df.year.max(), id='year-dropdown'),
    ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),
    dcc.Graph(id='graph-content')
]

@callback(
    Output('graph-content', 'figure'),
    [Input('dropdown-selection', 'value'),
     Input('year-dropdown', 'value')]
)
def update_graph(region_value, year_value):
    dff = df[(df.region == region_value) & (df.year == year_value)]
    return px.line(dff, x='date', y='sales', title=f'Sales Data for {region_value.title()} Region in {year_value}')

if __name__ == '__main__':
    app.run(debug=True)
