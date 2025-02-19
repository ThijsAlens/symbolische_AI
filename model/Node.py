
from constants import REGULAR, PROSPECT
import Edge

class Node ():
    def __init__(self, id: int, coords: tuple[int], node_type: int) -> None:
        self.id: int = id
        self.coords: tuple[int] = coords
        self.node_type: int = node_type
        self.neighbors: list[Edge.Edge] = []

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'coords': self.coords,
            'node_type': self.node_type,
            'neighbors': [neighbor.serialize() for neighbor in self.neighbors]
        }
    
    @classmethod
    def deserialize(cls, data: dict):
        node: Node = cls(data["id"], data["coords"], data["node_type"])
        return node


