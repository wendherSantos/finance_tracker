import dash
from dash.dependencies import Input, Output
from dash import dash_table
from dash.dash_table.Format import Group
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from app import app

# =========  Layout  =========== #
layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Legend("Tabela de Despesas"),
                    className="mt-3",
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(id="bar-graph", style={"margin-right": "20px"}),
                    width=9,
                ),
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H4("Despesas"),
                                    html.Legend(
                                        "R$ 4440",
                                        id="valor_despesa_card",
                                        style={"font-size": "60px"},
                                    ),
                                    html.H6("Total de Despesas"),
                                ],
                                style={"textAlign": "center", "padding-top": "30px"},
                            ),
                        ],
                    ),
                    width=3,
                ),
            ],
        ),
    ],
    fluid=True,
    style={"padding": "10px"},
)

# =========  Callbacks  =========== #
# Tabela
