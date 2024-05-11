import os

import matplotlib.pyplot as plt
import networkx as nx


def plot_graph(graph, filename):

    fig = plt.figure(figsize=(15, 15))
    pos = nx.spring_layout(graph, seed=12, k=0.1)
    nx.draw(graph, pos=pos, with_labels=True, width=0.5, node_size=100, font_size=4)
    plt.axis("equal")
    plt.show()

    fig.savefig(os.path.join("outputs", "static", filename))


def plot_graph_with_degree_size(graph, degrees, filename):

    node_sizes = [deg * 10000 for deg in degrees.values()]
    node_colors = list(degrees.values())

    fig = plt.figure(figsize=(13, 13))

    pos = nx.spring_layout(graph, seed=12, k=0.14)
    nx.draw(
        graph,
        pos=pos,
        with_labels=True,
        width=0.5,
        font_size=3.5,
        font_color="black",
        node_size=node_sizes,
        node_color=node_colors,
        cmap=plt.cm.viridis,
        alpha=0.9,
    )
    plt.axis("equal")
    fig.savefig(os.path.join("outputs", "static", filename))


def plot_graph_with_communities(graph, communities, degrees, filename):

    node_sizes = [deg * 10000 for deg in degrees.values()]
    node_colors = list(communities.values())

    fig = plt.figure(figsize=(13, 13))

    pos = nx.spring_layout(graph, seed=12, k=0.14)
    nx.draw(
        graph,
        pos=pos,
        with_labels=True,
        width=0.5,
        font_size=3.5,
        font_color="black",
        node_size=node_sizes,
        node_color=node_colors,
        cmap=plt.cm.viridis,
        alpha=0.9,
    )
    plt.axis("equal")
    fig.savefig(os.path.join("outputs", "static", filename))
