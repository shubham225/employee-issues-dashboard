import dash
import dash_table
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd

import traceback

# Connect to main app.py file
from app import app

from modules import data_operations,constant

def get_layout():
    try:
        config_df = data_operations.read_config_in_df()
        layout = dbc.Container([
                    dbc.Row([
                            dbc.Col([
                            dbc.Card([
                                    dbc.CardHeader("Configurations: CSV Mapping"),
                                    dbc.CardBody(
                                    [
                                        html.P(
                                                "Setup mapping between csv file and the app fields.",
                                                className="card-text",id="paragr"
                                            ),
                                        dash_table.DataTable(
                                            id="settings-mapping",
                                            columns = [{"name": i, "id": i} for i in config_df.columns],
                                            data = config_df.to_dict('records'),
                                            style_header={
                                            'fontWeight': 'bold'
                                            },
                                            style_cell={
                                            'whiteSpace': 'normal',
                                            'height':'auto' 
                                            },
                                            fixed_rows={'headers': True},
                                            page_action='none',
                                            editable=True
                                        )
                                    ]),
                                ],
                                className="shadow p-3 bg-light rounded")
                            ],
                            width=12)
                        ],
                        className= "pb-3"
                    ),
                    dbc.Row([
                        dbc.Col([
                            html.Span("Format: ", style={"vertical-align": "middle"},className="ml-3")
                        ], width=1),
                        dbc.Col([
                            dbc.Input(
                                id="input_dateformat",
                                type="text",
                                placeholder="Input Date Format...",
                                value = constant.DATE_FORMAT
                            )
                        ], width=3)
                    ], no_gutters=True),
                    dbc.Row([
                    html.Div(
                            [
                            dbc.Button("Save Configurations", id="save_button", n_clicks= 0, className="m-3 ml-0", color="primary"),
                            html.Span(id="example-output", style={"vertical-align": "middle"}),
                            ]
                    )
                    ])
                ],
            fluid=True)
        return (layout)
    except:
        layout = dbc.Jumbotron(
                    [
                        html.Div([
                            html.H1("500: Internal Server Error", className="text-danger"),
                            html.Hr(),
                            html.P(f"Following Exception Occured:"),
                            html.Code(traceback.format_exc())
                        ],
                        style=constant.NAVITEM_STYLE)
                    ]
                )
        return layout
        
@app.callback(
    Output(component_id='example-output', component_property='children'), 
    [Input(component_id='save_button', component_property='n_clicks')],
    [State(component_id='settings-mapping', component_property='data'),
     State(component_id='input_dateformat', component_property='value')]
)
def on_button_click(num_click, table_data, dt_format):
    if num_click > 0:
        if data_operations.write_field_mapping_file(table_data,dt_format) == 0:
            config_df = data_operations.read_config_in_df()
            return "Settings Saved Sucessfully..."
        else:    
            return "Error Writing Config file"