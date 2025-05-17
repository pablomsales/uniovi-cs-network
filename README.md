# UniOvi Computer Science Network Analysis

## TLDR

This project analyzes PhD thesis supervision relationships at University of Oviedo's CS
Department using network analysis. It identifies influential supervisors, research
communities, and network structures through various centrality metrics.
[Explore the interactive network visualization](https://pablomsales.github.io/uniovi-cs-network/)
to see the connections between authors and supervisors.

It scrapes data from the university's thesis web repository using Selenium, builds
relationship graphs between authors and directors using Networkx, calculates relevant
network metrics, and provides both static and interactive visualizations.

## Features

*   **Data Scraping**: Collects thesis data, including titles, authors, directors
                        using Python and Selenium.

*   **Graph Generation**: Creates directed graphs representing thesis supervision
                        relationships using NetworkX.

*   **Network Metrics**: Calculates key centrality metrics (Degree, In-Degree/Prestige,
                        Betweenness, Closeness) to identify influential individuals and
                        structural properties of the network.

*   **Community Detection**: Identifies research communities or clusters within the network
                        using Louvain's Method, the current SOTA in community detection.

*   **Interactive Visualizations**: Generates dynamic and explorable HTML graphs using
                        Pyvis, allowing users to interact with the network.

*   **Static Visualizations**: Produces static SVG images of graphs and barplots of
                        metrics using Matplotlib for quick overviews and reporting.



## Visualizations

### Interactive Network Graphs With Detected Communities

Explore the interactive network visualizations hosted on GitHub Pages:

**[View Interactive Graph](https://pablomsales.github.io/uniovi-cs-network/)**

/**
 * The results of the detected communities show a significant level of correspondence
 * with the existing research groups, indicating that the Louvain method successfully
 * identifies communities that align well with the actual research group structure of the
 * department.

 * It's worth noting that this high level of correspondence suggests that collaborative patterns within the department 
 * tend to follow formal research group boundaries, which validates both the algorithmic approach and the existing
 * organizational structure.
 */



### Key Metrics

Below are barplots for some of the calculated network metrics, highlighting the top
individuals. Full metric data is available in the `.txt` files within the respective
`metrics` subdirectories.

**Degree Centrality**

*Highlights individuals with the most connections (supervisions given and received).*

![Degree Centrality Digraph](outputs/interactive/metrics/degree_centrality_digraph_barplot.svg)

**In-Degree Centrality / Prestige**

*Highlights individuals who have supervised the most theses.*

![In-Degree Centrality](outputs/interactive/metrics/in_degree_centrality_barplot.svg)

**Betweenness Centrality**

*Highlights individuals who act as bridges or connectors between different parts of the network.*

![Betweenness Centrality Digraph](outputs/interactive/metrics/betweenness_centrality_digraph_barplot.svg)

**Closeness Centrality**

*Highlights individuals who are, on average, closest to all other individuals in the network.*

![Closeness Centrality Digraph](outputs/interactive/metrics/closeness_centrality_digraph_barplot.svg)


## Technologies Used

*   **Python**: Core language for scripting, data processing, and automation.
    *   **Selenium**: For web scraping thesis data from dynamic web pages.
    *   **NetworkX**: For creating, manipulating, and analyzing complex networks (graphs).
    *   **Matplotlib**: For generating static plots and visualizations, such as bar charts for metrics.
    *   **Pyvis**: For creating interactive network visualizations renderable in HTML.
*   **Git & GitHub**: For version control and project hosting.