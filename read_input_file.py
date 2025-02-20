
import json

import model.Node
from model.Edge import Edge
from model.Graph import Graph
import globals

def read_input_file(filepath: str) -> list[any]:
    filepath = filepath.replace("\\", "/")

    input_edges: dict[int: Edge] = {}
    prospect_node_ids = []
    existing_node_ids = []

    f = open(filepath)
    data = json.load(f)

    for i in data['edges']:
        existing = True if i['edge_type'] == 'existing' else False
        offstreet = True if i['edge_type'] == 'offstreet' else False
        ep1 = int(i['endpoint1'])
        ep2 = int(i['endpoint2'])

        input_edges[int(i['id'])] = Edge(int(i['id']), ep1, ep2, int(i['cost']), existing, offstreet)

        if existing:
            if ep1 not in existing_node_ids:
                existing_node_ids.append(ep1)
            if ep2 not in existing_node_ids:
                existing_node_ids.append(ep2)

    for i in data['nodes']:        
        if i['node_type'] == 'prospect':
            prospect_node_ids.append(int(i['id']))

    f.close()
    return input_edges, existing_node_ids, prospect_node_ids