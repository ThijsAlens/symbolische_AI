
import globals
import model.Edge
import model.constants

def find_node_in_edge_list(node_id: int, list_of_edges: list[model.Edge.Edge]) -> model.Edge.Edge:
    for edge in list_of_edges:
        if (edge.endpoint1 == node_id):
            return edge
        if (edge.endpoint2 == node_id):
            return edge
    return None

def find_path(node_id: int, list_of_used_edges: list[model.Edge.Edge]):
    edge = find_node_in_edge_list(node_id, list_of_used_edges)

    if (edge):
        # the node is connected to the network via 'edge'
        return edge
    else:
        

def initial_solution():
    for prospect_node in globals.LIST_OF_PROSPECT_NODES:
        # first case: the prospect can connect to the network 
        res = find_node_in_edge_list(prospect_node.id, globals.LIST_OF_USED_EDGES)
        if (res):
            if (res[1] == 1):
                globals.LIST_OF_USED_NODES_ID.append(res[0].endpoint1)
            if (res[1] == 2):
                globals.LIST_OF_USED_NODES_ID.append(res[0].endpoint2)

