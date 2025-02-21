import sys
import threading

import read_input_file_graph
import initial_solution
import globals
import visualize_graph

def save_data(input_file: str):
    list_of_edges, list_of_nodes = read_input_file_graph.read_input_file(input_file)
    visualize_graph.visualize_graph(list_of_nodes,list_of_edges)

def solve_problem():
    return

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

    

    

