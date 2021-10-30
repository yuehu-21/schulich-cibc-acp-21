# -*- coding: utf-8 -*-

import pandas as pd
import json
from pyecharts import options as opts
from pyecharts.charts import Graph

df_links = pd.read_csv("links.csv")
df_categories = pd.read_csv("categories.csv")
df_nodes = pd.read_csv("nodes.csv")

links =  df_links.to_dict('records')
categories = df_categories.to_dict('records')
nodes =  df_nodes.to_dict('records')


c = (
    Graph(init_opts=opts.InitOpts(width="2000px", height="1200px"))
    .add(
        "",
        nodes,
        links,
        categories,
        repulsion=50,
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        legend_opts=opts.LegendOpts(orient="vertical", pos_left="2%", pos_top="20%"),
        title_opts=opts.TitleOpts(title="High Net Worth Canadian Executives Connection Graph"),
    )
    .render("graph_2.html")
)


