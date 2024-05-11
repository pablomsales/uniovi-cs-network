import networkx as nx


def get_relations(data):

    relations = []

    for year in data.keys():
        for id in data[year].keys():
            author = data[year][id]["author"]
            directors = data[year][id]["directors"]

            thesis_relations = [(author, director) for director in directors]
            relations.extend(thesis_relations)

    # eliminamos posibles duplicados (al menos Francisco Javier Gil Gala)
    relations = set(relations)

    return relations


def get_graph(relations):

    graph = nx.Graph()

    # añadimos nodos y aristas
    for rel in relations:
        author, director = rel
        graph.add_edge(author, director)

    return graph


def get_DiGraph(relations):

    DiGraph = nx.DiGraph()
    # añadimos nodos y aristas
    for rel in relations:
        author, director = rel
        DiGraph.add_edge(author, director)

    return DiGraph
