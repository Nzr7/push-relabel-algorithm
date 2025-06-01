import networkx as nx
import matplotlib.pyplot as plt

def grafi_gorsellestir(G, source, sink, node_limit=200, title='Ağ Grafiği'):
    """
    Büyük grafikleri sadeleştirerek ve source/sink vurgusu yaparak görselleştirir.
    """
    # Altgraf seçimi (büyük grafiklerde sadeleştirme için)
    if len(G.nodes) > node_limit:
        sampled_nodes = list(G.nodes)[:node_limit]
        G = G.subgraph(sampled_nodes).copy()

    pos = nx.spring_layout(G, seed=42)  # Düğümleri konumlandır

    node_colors = []
    for node in G.nodes():
        if node == source:
            node_colors.append('green')  # Source → Yeşil
        elif node == sink:
            node_colors.append('red')    # Sink → Kırmızı
        else:
            node_colors.append('lightblue')

    edge_labels = {(u, v): d['capacity'] for u, v, d in G.edges(data=True)}

    plt.figure(figsize=(12, 8))
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=300)
    nx.draw_networkx_edges(G, pos, arrows=True)
    nx.draw_networkx_labels(G, pos, font_size=8, font_color='black')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)
    plt.title(title)
    plt.axis('off')
    plt.tight_layout()
    plt.show()
