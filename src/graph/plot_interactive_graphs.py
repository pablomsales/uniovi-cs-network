import os

import networkx as nx
from pyvis.network import Network


def plot_DiGraph(graph, filename):

    dinet = Network(
        notebook=True,
        width="1920px",
        height="1080px",
        bgcolor="#222222",
        font_color="white",
        directed=True,
    )

    dinet.from_nx(graph)
    dinet.save_graph(os.path.join("outputs", "interactive", filename))


def plot_graph_with_degree_size(graph, degrees, filename):

    # modificamos las puntuaciones para visualizarlas mejor
    node_sizes = {k: v * 800 for k, v in degrees.items()}

    dinet = Network(
        notebook=True,
        width="1920px",
        height="1080px",
        bgcolor="#222222",
        font_color="white",
        directed=True,
    )
    nx.set_node_attributes(graph, node_sizes, "size")
    dinet.from_nx(graph)
    dinet.save_graph(os.path.join("outputs", "interactive", filename))


def plot_graph_with_communities(graph, communities, degrees, filename):

    node_sizes = {k: v * 800 for k, v in degrees.items()}

    dinet = Network(
        notebook=True,
        width="1920px",
        height="1080px",
        bgcolor="#222222",
        font_color="white",
        directed=True,
    )
    nx.set_node_attributes(graph, node_sizes, "size")
    nx.set_node_attributes(graph, communities, "group")
    dinet.from_nx(graph)
    dinet.save_graph(os.path.join("outputs", "interactive", filename))
