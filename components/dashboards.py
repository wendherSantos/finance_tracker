from dash import html, dcc  # Importa classes do Dash para criação de elementos HTML e componentes interativos
from dash.dependencies import Input, Output, State  # Importa classes do Dash para gerenciamento de callbacks
from datetime import date, datetime, timedelta  # Importa classes para manipulação de datas e horários
import dash_bootstrap_components as dbc  # Importa componentes estilizados do Bootstrap para o Dash
import pandas as pd  # Importa a biblioteca pandas para manipulação de dados
import numpy as np  # Importa a biblioteca numpy para operações matemáticas em arrays
import plotly.express as px  # Importa a biblioteca Plotly Express para visualizações gráficas
import plotly.graph_objects as go  # Importa a biblioteca Plotly Graph Objects para visualizações gráficas personalizadas
import calendar  # Importa o módulo de calendário
# from globals import *  # Importa módulo personalizado
from app import app  # Importa o objeto app do módulo app

card_icon = {
    "color": "white",
    "textAlign": "center",
    "fontSize": 30,
    "margin": "auto",
}

# =========  Layout  =========== #

# Define a estrutura de layout do painel de controle financeiro
layout = dbc.Col(
    [
        dbc.Row(
            [
                # Saldo
                dbc.Col(
                    [
                        dbc.CardGroup(
                            [
                                dbc.Card(
                                    [
                                        html.Legend("Saldo"),  # Legenda do card
                                        html.H5(
                                            "R$ -", id="p-saldo-dashboards", style={}
                                        ),  # Valor do saldo
                                    ],
                                    style={
                                        "padding-left": "20px",
                                        "padding-top": "10px",
                                    },  # Estilo do card
                                ),
                                dbc.Card(
                                    html.Div(
                                        className="fa fa-university", style=card_icon
                                    ),  # Ícone do card
                                    color="warning",  # Cor de fundo do card
                                    style={
                                        "maxWidth": 75,
                                        "height": 100,
                                        "margin-left": "-10px",
                                    },  # Estilo do card
                                ),
                            ]
                        )
                    ],
                    width=4,  # Largura da coluna do card
                ),
                # Receita
                dbc.Col(
                    [
                        dbc.CardGroup(
                            [
                                dbc.Card(
                                    [
                                        html.Legend("Receita"),  # Legenda do card
                                        html.H5("R$ -", id="p-receita-dashboards"),  # Valor da receita
                                    ],
                                    style={
                                        "padding-left": "20px",
                                        "padding-top": "10px",
                                    },  # Estilo do card
                                ),
                                dbc.Card(
                                    html.Div(
                                        className="fa fa-smile-o", style=card_icon
                                    ),  # Ícone do card
                                    color="success",  # Cor de fundo do card
                                    style={
                                        "maxWidth": 75,
                                        "height": 100,
                                        "margin-left": "-10px",
                                    },  # Estilo do card
                                ),
                            ]
                        )
                    ],
                    width=4,  # Largura da coluna do card
                ),
                # Despesa
                dbc.Col(
                    [
                        dbc.CardGroup(
                            [
                                dbc.Card(
                                    [
                                        html.Legend("Despesas"),  # Legenda do card
                                        html.H5("R$ -", id="p-despesa-dashboards"),  # Valor da despesa
                                    ],
                                    style={
                                        "padding-left": "20px",
                                        "padding-top": "10px",
                                    },  # Estilo do card
                                ),
                                dbc.Card(
                                    html.Div(className="fa fa-meh-o", style=card_icon),  # Ícone do card
                                    color="danger",  # Cor de fundo do card
                                    style={
                                        "maxWidth": 75,
                                        "height": 100,
                                        "margin-left": "-10px",
                                    },  # Estilo do card
                                ),
                            ]
                        )
                    ],
                    width=4,  # Largura da coluna do card
                ),
            ],
            style={"margin": "10px"},  # Estilo da linha
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                html.Legend(
                                    "Filtrar lançamentos", className="card-title"
                                ),  # Legenda do card
                                html.Label("Categorias das receitas"),  # Rótulo do dropdown
                                html.Div(
                                    dcc.Dropdown(
                                        id="dropdown-receita",
                                        clearable=False,
                                        style={"width": "100%"},
                                        persistence=True,
                                        persistence_type="session",
                                        multi=True,
                                    )  # Dropdown das categorias das receitas
                                ),
                                html.Label(
                                    "Categorias das despesas",
                                    style={"margin-top": "10px"},
                                ),  # Rótulo do dropdown
                                dcc.Dropdown(
                                    id="dropdown-despesa",
                                    clearable=False,
                                    style={"width": "100%"},
                                    persistence=True,
                                    persistence_type="session",
                                    multi=True,
                                ),  # Dropdown das categorias das despesas
                                html.Legend(
                                    "Período de Análise", style={"margin-top": "10px"}
                                ),  # Legenda do DatePickerRange
                                dcc.DatePickerRange(
                                    month_format="Do MMM, YY",
                                    end_date_placeholder_text="Data...",
                                    start_date=datetime.today(),
                                    end_date=datetime.today() + timedelta(days=31),
                                    with_portal=True,
                                    updatemode="singledate",
                                    id="date-picker-config",
                                    style={"z-index": "100"},
                                ),  # Intervalo de datas do DatePickerRange
                            ],
                            style={"height": "100%", "padding": "20px"},  # Estilo do card
                        ),
                    ],
                    width=4,  # Largura da coluna do card
                ),
                dbc.Col(
                    dbc.Card(
                        dcc.Graph(id="graph1"),  # Gráfico 1
                        style={"height": "100%", "padding": "10px"},  # Estilo do card
                    ),
                    width=8,  # Largura da coluna do card
                ),
            ],
            style={"margin": "10px"},  # Estilo da linha
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(dcc.Graph(id="graph2"), style={"padding": "10px"}),  # Gráfico 2
                    width=6,  # Largura da coluna do card
                ),
                dbc.Col(
                    dbc.Card(dcc.Graph(id="graph3"), style={"padding": "10px"}),  # Gráfico 3
                    width=3,  # Largura da coluna do card
                ),
                dbc.Col(
                    dbc.Card(dcc.Graph(id="graph4"), style={"padding": "10px"}),  # Gráfico 4
                    width=3,  # Largura da coluna do card
                ),
            ],
            style={"margin": "10px"},  # Estilo da linha
        ),
    ]
)

# =========  Callbacks  =========== #

