class Edge:
    def __init__(self, id: int, endpoint1: int, endpoint2: int, cost: float, existing: bool, offstreet: bool):
        self.id: int = id
        self.endpoint1: int = endpoint1
        self.endpoint2: int = endpoint2
        self.cost: float = cost
        self.existing: bool = existing
        self.offstreet: bool = offstreet

    def __repr__(self):
        return f"Edge({self.id}, {self.endpoint1}, {self.endpoint2}, cost={self.cost}, existing={self.existing}, offstreet={self.offstreet})"
