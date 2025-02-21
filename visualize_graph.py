import matplotlib.pyplot as plt
import networkx as nx

import model.Edge
import model.Node

def visualize_graph(nodes : list[model.Node.Node], edges : list[model.Edge.Edge]):
    G = nx.Graph()
    
    # Voeg nodes toe met hun coördinaten
    for node in nodes:
        G.add_node(node.id, pos=(node.coords[0], node.coords[1]))

    # Voeg edges toe tussen de juiste nodes
    for edge in edges:
        G.add_edge(edge.endpoint1, edge.endpoint2)

    # Get positions for visualization
    pos = nx.get_node_attributes(G, 'pos')

    # Visualize the graph
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=20, font_size=4)
    plt.show()
