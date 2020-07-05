import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from pages import (
    sample,
    random
)

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"},
    ],external_stylesheets=[dbc.themes.BOOTSTRAP]
)
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)



# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/Dash/sample":
        return sample.create_layout(app)
    elif pathname == "/Dash/full-view":
        return (
            sample.create_layout(app),
            random.create_layout(app)
            )
    else:
        return random.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)