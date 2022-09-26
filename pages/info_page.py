import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd

##############################################
#  Functions
##############################################

##############################################
#  Layout
##############################################

dash.register_page(__name__, path="/about")

layout = html.Div(children=[
    html.H1("About page"),
    html.Br(),
    html.Center(
        [
            html.H3("Under construction"),
            html.Br(),
            html.Img(
                src="https://www.westend61.de/images/0001177018pw/blacksmith-working-with-hammer-at-anvil-in-his-workshop-ABZF02301.jpg",
                className="under-construction-img"
            )
        ]
    )
])