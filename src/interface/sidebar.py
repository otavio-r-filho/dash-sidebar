import logging
from dash import html
import dash_bootstrap_components as dbc


def build_nav(lst_links):
    nav_links = []
    nav_tooltips = []

    for link_dict in lst_links:
        nav_links.append(
            dbc.NavLink(
                link_dict.get("text"),
                href=link_dict.get("href"),
                active="exact",
                id=link_dict.get("id")
            )
        )
        if "tooltip" in link_dict:
            nav_tooltips.append(
                dbc.Tooltip(
                    link_dict.get("tooltip"),
                    target=link_dict.get("id"),
                    placement="right"
                )
            )
    nav = dbc.Nav(
        children=nav_links,
        pills=True,
        vertical=True,
        class_name='mb-auto text-center'
    )

    return nav, nav_tooltips



def build_sidebar(top_links, bottom_links=None):
    sidebar_children = []

    top_nav, top_tooltips = build_nav(top_links)
    top_nav.style = {"height": "100%"}

    sidebar_children.append(top_nav)
    if len(top_tooltips) > 0:
        sidebar_children.append(top_tooltips)

    if bottom_links is not None and len(bottom_links) > 0:
        bottom_nav, bottom_tooltips = build_nav(bottom_links)
        sidebar_children.append(bottom_nav)
        if len(bottom_tooltips) > 0:
            sidebar_children.append(bottom_tooltips)
    
    sidebar = html.Div(
        children=sidebar_children,
        className="bg-light d-flex flex-column",
        style={
            "position": "fixed",
            "top": "0",
            "left": "0",
            "bottom": "0",
            "width": "3rem",
            "padding-top": "1rem",
            "padding-bottom": "1rem",
        }
    )

    return sidebar