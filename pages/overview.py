import dash
import dash_table
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd

import traceback

# import custom modules
from app import app
from modules import app_element, data_operations, constant

def get_layout():
	try:  
		df = data_operations.generate_dataframe()
		
		df1 = df[[constant.ASSIGNED_TO, constant.ISSUE_ID]]
		df1 = df1.groupby([constant.ASSIGNED_TO])[constant.ISSUE_ID].count().reset_index(name="Count")
		df2 = df[[constant.CODED_BY, constant.ISSUE_ID]]
		df2 = df2.groupby([constant.CODED_BY])[constant.ISSUE_ID].count().reset_index(name="Count")


		layout = dbc.Container([
				dbc.Row([
						dbc.Col([
						dbc.Card([
								dbc.CardHeader("Description Here"),
								dbc.CardBody([
										html.H2("01", className="card-text")
										]),
								],
						className="shadow p-3 bg-light rounded")
						],
						width=3),
						dbc.Col([
						dbc.Card([
								dbc.CardHeader("Description Here"),
								dbc.CardBody([
										html.H2("02", className="card-text")
										]),
								],
						className="shadow p-3 bg-light rounded")
						],
						width=3),
						dbc.Col([
						dbc.Card([
								dbc.CardHeader("Description Here"),
								dbc.CardBody([
										html.H2("03", className="card-text")
										]),
								],
						className="shadow p-3 bg-light rounded")
						],
						width=3),
						dbc.Col([
						dbc.Card([
								dbc.CardHeader("Description Here"),
								dbc.CardBody([
										html.H2("04", className="card-text")
										]),
								],
						className="shadow p-3 bg-light rounded")
						],
						width=3)
				],
				className= "pb-3"),
				dbc.Row([
						dbc.Col(dbc.Card([
								dbc.CardHeader(f"Total Ticket Count by {constant.ASSIGNED_TO}"),
								app_element.generate_dashtable(identifier = "table1",dataframe = df1)
								],
								className="shadow p-3 bg-light rounded"),
						width=6),
						dbc.Col(dbc.Card([
								dbc.CardHeader(f"Total Ticket Count by {constant.CODED_BY}"),
								app_element.generate_dashtable(identifier = "table2",dataframe = df2)
								],
								className="shadow p-3 bg-light rounded"),
						width=6)
				])
		],
		fluid=True)

		return layout
	except:
		layout = dbc.Jumbotron(
					[
						html.Div([
							html.H1("500: Internal Server Error", className="text-danger"),
							html.Hr(),
							html.P("Following Exception Occured:"),
                            html.Code(traceback.format_exc())
						],
						style=constant.NAVITEM_STYLE)
					]
				)
		return layout


