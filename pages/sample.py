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
    
    return html.Div(children= 
    [
        html.Div([Header(app)]),
        dbc.Button("Click me TOO", id="example-button", className="mr-2"),
        html.Span(id="example-output", style={"vertical-align": "middle"}),
    ], style = {'textAlign' : 'center'}
    )
    
    @app.callback(
    Output("example-output", "children"), [Input("example-button", "n_clicks")]
    )

    def on_button_click(n):
        if n is None:
            return "Not clicked."
        else:
            return f"Clicked {n} times."

