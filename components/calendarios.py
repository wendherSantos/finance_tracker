from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from datetime import date, datetime

from app import app

# =========  Componentes  =========== #

# Componente de calendário 1
calendario1 = html.Div(
    [
        dcc.DatePickerSingle(
            id="date_picker_single",
            min_date_allowed=datetime.today(),
            max_date_allowed=date(2030, 12, 31),
            initial_visible_month=datetime.today(),
            date=datetime.today(),
            display_format="DD/MM/YYYY",  # Define o formato da data
        ),
        html.Div(id="output_container_datepicker"),
    ]
)

# Componente de calendário 2
calendario2 = html.Div(
    [
        dcc.DatePickerSingle(
            id="date_picker_single2",
            min_date_allowed=datetime.today(),
            max_date_allowed=date(2030, 12, 31),
            initial_visible_month=datetime.today(),
            date=datetime.today(),
            display_format="DD/MM/YYYY",  # Define o formato da data
        ),
        html.Div(id="output_container_datepicker2"),
    ]
)


# =========  Callbacks  =========== #

# Callback para atualizar a saída do calendário 1
@app.callback(
    Output("output_container_datepicker", "children"),
    Input("date_picker_single", "date"),
)
def update_output(date_value):
    string_prefix = "Selecionado: "
    if date_value is not None:
        date_object = date.fromisoformat(date_value)
        date_string = date_object.strftime("%d/%m/%Y")  # Formata a data para DD/MM/AAAA
        return string_prefix + date_string


# Callback para atualizar a saída do calendário 2
@app.callback(
    Output("output_container_datepicker2", "children"),
    Input("date_picker_single2", "date"),
)
def update_output(date_value):
    string_prefix = "Selecionado: "
    if date_value is not None:
        date_object = date.fromisoformat(date_value)
        date_string = date_object.strftime("%d/%m/%Y")  # Formata a data para DD/MM/AAAA
        return string_prefix + date_string
