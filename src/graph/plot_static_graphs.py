import os
from typing import Dict

import matplotlib.pyplot as plt
import networkx as nx


def plot_graph(graph: nx.Graph, filename: str) -> None:
    """
    Crea y guarda un gráfico de un grafo dado.

    Params:
    -------
    graph : nx.Graph
        El grafo que se dibujará.
    filename : str
        El nombre del archivo donde se guardará el gráfico.

    Returns:
    --------
    None
    """

    fig = plt.figure(figsize=(15, 15))
    pos = nx.spring_layout(graph, seed=12, k=0.1)
    nx.draw(graph, pos=pos, with_labels=True, width=0.5, node_size=100, font_size=4)
    plt.axis("equal")

    fig.savefig(os.path.join("outputs", "static", filename))


def plot_graph_with_degree_size(graph: nx.Graph, degrees: dict, filename: str) -> None:
    """
    Crea y guarda un gráfico de un grafo con nodos de tamaño proporcional a su grado.

    Params:
    -------
    graph : nx.Graph
        El grafo que se dibujará.
    degrees : dict
        Un diccionario que mapea nodos a sus grados.
    filename : str
        El nombre del archivo donde se guardará el gráfico.

    Returns:
    --------
    None
    """

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


def plot_graph_with_communities(
    graph: nx.Graph, communities: Dict, degrees: Dict, filename: str
) -> None:
    """
    Crea y guarda un gráfico de un grafo con nodos coloreados según comunidades y tamaño proporcional a su grado.

    Params:
    -------
    graph : nx.Graph
        El grafo que se dibujará.
    communities : dict
        Un diccionario que mapea nodos a sus comunidades.
    degrees : dict
        Un diccionario que mapea nodos a sus grados.
    filename : str
        El nombre del archivo donde se guardará el gráfico.

    Returns:
    --------
    None
    """

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
