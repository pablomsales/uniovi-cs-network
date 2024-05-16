from typing import Iterable

import networkx as nx


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


def get_graph(relations: Iterable[tuple]) -> nx.Graph:
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
