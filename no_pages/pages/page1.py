import dash
import dash_bootstrap_components as dbc
from dash import html, Output, Input, callback


layout = html.Div([
    html.P("Page 1"),
    html.H5("Steps to reproduce:"),
    html.P("1. Trigger Toast with below button"),
    html.P("2. Navigate to Page 2 before toast dismisses"),
    dbc.Button("Trigger Toast", id="toast_trigger", n_clicks=0),
    html.Div([
        dbc.Toast(f"Some words",
                  header=f"Header",
                  dismissable=True,
                  icon="success",
                  duration=4000,
                  is_open=False,
                  id="toast")
    ])
])


@callback(
    Output("toast", "is_open"),
    Input("toast_trigger", "n_clicks")
)
def trigger_toast(n_clicks):
    if n_clicks:
        return True
