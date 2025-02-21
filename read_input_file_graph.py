
import json

from model.Node import Node
from model.Edge import Edge
from model.Graph import Graph


def read_input_file(filepath: str) -> list[any]:
    filepath = filepath.replace("\\", "/")

    input_edges: list[Edge] = []
    input_nodes: list[Node] = []

    f = open(filepath)
    data = json.load(f)

    for i in data['edges']:
        existing = True if i['edge_type'] == 'existing' else False
        offstreet = True if i['edge_type'] == 'offstreet' else False
        ep1 = int(i['endpoint1'])
        ep2 = int(i['endpoint2'])
        
        input_edges.append(Edge(int(i['id']), ep1, ep2, int(i['cost']), existing, offstreet))

    for i in data['nodes']:  
        node = Node(int(i['id']), tuple[float](i['coords']), str(i['node_type']))
        input_nodes.append(node)

    f.close()
    return input_edges, input_nodes