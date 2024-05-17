# Grafos Tesis UniOvi

Grafos con las Tesis Doctorales del Departamento de Informática de la Universidad de Oviedo.

Los grafos se encuentran en `outputs`. Hay versiones estáticas e interactivas. Las interactivas son muchísimo más informativas que las estáticas.
Para visualizarlas, descargar el `.html` correspondiente y abrirlo con un navegador. En principio, deberían poder visualizarse tanto con Firefox como con cualquier navegador derivado de Chromium (Chrome, Safari, Brave, ...).

También se adjuntas barplots de las métricas calculadas, estan en los subdirectorios `metrics`, junto con las métricas completas en formato `.txt`.

## Estructura de directorios:

./
├──  data/
│   └──  thesis.json
|
├── outputs/
│   ├── interactive/
│   │   ├── metrics/
│   │   │   ├── betweenness_centrality_digraph_barplot.svg
│   │   │   ├── betweenness_centrality_digraph.txt
│   │   │   ├── closeness_centrality_digraph_barplot.svg
│   │   │   ├── closeness_centrality_digraph.txt
│   │   │   ├── degree_centrality_digraph_barplot.svg
│   │   │   ├── degree_centrality_digraph.txt
│   │   │   ├── in_degree_centrality_barplot.svg
│   │   │   └── in_degree_centrality.txt
|   |   |
│   │   ├── thesis_communities_interactive.html
│   │   ├── thesis_degree_interactive.html
│   │   └── thesis_interactive.html
|   |
│   └── static/
│       ├── metrics/
│       │   ├── betweenness_centrality_barplot.svg
│       │   ├── betweenness_centrality.txt
│       │   ├── closeness_centrality_barplot.svg
│       │   ├── closeness_centrality.txt
│       │   ├── degree_centrality_barplot.svg
│       │   └── degree_centrality.txt
|       |
│       ├── thesis_communities.svg
│       ├── thesis_degree.svg
│       └── thesis_simple.svg
|
├── src/
│   ├── graph/
│   │   ├── __pycache__/
│   │   │   ├── graph_and_metrics.cpython-311.pyc
│   │   │   ├── graph_maker.cpython-311.pyc
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   ├── metrics.cpython-311.pyc
│   │   │   ├── plot_interactive_graphs.cpython-311.pyc
│   │   │   ├── plot_static_graphs.cpython-311.pyc
│   │   │   └── relations.cpython-311.pyc
|   |   |
│   │   ├── graph_maker.py
│   │   ├── __init__.py
│   │   ├── metrics.py
│   │   ├── plot_interactive_graphs.py
│   │   └── plot_static_graphs.py
|   |
│   ├── scraper/
│   │   ├── __pycache__/
│   │   │   ├── button_click.cpython-311.pyc
│   │   │   ├── clean_data.cpython-311.pyc
│   │   │   ├── click_button.cpython-311.pyc
│   │   │   ├── config.cpython-311.pyc
│   │   │   ├── extract_data.cpython-311.pyc
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   └── json_generator.cpython-311.pyc
|   |   |
│   │   ├── clean_data.py
│   │   ├── click_button.py
│   │   ├── config.py
│   │   ├── extract_data.py
│   │   ├── __init__.py
│   │   └── json_generator.py
|   |
│   └── main.py
|
├── README.md
└── requirements.txt