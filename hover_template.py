'''
    Provides the template for the tooltips.
'''
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

def hover_map_Template():
    '''
        Sets the template for the hover tooltips.
        
        Contains four labels, followed by their corresponding
        value and units where appropriate, separated by a
        colon : country, population, GDP and CO2 emissions.

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''
    # TODO : Generate tooltip
    hovertemplate = '<span><b>          State : </b>%{customdata[1]}</span><br>' 
    hovertemplate += '<span><b>          Revenue (M$) : </b>%{customdata[2]} (USD)</span><br>'  
    hovertemplate += '<extra></extra>'
    return hovertemplate

def hover_marker_Template():
    '''
        Sets the template for the hover tooltips.
        
        Contains four labels, followed by their corresponding
        value and units where appropriate, separated by a
        colon : country, population, GDP and CO2 emissions.

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''
    # TODO : Generate tooltip
    hovertemplate = '<span><b>Company : </b>%{customdata[4]}</span><br>' 
    hovertemplate += '<span><b>City : </b>%{customdata[2]}</span><br>' 
    hovertemplate += '<span><b>State : </b>%{customdata[1]}</span><br>'  
    hovertemplate += '<span><b>Revenue (M$) : </b>%{marker.size} (USD)</span><br>'
    hovertemplate += '<extra></extra>'
    return hovertemplate
