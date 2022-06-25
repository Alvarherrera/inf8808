# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import json
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
from geojson_rewind import rewind
import plotly.graph_objects as go

import preprocess
import map

app = Dash(__name__)
app.title = 'Innovation Canada'

colors = {
    'background': '#DDDDDD',
    'text': '#111111'
}

with open('./assets/data/georef-canada-province.geojson', encoding='utf-8') as data_file:
    canada_data = json.load(data_file)

df_2015 = pd.read_csv('./assets/data/Canada_2015_Site_Description.csv')
df_2016 = pd.read_csv('./assets/data/Canada_2016_Site_Description.csv')
df_2017 = pd.read_csv('./assets/data/Canada_2017_Site_Description.csv')
df_2018 = pd.read_csv('./assets/data/Canada_2018_Site_Description.csv')

df_combine = preprocess.combine_dfs(df_2015, df_2016, df_2017, df_2018)
df_revenue = preprocess.sort_dy_by_yr_region(df_combine)
df_business = preprocess.sort_business(df_combine)

revenue_range = preprocess.get_range('Revenue', df_revenue)

canada_data = rewind(canada_data,rfc7946=False)
fig = go.Figure()
fig = map.get_plot(fig, df_revenue, canada_data, revenue_range, df_business)

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig.update_layout(height=800, width=800, margin=dict(l=20, r=20, t=20, b=0))

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1("L'innovation des entreprises au Canada",
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children=[
        dcc.Graph(id="figure-1", figure=fig,style={'display': 'inline-block'}),
        dcc.Graph(id="figure-2", figure=fig,style={'display': 'inline-block'})
    ]),
        
    html.Div(children="Un site crée par Alexandre Ramtoula, Alvar Herrera et Sylvain Ramtoula dans le cadre du cours INF8808", style={
        'textAlign': 'right',
        'color': colors['text'],
        'size': '10px'
    }),
    
])

if __name__ == '__main__':
    app.run_server(debug=True)
    