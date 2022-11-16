import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc

from pages import page1, page2


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True,
                title="Toast Example", )

app.layout = html.Div([
    dcc.Location(id="url"),
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Page 1", href="/page1")),
            dbc.NavItem(dbc.NavLink("Page 2", href="/page2")),
        ], brand="Navbar"
    ),
    html.Div(id="layout")
])

@app.callback(Output("layout", "children"), [Input("url", "pathname")])
def set_layout(pathname):
    if pathname == "/page1":
        return page1.layout
    elif pathname == "/page2":
        return page2.layout
    return html.H2("404: not found")


if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")
