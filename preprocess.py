'''
    Contains some functions to preprocess the data used in the visualisation.
'''


import pandas as pd

# def get_range(col, df1, df2):
#     '''
#         An array containing the minimum and maximum values for the given
#         column in the two dataframes.

#         args:
#             col: The name of the column for which we want the range
#             df1: The first dataframe containing a column with the given name
#             df2: The first dataframe containing a column with the given name
#         returns:
#             The minimum and maximum values across the two dataframes
#     '''
#     # TODO : Get the range from the dataframes
#     col1 = df1.loc[:,col]
#     col2 = df2.loc[:,col]
#     minimum = min(col1.min(), col2.min())
#     maximum = max(col1.max(), col2.max())
#     return [minimum, maximum]

TITLES_STATES = {
    # pylint: disable=line-too-long
    'AB': 'Alberta',
    'BC': 'British Columbia', # noqa : E501
    'MB': 'Manitoba', # noqa : E501
    'NB': 'New Brunswick', # noqa : E501
    'NL': 'Newfoundland and Labrador', # noqa : E501
    'NS': 'Nova Scotia', # noqa : E501
    'NT': 'Northwest Territories',
    'ON': 'Ontario', # noqa : E501
    'PE': 'Prince Edward Island', # noqa : E501
    'QC': 'Quebec', # noqa : E501
    'SK': 'Saskatchewan',
    'YU': 'Yukon', # noqa : E501
    'NU': 'Nunavut', # noqa : E501
    'YT': 'Yukon',
    'PR': 'Prince Edward Island' # noqa : E501
}

def get_range(col, df):
    '''
        An array containing the minimum and maximum values for the given
        column in the two dataframes.

        args:
            col: The name of the column for which we want the range
            df1: The first dataframe containing a column with the given name
            df2: The first dataframe containing a column with the given name
        returns:
            The minimum and maximum values across the two dataframes
    '''
    # TODO : Get the range from the dataframes
    col = df.loc[:,col]
    minimum = col.min()
    maximum = col.max()
    return [minimum, maximum]

def combine_dfs(df1, df2, df3, df4):
    '''
        Combines the two dataframes, adding a column 'Year' with the
        value 2000 for the rows from the first dataframe and the value
        2015 for the rows from the second dataframe

        args:
            df1: The first dataframe to combine
            df2: The second dataframe, to be appended to the first
        returns:
            The dataframe containing both dataframes provided as arg.
            Each row of the resulting dataframe has a column 'Year'
            containing the value 2000 or 2015, depending on its
            original dataframe.
    '''
    # TODO : Combine the two dataframes
    df1["Year"] = 2015
    df2["Year"] = 2016
    df3["Year"] = 2017
    df4["Year"] = 2018
    df = pd.concat([df1, df2, df3, df4])
    df = df.reset_index(drop=True)
    df = df.replace({"STATE": TITLES_STATES})
    return df


def sort_dy_by_yr_region(my_df):
    '''
        Sorts the dataframe by year and then by continent.

        args:
            my_df: The dataframe to sort
        returns:
            The sorted dataframe.
    '''
    # TODO : Sort the dataframe
    my_df = my_df.sort_values(by=['Year', 'STATE'])
    df = my_df.groupby(['Year', 'STATE'])['REVEN'].sum().reset_index(name="Revenue")
    new_row1 = {'Year':2015, 'STATE':'Nunavut', 'Revenue':0}
    new_row2 = {'Year':2017, 'STATE':'Nunavut', 'Revenue':0}
    df = df.append(new_row1, ignore_index=True)
    df = df.append(new_row2, ignore_index=True)
    return df

def sort_business(my_df):
    '''
        Sorts the dataframe by year and then by continent.

        args:
            my_df: The dataframe to sort
        returns:
            The sorted dataframe.
    '''
    # TODO : Sort the dataframe
    df = my_df.groupby([my_df['Year']]).apply(lambda grp: grp.nlargest(10, 'REVEN'))
    df = df[['Year', 'STATE', 'CITY', 'REVEN', 'NAICS3_DESC', 'LONGITUDE', 'LATITUDE']]
    df = df.reset_index(drop=True)
    df.loc[3, 'LONGITUDE'] = -100
    df.loc[3, 'LATITUDE'] = 50
    df.loc[5, 'LONGITUDE'] = -100
    df.loc[5, 'LATITUDE'] = 50
    df.loc[6, 'LONGITUDE'] = -100
    df.loc[6, 'LATITUDE'] = 50
    df.loc[11, 'LONGITUDE'] = -100
    df.loc[11, 'LATITUDE'] = 50
    df.loc[12, 'LONGITUDE'] = -100
    df.loc[12, 'LATITUDE'] = 50
    df.loc[14, 'LONGITUDE'] = -100
    df.loc[14, 'LATITUDE'] = 50
    df.loc[16, 'LONGITUDE'] = -100
    df.loc[16, 'LATITUDE'] = 50
    df.loc[18, 'LONGITUDE'] = -100
    df.loc[18, 'LATITUDE'] = 50
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="geoapiExercises")
    

    df.loc[:,'Location'] = geolocator.geocode(str(df['LATITUDE'])+","+str(df['LONGITUDE']))
    # for index, row in df.iterrows():
    #     lat = str(row['LATITUDE'])
    #     lon = str(row['LONGITUDE'])
    #     location = geolocator.geocode(lat+","+lon)
    #     df.loc[index, 'Location'] = (lat+","+lon)

    return df
