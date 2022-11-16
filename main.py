import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True,
                title="Toast Example", use_pages=True, pages_folder="layouts")

app.layout = html.Div([
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Page 1", href="/page1")),
            dbc.NavItem(dbc.NavLink("Page 2", href="/page2")),
        ], brand="Navbar"
    ),
    html.Div([
        dash.page_container
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")

