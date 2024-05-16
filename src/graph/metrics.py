import os
from typing import List

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def plot_metric(metric_list: List[tuple], output_dir: str, filename: str):
    """
    Crea y guarda un gráfico de barras con los 10 primeros individuos de una métrica.

    Params:
    -------
    metric_list : List[tuple]
        Lista de tuplas que contienen los nombres y valores de la métrica.
    output_dir : str
        Directorio de salida donde se guardará el gráfico.
    filename : str
        Nombre del archivo de la métrica.

    Returns:
    --------
    None
    """

    # Creamos y guardamos el gráfico de barras con los 10 primeros individuos
    names = [item[0] for item in metric_list[:10]]
    values = [item[1] for item in metric_list[:10]]

    metric = filename.split(".")[0]

    # Creamos un rango de colores basado en los valores de la métrica usando el colormap 'viridis'
    colors = plt.cm.viridis(np.linspace(0, 1, len(values)))

    plt.figure(figsize=(10, 6))
    plt.bar(names, values, color=colors)
    plt.ylabel(f"Valor de {metric}")
    plt.title(f"Top 10 Individuos por {metric}")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # Guardamos el gráfico en la misma ruta que el archivo de métricas
    graph_filename = metric + "_barplot.svg"
    graph_output_file = os.path.join(output_dir, graph_filename)
    plt.savefig(graph_output_file)

    # Cerramos el gráfico para liberar recursos
    plt.close()


def save_metric(metric_list: List[tuple], is_digraph: bool, filename: str) -> None:
    """
    Guarda una lista de métricas en un archivo y los barplots asociados en el mismo directorio.

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

    metrics_dir = "interactive" if is_digraph else "static"
    metrics_dir = os.path.join(metrics_dir, "metrics")

    output_dir = os.path.join("outputs", metrics_dir)
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, filename)

    with open(output_file, "w") as f:
        for node, metric_value in metric_list:
            f.write(f"{node}: {str(metric_value)}\n")

    plot_metric(metric_list, output_dir, filename)


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
