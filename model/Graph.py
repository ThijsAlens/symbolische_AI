from model.Edge import Edge

class Graph:
    def __init__(self, filename=None):
        self.filename = filename
        self.prospects: set[int] = set()                      # Set of prospect node IDs
        self.edges: dict[int, Edge] = {}                      # Dict of edges with ID as key
        self.adjacency_list: dict[int, list[Edge]] = {}       # Dict mapping node ID to list of adjacent edges
        self.nodes: set[int] = set()                          # Set of node IDs in the graph

    def add_edge(self, edge: Edge):
        self.nodes.update([edge.endpoint1, edge.endpoint2])

        self.edges[edge.id] = edge

        self.adjacency_list.setdefault(edge.endpoint1, []).append(edge)
        self.adjacency_list.setdefault(edge.endpoint2, []).append(edge)

    def add_prospect(self, prospect_id: int):
        self.prospects.add(prospect_id)

    def calculate_cost(self) -> int:
        return sum(edge.cost for edge in self.edges.values())