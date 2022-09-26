# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

#######################################
### Callbacks
#######################################

#######################################
### Main code
#######################################

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        dbc.icons.FONT_AWESOME
    ]
)

sidebar = html.Div([
    dbc.Nav(
        [
            dbc.NavLink(
                html.I(className="fa-solid fa-square-rss"),  
                href="/",
                active="exact",
                id="data-viz-navlink"
            ),
            dbc.NavLink(
                html.I(className="fa-solid fa-chart-simple"),
                href="/stats",
                active="exact",
                id="stats-navlink"
            ),
            dbc.NavLink(
                html.I(className="fa-solid fa-gear"),
                href="/config",
                active="exact",
                id="config-navlink"
            )
        ],
        pills=True,
        vertical=True,
        class_name='sidebar ms-auto text-center'
    ),
    dbc.Nav(
        [
            dbc.NavLink(
                html.I(className="fa-solid fa-info"),
                href="/about",
                disabled=True,
                active="exact",
                id="about-navlink"
            ),
            dbc.NavLink(
                html.I(className="fa-solid fa-circle-question"),
                href="/help",
                active="exact",
                id="help-navlink"
            )
        ],
        pills=True,
        vertical=True,
        class_name='infobar mb-auto text-center'
    ),
    dbc.Tooltip(
        "Data visualization",
        target="data-viz-navlink",
        placement="right"
    ),
    dbc.Tooltip(
        "App stats",
        target="stats-navlink",
        placement="right"
    ),
    dbc.Tooltip(
        "Settings",
        target="config-navlink",
        placement="right"
    ),
    dbc.Tooltip(
        "About",
        target="about-navlink",
        placement="right"
    ),
    dbc.Tooltip(
        "Help",
        target="help-navlink",
        placement="right"
    )
],
    className='sidebar-div bg-light d-flex flex-column'
)

app.layout = html.Div([
    sidebar,
    html.Div([dash.page_container], className='main-content-div')
],
    className='main-div d-flex flex-column'
)

if __name__ == '__main__':
    app.run_server(debug=True)
