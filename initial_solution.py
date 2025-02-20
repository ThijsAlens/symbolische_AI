
import globals
from model.Edge import Edge

#def find_node_in_edge_list(node_id: int, list_of_edges: list[model.Edge.Edge]) -> list[model.Edge.Edge]:
#    res: list[model.Edge.Edge] = []
#    for edge in list_of_edges:
#        if (edge.endpoint1 == node_id or edge.endpoint2 == node_id):
#            res.append(edge)
#    return res
#
#def find_path(node_id: int, list_of_existing_edges: list[model.Edge.Edge]) -> None:
#    """
#    find a path from the node with id node_id to the existing network
#
#    args:
#        node_id (int): the id of the node to connect to the network
#        list_of_edges (list[model.Edge.Edge]): the list of edges that are already used (in state "existing") to connect the network
#    
#    returns:
#        None
#    """
#    edge_list = find_node_in_edge_list(node_id, list_of_existing_edges)
#    if (not edge_list):
#        # no connection is found in the existing edges
#        # try to find a connection in all the edges
#        edge_list = find_node_in_edge_list(node_id, globals.LIST_OF_ALL_EDGES)
#    if (not edge_list):
#        # something went wrong
#        print(f"Error: the node with id {node_id} is not connected to the network in any way")
#        globals.RUNNING = False
#        return
#        
#    # the node is connected to the network (existing or not) via at least one edge, take the lowest cost edge which is not an off-street edge
#    min_cost = edge_list[0].cost
#    min_cost_edge = edge_list[0]
#    for edge in edge_list:
#        if (edge.cost < min_cost):
#            min_cost = edge.cost
#            min_cost_edge = edge
#    
#    if (min_cost_edge.edge_type == "existing"):
#        # the node is connected to the network via an existing edge
#        return
#    elif (min_cost_edge.edge_type == "regular"):
#        # the node is not yet connected to the network:
#        # use the new found edge and find an other edge that is connected to the network
#        min_cost_edge.edge_type = "existing"
#        list_of_existing_edges.append(min_cost_edge)
#        globals.COST += min_cost_edge.cost
#        if (min_cost_edge.endpoint1 == node_id):
#            find_path(min_cost_edge.endpoint2, list_of_existing_edges)
#        else:
#            find_path(min_cost_edge.endpoint1, list_of_existing_edges)


def dfs(start: int, existing_node_ids: set[int], prospects: set[int]):
    """
    Depth-First Search to find a path from the start node (most likely a prospect node) to the existing network.
    
    Args:
        start (int): The ID of the start node.
        existing_node_ids (set[int]): The set of existing node IDs.
        prospects (set[int]): The set of prospect node IDs.

    Returns:
        bool: True if a path is found, False otherwise.
    """
    visited_nodes: set[int] = set()
    visited_edges: set[int] = set()  # Store visited edge IDs
    stack: list[int] = [start]

    while stack:
        node = stack.pop()
        if node in existing_node_ids:
            break  # Stop search when reaching an existing node
        if node in visited_nodes:
            continue

        visited_nodes.add(node)

        # Get adjacent edges (edges that contain 'node' as an endpoint)
        edges = globals.GRAPH.adjacency_list.get(node, [])  

        for edge in edges:
            neighbor = edge.endpoint1 if edge.endpoint2 == node else edge.endpoint2

            if neighbor not in visited_nodes and neighbor not in prospects:
                stack.append(neighbor)
                visited_edges.add(edge.id)  # Store the visited edge ID

    # Add visited edges to the graph (if needed for tracking purposes)
    for edge_id in visited_edges:
        edge = globals.GRAPH.edges[edge_id]  # Retrieve the edge from graph storage
        globals.GRAPH.add_edge(edge.id, edge.endpoint1, edge.endpoint2, edge.cost, edge.existing, edge.offstreet)

    return any(node in existing_node_ids for node in visited_nodes)  # True if a path is found

        

def initial_solution():
    for prospect in globals.GRAPH.prospects:
        dfs(prospect, globals.GRAPH.nodes, globals.GRAPH.prospects)
    
    print("Initial solution found")
    print(f"Cost: {globals.GRAPH.calculate_cost()}")

