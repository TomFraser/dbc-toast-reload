import dash
import dash_bootstrap_components as dbc
from dash import html, Output, Input, callback


layout = html.Div(
    [
        # If you uncomment the lines below, you will see the same error as on page1

        # html.P("Page 3"),
        # html.H5("Steps to reproduce:"),
        # html.P("1. Trigger Toast with below button"),
        # html.P("2. Navigate to Page 2 before toast dismisses"),
        dbc.Button("Trigger Toast", id="page3-toast_trigger", n_clicks=0),
        dbc.Toast(
            f"Some words",
            header=f"Header",
            dismissable=True,
            icon="success",
            duration=4000,
            is_open=False,
            id="page3-toast",
        ),
    ]
)


@callback(Output("page3-toast", "is_open"), Input("page3-toast_trigger", "n_clicks"))
def trigger_toast(n_clicks):
    if n_clicks:
        return True

