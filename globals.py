
import model.Node
import model.Edge
from model.Graph import Graph

LIST_OF_PROSPECT_NODES: list[model.Node.Node] = []
LIST_OF_REGULAR_NODES: list[model.Node.Node] = []
LIST_OF_USED_NODES_ID: list[model.Node.Node] = []

LIST_OF_EXISTING_EDGES: list[model.Edge.Edge] = []
LIST_OF_REGULAR_EDGES: list[model.Edge.Edge] = []
LIST_OF_OFF_STREET_EDGES: list[model.Edge.Edge] = []

LIST_OF_ALL_EDGES: list[model.Edge.Edge] = []

LIST_OF_USED_EDGES: list[model.Edge.Edge] = []

#---------------------------------------------------------#

COST: int = 0
RUNNING: bool = True
GRAPH: Graph = None
EXISTING_NODE_IDS: set[int] = None

