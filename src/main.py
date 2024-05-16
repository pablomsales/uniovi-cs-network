import os

from graph import graph_maker, metrics
from scrapper.json_generator import load_thesis_json, save_thesis_json


def main():

    # hacemos el scrapping si no tenemos los datos
    filename = os.path.join("data", "thesis.json")
    if not os.path.exists(filename):
        os.makedirs("data", exist_ok=True)
        save_thesis_json(filename)

    # cargamos los datos
    data = load_thesis_json(filename)
    relations = graph_maker.get_relations(data)

    # creamos directorios para guardar grafos
    static_graphs_dir = os.path.join("outputs", "static")
    interactive_graphs_dir = os.path.join("outputs", "interactive")

    for dir in [static_graphs_dir, interactive_graphs_dir]:
        os.makedirs(dir, exist_ok=True)

    # obtenemos grafos simples
    simple_graph, simple_digraph = graph_maker.get_simple_graphs(relations)

    # obtenemos grafos con centralidad de grado
    graph_deg, degrees, degrees_DiG = graph_maker.get_degree_graphs(relations)

    degrees_sorted = sorted(degrees.items(), key=lambda x: x[1], reverse=True)
    metrics.save_metric(
        degrees_sorted,
        is_digraph=False,
        filename="degree_centrality.txt",
    )

    degrees_DiG_sorted = sorted(degrees_DiG.items(), key=lambda x: x[1], reverse=True)
    metrics.save_metric(
        degrees_DiG_sorted,
        is_digraph=True,
        filename="degree_centrality_digraph.txt",
    )

    # obtenemos grafos con comunidades
    graph_maker.get_communities_graphs(relations, graph_deg, degrees, degrees_DiG)

    # BETWEENNESS
    metrics.get_metric(
        simple_graph,
        "betweenness",
        is_digraph=False,
        filename="betweenness_centrality.txt",
    )
    metrics.get_metric(
        simple_digraph,
        "betweenness",
        is_digraph=True,
        filename="betweenness_centrality_digraph.txt",
    )

    # CLOSENESS
    metrics.get_metric(
        simple_graph,
        "closeness",
        is_digraph=False,
        filename="closeness_centrality.txt",
    )
    metrics.get_metric(
        simple_digraph,
        "closeness",
        is_digraph=True,
        filename="closeness_centrality_digraph.txt",
    )

    # PRESTIGIO
    metrics.get_metric(
        simple_digraph,
        "in_degree",
        is_digraph=True,
        filename="in_degree_centrality.txt",
    )


if __name__ == "__main__":
    main()
