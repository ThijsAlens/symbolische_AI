import model.Edge as Edge

class Node ():
    def __init__(self, id: int, coords: tuple[int], node_type: str) -> None:
        self.id: int = id
        self.coords: tuple[int] = coords
        self.node_type: str = node_type
        self.neighbors: list[Edge.Edge] = []


