import sys
import threading
import time

import load_lists
import algorithm
import globals


def save_data(input_file: str):
    load_lists.load_lists(input_file)

def solve_problem():

    #Find initial solution
    algorithm.initial_solution()
    #Optimize the solution

if __name__ == "__main__":
    args = sys.argv[1:]

    save_data(args[0])

    solve = threading.Thread(target=solve_problem)

    solve.start()

    time.sleep(int(args[2]))
    globals.RUNNING = False
    solve.join()


    # <input_file> <solution_file> <time_limit> <random_seed>
    input_file = args[0]
    solution_file = args[1]
    time_limit = args[2]
    if len(args) > 3:
        random_seed = args[3]

    

    

