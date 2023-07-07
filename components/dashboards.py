from dash import (
    html,
    dcc,
)  # Importa classes do Dash para criação de elementos HTML e componentes interativos
from dash.dependencies import (
    Input,
    Output,
    State,
)  # Importa classes do Dash para gerenciamento de callbacks
from datetime import (
    date,
    datetime,
    timedelta,
)  # Importa classes para manipulação de datas e horários
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

graph_margin = dict(l=25, r=25, t=25, b=0)

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
                                        html.H5(
                                            "R$ -", id="p-receita-dashboards"
                                        ),  # Valor da receita
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
                                        html.H5(
                                            "R$ -", id="p-despesa-dashboards"
                                        ),  # Valor da despesa
                                    ],
                                    style={
                                        "padding-left": "20px",
                                        "padding-top": "10px",
                                    },  # Estilo do card
                                ),
                                dbc.Card(
                                    html.Div(
                                        className="fa fa-meh-o", style=card_icon
                                    ),  # Ícone do card
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
                                html.Label(
                                    "Categorias das receitas"
                                ),  # Rótulo do dropdown
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
                            style={
                                "height": "100%",
                                "padding": "20px",
                            },  # Estilo do card
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
                    dbc.Card(
                        dcc.Graph(id="graph2"), style={"padding": "10px"}
                    ),  # Gráfico 2
                    width=6,  # Largura da coluna do card
                ),
                dbc.Col(
                    dbc.Card(
                        dcc.Graph(id="graph3"), style={"padding": "10px"}
                    ),  # Gráfico 3
                    width=3,  # Largura da coluna do card
                ),
                dbc.Col(
                    dbc.Card(
                        dcc.Graph(id="graph4"), style={"padding": "10px"}
                    ),  # Gráfico 4
                    width=3,  # Largura da coluna do card
                ),
            ],
            style={"margin": "10px"},  # Estilo da linha
        ),
    ]
)


# =========  Callbacks  =========== #


# Dropdown receita
@app.callback(
    [
        Output("dropdown-receita", "options"),
        Output("dropdown-receita", "value"),
        Output("p-receita-dashboards", "children"),
    ],
    Input("store-receitas", "data"),
)
def populate_dropdownvalues(data):
    df = pd.DataFrame(data)
    valor = df["Valor"].sum()
    val = df.Categoria.unique().tolist()

    return ([{"label": x, "value": x} for x in val], val, f"R${valor}")


# Dropdown despesa
@app.callback(
    [
        Output("dropdown-despesa", "options"),
        Output("dropdown-despesa", "value"),
        Output("p-despesa-dashboards", "children"),
    ],
    Input("store-despesas", "data"),
)
def populate_dropdownvalues(data):
    df = pd.DataFrame(data)
    valor = df["Valor"].sum()
    val = df.Categoria.unique().tolist()

    return ([{"label": x, "value": x} for x in val], val, f"R${valor}")


# VALOR - saldo
@app.callback(
    Output("p-saldo-dashboards", "children"),
    [Input("store-despesas", "data"), Input("store-receitas", "data")],
)
def saldo_total(despesas, receitas):
    df_despesas = pd.DataFrame(despesas)
    df_receitas = pd.DataFrame(receitas)

    valor = df_receitas["Valor"].sum() - df_despesas["Valor"].sum()

    return f"R$ {valor}"


# Grafico 1
@app.callback(
    Output("graph1", "figure"),
    [
        Input("store-despesas", "data"),
        Input("store-receitas", "data"),
        Input("dropdown-despesa", "value"),
        Input("dropdown-receita", "value"),
    ],
)
def update_output(data_despesa, data_receita, despesa, receita):
    df_despesas = pd.DataFrame(data_despesa).set_index("Data")[["Valor"]]
    df_ds = df_despesas.groupby("Data").sum().rename(columns={"Valor": "Despesa"})

    df_receitas = pd.DataFrame(data_receita).set_index("Data")[["Valor"]]
    df_rc = df_receitas.groupby("Data").sum().rename(columns={"Valor": "Receita"})

    df_acum = df_ds.join(df_rc, how="outer").fillna(0)
    df_acum["Acum"] = df_acum["Receita"] - df_acum["Despesa"]
    df_acum["Acum"] = df_acum["Acum"].cumsum()

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            name="Fluxo de caixa", x=df_acum.index, y=df_acum["Acum"], mode="lines"
        )
    )

    fig.update_layout(margin=graph_margin, height=400)
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

    return fig


# Grafico 2
@app.callback(
    Output("graph2", "figure"),
    [
        Input("store-receitas", "data"),
        Input("store-despesas", "data"),
        Input("dropdown-receita", "value"),
        Input("dropdown-despesa", "value"),
        Input("date-picker-config", "start_date"),
        Input("date-picker-config", "end_date"),
    ],
)
def graph2_show(data_receita, data_despesa, receita, despesa, start_date, end_date):
    df_ds = pd.DataFrame(data_despesa)
    df_rc = pd.DataFrame(data_receita)

    df_ds["Output"] = "Despesas"
    df_rc["Output"] = "Receitas"
    df_final = pd.concat([df_ds, df_rc])
    df_final["Data"] = pd.to_datetime(df_final["Data"])

    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    df_final = df_final[(df_final["Data"] >= start_date) & (df_final["Data"] <= end_date)]
    df_final = df_final[(df_final["Categoria"].isin(receita)) | (df_final["Categoria"].isin(despesa))]

    fig = px.bar(df_final, x="Data", y="Valor", color="Output", barmode="group")

    fig.update_layout(margin=graph_margin, height=350)
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

    return fig

# Gráfico 3
@app.callback(
    Output('graph3', "figure"),
    [Input('store-receitas', 'data'),
    Input('dropdown-receita', 'value'),]
)
def pie_receita(data_receita, receita):
    df = pd.DataFrame(data_receita)
    df = df[df['Categoria'].isin(receita)]

    fig = px.pie(df, values=df.Valor, names=df.Categoria, hole=.2)
    fig.update_layout(title={'text': "Receitas"})
    fig.update_layout(margin=graph_margin, height=350)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                  
    return fig    

# Gráfico 4
@app.callback(
    Output('graph4', "figure"),
    [Input('store-despesas', 'data'),
    Input('dropdown-despesa', 'value')]
)
def pie_despesa(data_despesa, despesa):
    df = pd.DataFrame(data_despesa)
    df = df[df['Categoria'].isin(despesa)]

    fig = px.pie(df, values=df.Valor, names=df.Categoria, hole=.2)
    fig.update_layout(title={'text': "Despesas"})

    fig.update_layout(margin=graph_margin, height=350)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

    return fig