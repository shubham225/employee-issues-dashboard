import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import traceback

from app import app
from modules import data_operations,constant


def get_layout():
    try:
        df_issues = data_operations.generate_dataframe()

        df1 = df_issues.groupby([constant.STATUS])[constant.ISSUE_ID].count().reset_index(name="Issue Count")
        
        grp = df_issues.groupby([constant.CREATED_DATE, constant.ISSUE_TYPE])[constant.ISSUE_ID]
        df2 = grp.count().reset_index(name="Issue Count")
        
        df3 = df_issues.groupby([constant.PRIORITY])[constant.ISSUE_ID].count().reset_index(name="Issue Count")

        layout = dbc.Container([
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='my-line', 
                                figure= px.line(df2, 
                                x=constant.CREATED_DATE, 
                                y='Issue Count', 
                                color=constant.ISSUE_TYPE,
                                title='Tickets by Created Date'))
                        ],
                        width=12)
                    ],
                    style={'padding-bottom': '10px'},
                    no_gutters=True),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id='my-pie2', 
                                figure= px.pie(df3, 
                                    values='Issue Count', 
                                    names= constant.PRIORITY, 
                                    title='Issues by Priority',
                                    hole=0.3))
                        ],
                        width=6),
                        dbc.Col([
                            dcc.Graph(id='my-pie', 
                                figure= px.pie(df1, 
                                    values='Issue Count', 
                                    names= constant.STATUS,
                                    title='Issues by Status'))
                        ],
                        width=6)
                    ],
                    style={'padding-bottom': '10px'},
                    no_gutters=True)
                ],
                fluid=True)
        return layout
    except:
        layout = dbc.Jumbotron(
                    [
                        html.Div([
                            html.H1("500: Internal Server Error", className="text-danger"),
                            html.Hr(),
                            html.P(f"Following Exception Occured: "),
                            html.Code(traceback.format_exc())
                        ],
                        style=constant.NAVITEM_STYLE)
                    ]
                )
        return layout
