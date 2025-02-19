
import globals
import model.Edge
import model.constants

def find_node_in_edge_list(node_id: int, list_of_edges: list[model.Edge.Edge]) -> list[model.Edge.Edge, int]:
    for edge in list_of_edges:
        if (edge.endpoint1 == node_id):
            return [edge, 1]
        if (edge.endpoint2 == node_id):
            return [edge, 2]
    return None

def initial_solution():
    for prospect_node in globals.LIST_OF_PROSPECT_NODES:
        # first case: the prospect can connect to the network 
        res = find_node_in_edge_list(prospect_node.id, globals.LIST_OF_USED_EDGES)
        if (res):
            if (res[1] == 1):
                globals.LIST_OF_USED_NODES_ID.append(res[0].endpoint2)
            globals.LIST_OF_USED_NODES.append(edge)

