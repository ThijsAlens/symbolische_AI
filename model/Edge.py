class Edge ():
    def __init__(self, id: int, endpoint1: int, endpoint2: int, cost: float, edge_type: int) -> None:
        self.id = id
        self.endpoint1 = endpoint1
        self.endpoint2 = endpoint2
        self.cost = cost
        self.edge_type = edge_type

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'endpoint1': self.endpoint1,
            'endpoint2': self.endpoint2,
            'cost': self.cost,
            'edge_type': self.edge_type
        }
    
    @classmethod
    def deserialize(cls, data: dict):
        edge: Edge = cls(data["id"], data["endpoint1"], data["endpoint2"], data["cost"], data["edge_type"])
        return edge