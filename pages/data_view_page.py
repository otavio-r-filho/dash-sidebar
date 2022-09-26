import os
import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd
from glob import glob

##############################################
#  Functions
##############################################


##############################################
#  Layout
##############################################

dash.register_page(__name__, path="/")

# df_news = load_data()

layout = html.Div(children=[
    html.H1("Data visualization page"),
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