import matplotlib.pyplot as plt
import networkx as nx

import model.Edge
import model.Node

def visualize_graph(nodes : list[model.Node.Node], edges : list[model.Edge.Edge]):
    G = nx.Graph()
    
    # Voeg nodes toe met hun coördinaten
    pos = {node.id: node.coords for node in nodes}
    for node in nodes:
        G.add_node(node.id, pos=node.coords)

    # Voeg edges toe tussen de juiste nodes
    for edge in edges:
        G.add_edge(edge.endpoint1, edge.endpoint2)

    # Teken de grafiek
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', edge_color='gray')
    plt.show()
