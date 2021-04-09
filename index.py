import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from pages import dashboard, overview, settings
from modules import navbar, constant

#Fetch the Configurations
CONFIG_OBJECT = constant.read_config()

auth = dash_auth.BasicAuth(
    app,
    constant.VALID_USERNAME_PASSWORD_PAIRS
)

content = html.Div(id="page-content", style=constant.CONTENT_STYLE, className="p-3 pt-4 pb-3")

app.layout = html.Div([dcc.Location(id="url"), navbar.layout, content])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/pages/dashboard' or pathname == '/':
        return dashboard.get_layout()
    elif pathname == '/pages/overview':
        return overview.get_layout()
    elif pathname == '/pages/settings':
        return settings.get_layout()
    else:
        return dbc.Jumbotron(
            [
                html.Div([
                    html.H1("404: Not found", className="text-danger"),
                    html.Hr(),
                    html.P(f"Page {pathname} was not found...")
                ],
                style=constant.NAVITEM_STYLE)
            ]
       )

app.title = 'Issues Dashboard'

if __name__ == '__main__':
    app.run_server(debug=False,port=8090,host='0.0.0.0',threaded=True)
