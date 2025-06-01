import networkx as nx
import numpy as np

def rastgele_graf_olustur(n=1250, p=0.01, min_cap=1, max_cap=20):
    G = nx.gnp_random_graph(n, p, directed=True)
    capacities = np.random.randint(min_cap, max_cap + 1, size=G.number_of_edges())
    for (u, v), c in zip(G.edges(), capacities):
        G[u][v]['capacity'] = c
    return G

def source_sink_belirle(G, source=0):
    lengths = nx.single_source_shortest_path_length(G, source)
    sink = max(lengths, key=lengths.get)
    return source, sink
