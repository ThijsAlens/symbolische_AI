import model.Edge as Edge

class Node:
    def __init__(self, id: int, coords: tuple[float], node_type: str):
        self.id: int = id
        self.coords: tuple[float] = coords
        self.node_type: str = node_type
        self.neighbors: list[Edge.Edge] = []


