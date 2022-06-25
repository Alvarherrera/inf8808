'''
    This file contains the code for the bubble plot.
'''
import plotly.io as pio
from pydoc import visiblename
from turtle import title
import plotly.express as px
import plotly.graph_objects as go
from hover_template import hover_map_Template, hover_marker_Template


def get_plot(fig, df_revenue, montreal_data, revenue_range, df_top10Business):
    '''
        Generates the bubble plot.

        The x and y axes are log scaled, and there is
        an animation between the data for years 2000 and 2015.

        The markers' maximum size is 30 and their minimum
        size is 5.

        Args:
            my_df: The dataframe to display
            gdp_range: The range for the x axis
            co2_range: The range for the y axis
        Returns:
            The generated figure
    '''
    # TODO : Define figure with animation
    fig = px.choropleth(df_revenue, geojson=montreal_data, color="Revenue", 
                    color_continuous_scale=[[0, 'rgb(255, 255, 255)'], [0.01, 'rgb(255, 200, 200)'], [0.1, 'rgb(255, 175, 150)'], [0.5, 'rgb(255, 70, 120)'], [1.0, 'rgb(170, 0, 0)']],
                    locations='STATE', featureidkey="properties.prov_name_en", range_color=revenue_range, custom_data=df_revenue,
                    projection="mercator", animation_frame="Year")

    fig.update_traces(hovertemplate = hover_map_Template())
    for frame in fig.frames:
        for data in frame.data:
            data.hovertemplate = hover_map_Template()

    fig_scatter = px.scatter_geo(df_top10Business, lat="LATITUDE", lon='LONGITUDE', color='CITY', opacity=0.70,
                    hover_name='NAICS3_DESC', size='REVEN', custom_data=df_top10Business,
                     animation_frame="Year"
                    )
                    
    fig_scatter.update_traces(hovertemplate = hover_marker_Template())
    for frame in fig_scatter.frames:
        for data in frame.data:
            data.hovertemplate = hover_marker_Template()

    nbMarkers = len(fig_scatter.data)
    for m in range(nbMarkers):
        fig.add_trace(fig_scatter.data[m])

    for i, frame in enumerate(fig.frames):
        fig.frames[i].data += (fig_scatter.frames[i].data)
    fig.update_geos(
        fitbounds="locations",
        visible=False)

    fig.update_layout(dragmode=False,
    legend=dict(
        orientation="h",
        yanchor="top",
        y=0.13,
        xanchor="center",
        x=1.1
    ),
    coloraxis_colorbar=dict(
        title="Revenue (M$)",
        thicknessmode="pixels", thickness=30,
        lenmode="pixels", len=450,
        yanchor="top", y=1,
        ticks="outside"
    )
    )
    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                buttons=[
                    dict(label="Animate", visible=False),
                    dict(label="Pause", visible=False)
                ],
            )
        ],
        sliders=[{"currentvalue": {"prefix": "Data for year : "}}],
        legend_title_text='Cities of the top 10 enterprises by revenue (M$)')

    fig['layout']['updatemenus'][0]['pad']=dict(r= 50, t= 0)
    # fig['layout']['updatemenus'][0]['buttons']=dict(r= 50, t= 0)
    fig['layout']['sliders'][0]['pad']=dict(r= 50, t= 0,)

    return fig
