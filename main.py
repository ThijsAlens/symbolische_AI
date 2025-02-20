import sys
import threading
import time
from tqdm import tqdm

import read_input_file
import initial_solution
import globals
from model.Graph import Graph
from model.Edge import Edge


def save_data(input_file: str):
    input_edges: dict[int, Edge]
    existing_node_ids: set[int]
    prospect_node_ids: set[int]

    input_edges, existing_node_ids, prospect_node_ids = read_input_file.read_input_file(input_file)

    globals.GRAPH = Graph(filename=input_file)
    for input_edge in input_edges.values():
        globals.GRAPH.add_edge(input_edge)
    for prospect_node_id in prospect_node_ids:
        globals.GRAPH.add_prospect(prospect_node_id)
    globals.EXISTING_NODE_IDS = existing_node_ids

def solve_problem():

    #Find initial solution
    initial_solution.initial_solution()
    #Optimize the solution

if __name__ == "__main__":
    args = sys.argv[1:]

    save_data(args[0])

    solve = threading.Thread(target=solve_problem)
    solve.start()

    timer = int(args[2])
    with tqdm(total=timer, desc="Countdown", unit="s") as pbar:
        while globals.RUNNING and timer > 0:
            time.sleep(1)  # Simulating work (e.g., countdown)
            timer -= 1
            pbar.update(1)  # Update the progress bar
    globals.RUNNING = False
    solve.join()


    # <input_file> <solution_file> <time_limit> <random_seed>
    input_file = args[0]
    solution_file = args[1]
    time_limit = args[2]
    if len(args) > 3:
        random_seed = args[3]

    

    

