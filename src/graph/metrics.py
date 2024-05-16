import os
from typing import List

import networkx as nx


def save_metric(metric_list: List[tuple], is_digraph: bool, filename: str) -> None:
    """
    Guarda una lista de métricas en un archivo.

    Params:
    -------
    metric_list : List[tuple]
        La lista de tuplas que contienen nodos y valores de métricas.
    is_digraph : bool
        Indica si el grafo es dirigido o no dirigido.
    filename : str
        El nombre del archivo donde se guardará la métrica.

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
    graph : nx.Graph
        El grafo para el cual se calculará la métrica.
    metric : str
        La métrica de centralidad a calcular. Puede tomar los valores: "betweenness", "closeness" o "in_degree".
    is_digraph : bool
        Indica si el grafo es dirigido o no dirigido.
    filename : str
        El nombre del archivo donde se guardará la métrica calculada.

    Returns:
    --------
    None

    Raises:
    -------
    ValueError
        Si la métrica especificada no es soportada.
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
