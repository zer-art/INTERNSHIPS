from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('data/final.csv')
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year

app = Dash()

# Custom CSS styling
app.layout = html.Div([
    # Header section
    html.Div([
        html.H1(
            children='📊 Sales Data Visualization Dashboard',
            style={
                'textAlign': 'center',
                'color': '#2c3e50',
                'marginBottom': '30px',
                'fontFamily': 'Arial, sans-serif',
                'fontSize': '2.5em',
                'fontWeight': 'bold',
                'textShadow': '2px 2px 4px rgba(0,0,0,0.1)'
            }
        ),
    ], style={
        'background': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'padding': '20px',
        'marginBottom': '30px',
        'borderRadius': '10px',
        'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)'
    }),
    
    # Controls section
    html.Div([
        # Region selection
        html.Div([
            html.Label(
                'Select Region:',
                style={
                    'fontWeight': 'bold',
                    'fontSize': '1.2em',
                    'color': '#34495e',
                    'marginBottom': '10px',
                    'display': 'block'
                }
            ),
            dcc.RadioItems(
                options=[{'label': region.title(), 'value': region} for region in df.region.unique()],
                value='north',
                id='radio-selection',
                inline=True,
                style={
                    'display': 'flex',
                    'justifyContent': 'space-around',
                    'marginTop': '10px'
                },
                inputStyle={
                    'marginRight': '5px',
                    'transform': 'scale(1.2)'
                },
                labelStyle={
                    'marginRight': '20px',
                    'fontSize': '1.1em',
                    'color': '#2c3e50',
                    'fontWeight': '500'
                }
            ),
        ], style={
            'width': '48%',
            'display': 'inline-block',
            'padding': '20px',
            'backgroundColor': '#ecf0f1',
            'borderRadius': '10px',
            'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
            'marginRight': '2%'
        }),
        
        # Year selection
        html.Div([
            html.Label(
                'Select Year:',
                style={
                    'fontWeight': 'bold',
                    'fontSize': '1.2em',
                    'color': '#34495e',
                    'marginBottom': '10px',
                    'display': 'block'
                }
            ),
            dcc.Dropdown(
                options=[{'label': str(year), 'value': year} for year in sorted(df.year.unique())],
                value=df.year.min(),
                id='year-dropdown',
                style={
                    'fontSize': '1.1em'
                }
            ),
        ], style={
            'width': '48%',
            'display': 'inline-block',
            'padding': '20px',
            'backgroundColor': '#ecf0f1',
            'borderRadius': '10px',
            'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
        }),
    ], style={'marginBottom': '30px'}),
    
    # Graph section
    html.Div([
        dcc.Graph(
            id='graph-content',
            style={
                'borderRadius': '10px',
                'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'
            }
        )
    ], style={
        'backgroundColor': 'white',
        'padding': '20px',
        'borderRadius': '10px',
        'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'
    })
], style={
    'fontFamily': 'Arial, sans-serif',
    'backgroundColor': '#f8f9fa',
    'padding': '20px',
    'minHeight': '100vh'
})

@callback(
    Output('graph-content', 'figure'),
    [Input('radio-selection', 'value'),
     Input('year-dropdown', 'value')]
)
def update_graph(region_value, year_value):
    dff = df[(df.region == region_value) & (df.year == year_value)]
    
    # Create the line plot with custom styling
    fig = px.line(
        dff, 
        x='date', 
        y='sales', 
        title=f'Sales Data for {region_value.title()} Region in {year_value}',
        color_discrete_sequence=['#3498db']
    )
    
    # Update layout for better styling
    fig.update_layout(
        title={
            'text': f'📈 Sales Data for {region_value.title()} Region in {year_value}',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 24, 'color': '#2c3e50', 'family': 'Arial, sans-serif'}
        },
        xaxis={
            'title': {'text': 'Date', 'font': {'size': 16, 'color': '#34495e'}},
            'tickfont': {'size': 12, 'color': '#7f8c8d'},
            'gridcolor': '#ecf0f1'
        },
        yaxis={
            'title': {'text': 'Sales ($)', 'font': {'size': 16, 'color': '#34495e'}},
            'tickfont': {'size': 12, 'color': '#7f8c8d'},
            'gridcolor': '#ecf0f1'
        },
        plot_bgcolor='white',
        paper_bgcolor='white',
        font={'family': 'Arial, sans-serif'}
    )
    
    # Update line styling
    fig.update_traces(
        line=dict(width=3, color='#3498db'),
        hovertemplate='<b>Date:</b> %{x}<br><b>Sales:</b> $%{y:,.2f}<extra></extra>'
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)
