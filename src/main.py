import os

import networkx as nx
from community import community_louvain

from graph import plot_interactive_graphs, plot_static_graphs
from graph.graph_and_metrics import get_DiGraph, get_graph, get_relations
from scrapper.json_generator import load_thesis_json, save_thesis_json


def get_simple_graphs(relations):

    # obtenemos grafo simple
    simple_graph = get_graph(relations)
    plot_static_graphs.plot_graph(simple_graph, "thesis_simple.svg")

    # obtenemos grafo simple DIRIGIDO
    simple_digraph = get_DiGraph(relations)
    plot_interactive_graphs.plot_DiGraph(simple_digraph, "thesis_interactive.html")

    return simple_graph, simple_digraph


def get_degree_graphs(relations):

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


def get_communities_graphs(relations, graph_deg, degrees, degrees_DiG):

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


def save_metric(metric_list, is_digraph: bool, filename):

    if is_digraph:
        output_file = os.path.join("outputs", "interactive", filename)
    else:
        output_file = os.path.join("outputs", "static", filename)

    with open(output_file, "w") as f:
        for node, metric_value in metric_list:
            f.write(f"{node}: {str(round(metric_value, 6))}\n")


def get_betweenness(graph, is_digraph: bool, filename):
    betweenness = nx.betweenness_centrality(graph)
    betweenness_sorted = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)
    save_metric(betweenness_sorted, is_digraph, filename)


def get_closeness(graph, is_digraph: bool, filename):
    closeness = nx.closeness_centrality(graph)
    closeness_sorted = sorted(closeness.items(), key=lambda x: x[1], reverse=True)
    save_metric(closeness_sorted, is_digraph, filename)


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

    # obtenemos betweenness para los dos grafos (dirigido y no dirigido)
    get_betweenness(
        simple_graph,
        is_digraph=False,
        filename="betweenness_centrality.txt",
    )
    get_betweenness(
        simple_digraph,
        is_digraph=True,
        filename="betweenness_centrality_digraph.txt",
    )

    # obtenemos closeness para los dos grafos (dirigido y no dirigido)
    get_closeness(
        simple_graph,
        is_digraph=False,
        filename="closeness_centrality.txt",
    )
    get_closeness(
        simple_digraph,
        is_digraph=True,
        filename="closeness_centrality_digraph.txt",
    )


if __name__ == "__main__":
    main()
