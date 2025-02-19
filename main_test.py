import sys
import threading

import load_lists
import algorithm
import globals
import visualize_graph


def save_data(input_file: str):
    load_lists.load_lists(input_file)

def solve_problem():

    #visualize nodes and edges
    list_of_nodes = globals.LIST_OF_PROSPECT_NODES + globals.LIST_OF_REGULAR_NODES
    list_of_edges = globals.LIST_OF_EXISTING_EDGES + globals.LIST_OF_REGULAR_EDGES + globals.LIST_OF_OFF_STREET_EDGES
    
    visualize_graph.visualize_graph(list_of_nodes,list_of_edges)


if __name__ == "__main__":
    args = sys.argv[1:]

    save_data(args[0])

    start = threading.Thread(target=solve_problem)

    start.start()

    # <input_file> <solution_file> <time_limit> <random_seed>
    input_file = args[0]
    solution_file = args[1]
    time_limit = args[2]
    if len(args) > 3:
        random_seed = args[3]

    

    

