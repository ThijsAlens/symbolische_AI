
import globals
import model.Edge
import model.constants

def find_node_in_edge_list(node_id: int, list_of_edges: list[model.Edge.Edge]) -> list[model.Edge.Edge]:
    for edge in list_of_edges:
        res: list[model.Edge.Edge] = []
        if (edge.endpoint1 == node_id or edge.endpoint2 == node_id):
            res.append(edge)
    return res

def find_path(node_id: int, list_of_edges: list[model.Edge.Edge]):
    edge_list = find_node_in_edge_list(node_id, list_of_edges)

    if (edge_list):
        # the node is connected to the network via an edge, take the lowest cost edge
        min_cost = edge_list[0].cost
        min_cost_edge = edge_list[0]
        for edge in edge_list:
            if (edge.cost < min_cost):
                min_cost = edge.cost
                min_cost_edge = edge
        return min_cost_edge

    else:
        # the node is not connected to the network, search further
        
        

def initial_solution():
    for prospect_node in globals.LIST_OF_PROSPECT_NODES:
        # first case: the prospect can connect to the network 
        res = find_node_in_edge_list(prospect_node.id, globals.LIST_OF_USED_EDGES)
        if (res):
            if (res[1] == 1):
                globals.LIST_OF_USED_NODES_ID.append(res[0].endpoint1)
            if (res[1] == 2):
                globals.LIST_OF_USED_NODES_ID.append(res[0].endpoint2)

