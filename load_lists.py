
import json

import model.Node
import model.Edge
import globals

def load_lists(file_path: str):
    with open(file_path, 'r') as file:
        # Load the existing data
        file.seek(0)
        existing_data: dict[str:list[dict[str:any]]] = json.load(file)

        # Load the nodes
        nodes: list[dict[str:any]] = existing_data["nodes"]
        for node in nodes:
            match node["node_type"]:
                case "regular":
                    globals.LIST_OF_REGULAR_NODES.append(model.Node.Node.deserialize(node))
                case "prospect":
                    globals.LIST_OF_PROSPECT_NODES.append(model.Node.Node.deserialize(node))
                case _:
                    raise ValueError("Invalid node type")
        
        # Load the edges
        edges: list[dict[str:any]] = existing_data["edges"]
        for edge in edges:
            match edge["edge_type"]:
                case "regular":
                    globals.LIST_OF_REGULAR_EDGES.append(model.Edge.Edge.deserialize(edge))
                case "existing":
                    globals.LIST_OF_EXISTING_EDGES.append(model.Edge.Edge.deserialize(edge))
                case "off_street":
                    globals.LIST_OF_OFF_STREET_EDGES.append(model.Edge.Edge.deserialize(edge))
                case _:
                    raise ValueError("Invalid edge type")