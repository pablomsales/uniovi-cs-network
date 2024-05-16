import os
from typing import Dict, Iterable, List, Tuple

import networkx as nx
from community import community_louvain

from graph import plot_interactive_graphs, plot_static_graphs
from graph.graph_maker import get_DiGraph, get_graph, get_relations
from scrapper.json_generator import load_thesis_json, save_thesis_json


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
    simple_graph = get_graph(relations)
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
    graph_deg = get_graph(relations)
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
    graph_louvain = get_graph(relations)
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


def save_metric(metric_list: List[tuple], is_digraph: bool, filename: str) -> None:
    """
    Guarda una lista de métricas en un archivo.

    Params:
    -------
    - metric_list (List[tuple]): La lista de tuplas que contienen nodos y valores de métricas.
    - is_digraph (bool): indica si el grafo es dirigido o no dirigido.
    - filename (str): El nombre del archivo donde se guardará la métrica.

    Returns:
    --------
    - None
    """

    if is_digraph:
        output_file = os.path.join("outputs", "interactive", filename)
    else:
        output_file = os.path.join("outputs", "static", filename)

    with open(output_file, "w") as f:
        for node, metric_value in metric_list:
            f.write(f"{node}: {str(metric_value)}\n")


def get_metric(graph: nx.Graph, metric: str, is_digraph: bool, filename: str) -> None:
    """
    Calcula y guarda una métrica de centralidad para un grafo dado.

    Params:
    -------
    - graph (nx.Graph): El grafo para el cual se calculará la métrica.
    - metric (str): La métrica de centralidad a calcular. Puede tomar los valores: "betweenness", "closeness" o "in_degree".
    - is_digraph (bool): indica si el grafo es dirigido o no dirigido.
    - filename (str): El nombre del archivo donde se guardará la métrica calculada.

    Returns:
    --------
    - None

    Raises:
    -------
    - ValueError: Si la métrica especificada no es soportada.
    """

    metrics_map = {
        "betweenness": nx.betweenness_centrality,
        "closeness": nx.closeness_centrality,
        "in_degree": nx.in_degree_centrality,
    }

    if metric in metrics_map:
        compute_metric = metrics_map[metric]
        values = compute_metric(graph)
    else:
        raise ValueError("Metrica no soportada: {}".format(metric))

    sorted_values = sorted(values.items(), key=lambda x: x[1], reverse=True)
    save_metric(sorted_values, is_digraph, filename)


def main():

    # hacemos el scrapping si no tenemos los datos
    filename = os.path.join("data", "thesis.json")
    if not os.path.exists(filename):
        os.makedirs("data", exist_ok=True)
        save_thesis_json(filename)

    # cargamos los datos
    data = load_thesis_json(filename)
    relations = get_relations(data)

    # creamos directorios para guardar grafos
    static_graphs_dir = os.path.join("outputs", "static")
    interactive_graphs_dir = os.path.join("outputs", "interactive")

    for dir in [static_graphs_dir, interactive_graphs_dir]:
        if not os.path.exists(dir):
            os.makedirs(dir)

    # obtenemos grafos simples
    simple_graph, simple_digraph = get_simple_graphs(relations)

    # obtenemos grafos con centralidad de grado
    graph_deg, degrees, degrees_DiG = get_degree_graphs(relations)

    degrees_sorted = sorted(degrees.items(), key=lambda x: x[1], reverse=True)
    save_metric(
        degrees_sorted,
        is_digraph=False,
        filename="degree_centrality.txt",
    )

    degrees_DiG_sorted = sorted(degrees_DiG.items(), key=lambda x: x[1], reverse=True)
    save_metric(
        degrees_DiG_sorted,
        is_digraph=True,
        filename="degree_centrality_digraph.txt",
    )

    # obtenemos grafos con comunidades
    get_communities_graphs(relations, graph_deg, degrees, degrees_DiG)

    get_metric(
        simple_graph,
        "betweenness",
        is_digraph=False,
        filename="betweenness_centrality.txt",
    )
    get_metric(
        simple_digraph,
        "betweenness",
        is_digraph=True,
        filename="betweenness_centrality_digraph.txt",
    )

    # Closeness
    get_metric(
        simple_graph,
        "closeness",
        is_digraph=False,
        filename="closeness_centrality.txt",
    )
    get_metric(
        simple_digraph,
        "closeness",
        is_digraph=True,
        filename="closeness_centrality_digraph.txt",
    )

    # Prestigio
    get_metric(
        simple_digraph,
        "in_degree",
        is_digraph=True,
        filename="in_degree_centrality.txt",
    )


if __name__ == "__main__":
    main()
