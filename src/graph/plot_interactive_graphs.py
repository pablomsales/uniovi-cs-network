import os
from typing import Dict

import networkx as nx
from pyvis.network import Network


def plot_DiGraph(graph: nx.DiGraph, filename: str) -> None:
    """
    Grafica un grafo dirigido y lo guarda como archivo interactivo.

    Params:
    -------
    graph : nx.DiGraph
        El grafo dirigido a ser graficado.

    filename : str
        El nombre del archivo donde se guardará el grafo.

    Returns:
    --------
    None
    """

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


def plot_graph_with_degree_size(
    graph: nx.Graph, degrees: Dict[str, float], filename: str
) -> None:
    """
    Grafica un grafo con tamaños de nodo proporcionales a los grados y guarda el resultado como archivo interactivo.

    Params:
    -------
    graph : nx.Graph
        El grafo a ser graficado.

    degrees : Dict[str, float]
        Un diccionario que mapea los nombres de los nodos a sus grados correspondientes.

    filename : str
        El nombre del archivo donde se guardará el grafo.

    Returns:
    --------
    None
    """

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


def plot_graph_with_communities(
    graph: nx.Graph,
    communities: Dict[str, int],
    degrees: Dict[str, float],
    filename: str,
) -> None:
    """
    Grafica un grafo con comunidades y tamaños de nodo proporcionales a los grados, y guarda el resultado como archivo interactivo.

    Params:
    -------
    graph : nx.Graph
        El grafo a ser graficado.

    communities : Dict[str, int]
        Un diccionario que mapea los nombres de los nodos a los números de las comunidades a las que pertenecen.

    degrees : Dict[str, float]
        Un diccionario que mapea los nombres de los nodos a sus grados correspondientes.

    filename : str
        El nombre del archivo donde se guardará el grafo.

    Returns:
    --------
    None
    """

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
