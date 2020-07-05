import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()



def create_layout(app):

    profile = '''
    Authors: [Newton Greco](https://www.linkedin.com/in/newtongreco/) & [Reyner Akira](https://www.linkedin.com/in/reyner-akira/)
    ''' 


    analysis_five = '''

    ***

    ### Model Evaluation

    In order to evaluate the accuracy of these models we have saved the data from year 2018 and compared with the predicted forecast for 2018.
    In the table underneath we can see that the coffee model produced the most accurate prediction with na error of 2.3%. Lemon and Maize both produced less accurate predictions with erros around 10%.

    ![alt text][id]

    [id]: https://github.com/R-Akira/Crop-Productivity-Dashboard/blob/master/Assets/Model_Evaluation.jpg?raw=True "Title"

    '''

    return html.Div(children= 
    [
        html.Div([Header(app)]),
        
        dcc.Markdown(children= profile,
        style = {'textAlign' : 'left', 'marginLeft' : 20
    }),

        dcc.Markdown(children=analysis_five, style = {
        'textAlign' : 'justify',
        'marginLeft' : 20,
        'marginRight': 50
    }),
    ])