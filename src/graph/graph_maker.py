from typing import Dict, Iterable, Tuple

import networkx as nx
from community import community_louvain

from graph import plot_interactive_graphs, plot_static_graphs


def get_relations(data: dict) -> set:
    """
    Obtiene relaciones entre autores y directores de tesis de los datos proporcionados.

    Params:
    -------
    data : dict
        Un diccionario que contiene datos de tesis organizados por año y ID.

    Returns:
    --------
    set
        Un conjunto de tuplas que representan relaciones entre autores y directores de tesis.
    """

    relations = []

    for year in data.keys():
        for id in data[year].keys():
            author = data[year][id]["author"]
            directors = data[year][id]["directors"]

            thesis_relations = [(author, director) for director in directors]
            relations.extend(thesis_relations)

    # Eliminamos posibles duplicados (al menos Francisco Javier Gil Gala)
    relations = set(relations)

    return relations


def get_Graph(relations: Iterable[tuple]) -> nx.Graph:
    """
    Crea un grafo no dirigido a partir de las relaciones proporcionadas.

    Params:
    -------
    relations : Iterable[tuple]
        Una secuencia de tuplas que representan relaciones entre nodos.

    Returns:
    --------
    nx.Graph
        Un objeto grafo no dirigido de NetworkX.
    """

    graph = nx.Graph()

    # Añadimos nodos y aristas
    for rel in relations:
        author, director = rel
        graph.add_edge(author, director)

    return graph


def get_DiGraph(relations: Iterable[tuple]) -> nx.DiGraph:
    """
    Crea un grafo dirigido a partir de las relaciones proporcionadas.

    Params:
    ----------
    relations : Iterable[tuple]
        Una secuencia de tuplas que representan relaciones entre nodos.

    Returns:
    ----------
    nx.DiGraph
        Un objeto grafo dirigido de NetworkX.
    """

    DiGraph = nx.DiGraph()

    # Añadimos nodos y aristas
    for rel in relations:
        author, director = rel
        DiGraph.add_edge(author, director)

    return DiGraph


def get_simple_graphs(relations: Iterable[tuple]) -> Tuple[nx.Graph, nx.DiGraph]:
    """
    Obtiene y visualiza grafos simples a partir de las relaciones proporcionadas.

    Params:
    -------
    relations : Iterable[tuple]
        Una secuencia de tuplas que representan relaciones entre nodos.

    Returns:
    --------
    Tuple[nx.Graph, nx.DiGraph]
        Una tupla que contiene un grafo no dirigido y un grafo dirigido, respectivamente.
    """

    # obtenemos grafo simple
    simple_graph = get_Graph(relations)
    plot_static_graphs.plot_graph(simple_graph, "thesis_simple.svg")

    # obtenemos grafo simple DIRIGIDO
    simple_digraph = get_DiGraph(relations)
    plot_interactive_graphs.plot_DiGraph(simple_digraph, "thesis_interactive.html")

    return simple_graph, simple_digraph


def get_degree_graphs(
    relations: Iterable[tuple],
) -> Tuple[nx.Graph, Dict[str, float], Dict[str, float]]:
    """
    Obtiene y visualiza grafos con centralidad de grado a partir de las relaciones proporcionadas.

    Params:
    -------
    relations : Iterable[tuple]
        Una secuencia de tuplas que representan relaciones entre nodos.

    Returns:
    --------
    Tuple[nx.Graph, Dict[str, float], Dict[str, float]]
        Una tupla que contiene un grafo no dirigido, un diccionario de centralidades de grado para el grafo no dirigido y otro diccionario de centralidades de grado para el grafo dirigido, respectivamente.
    """

    # obtenemos grafo NO dirigido con centralidad de grado
    graph_deg = get_Graph(relations)
    degrees = nx.degree_centrality(graph_deg)
    plot_static_graphs.plot_graph_with_degree_size(
        graph_deg,
        degrees,
        "thesis_degree.svg",
    )

    # obtenemos grafo DIRIGIDO con centralidad de grado
    digraph_deg = get_DiGraph(relations)
    degrees_DiG = nx.degree_centrality(graph_deg)
    plot_interactive_graphs.plot_graph_with_degree_size(
        digraph_deg,
        degrees_DiG,
        "thesis_degree_interactive.html",
    )

    return graph_deg, degrees, degrees_DiG


def get_communities_graphs(
    relations: Iterable[tuple],
    graph_deg: nx.Graph,
    degrees: Dict[str, float],
    degrees_DiG: Dict[str, float],
) -> None:
    """
    Obtiene y visualiza grafos con detección de comunidades a partir de las relaciones proporcionadas.

    Params:
    -------
    relations : Iterable[tuple]
        Una secuencia de tuplas que representan relaciones entre nodos.

    graph_deg : nx.Graph
        El grafo no dirigido con centralidad de grado.

    degrees : Dict[str, float]
        Un diccionario que mapea los nombres de los nodos a sus grados correspondientes en el grafo no dirigido.

    degrees_DiG : Dict[str, float]
        Un diccionario que mapea los nombres de los nodos a sus grados correspondientes en el grafo dirigido.

    Returns:
    --------
    None
    """

    # obtenemos grafo NO dirigido con comunidades
    graph_louvain = get_Graph(relations)
    communities = community_louvain.best_partition(graph_louvain)
    plot_static_graphs.plot_graph_with_communities(
        graph_deg,
        communities,
        degrees,
        "thesis_communities.svg",
    )

    # obtenemos grafo DIRIGIDO con comunidades
    digraph_louvain = get_DiGraph(relations)
    plot_interactive_graphs.plot_graph_with_communities(
        digraph_louvain,
        communities,
        degrees_DiG,
        "thesis_communities_interactive.html",
    )
