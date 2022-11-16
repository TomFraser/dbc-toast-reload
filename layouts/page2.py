import dash
from dash import html

dash.register_page(__name__, path="/page2")

layout = html.Div([
    html.P("Page 2"),
    html.P("Wait for it...")
])
