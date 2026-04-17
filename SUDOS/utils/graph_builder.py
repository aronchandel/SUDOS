import json
from typing import List, Tuple

class Graph:
    """
    A utility class to parse the JSON and construct the graph.
    Uses an adjacency list representation.
    """
    def __init__(self, json_path: str):
        self.nodes: List[str] = []
        self.adj_list: dict = {}
        self.depot: str = ""
        self.delivery_locations: List[str] = []
        
        self.load_graph(json_path)

    def load_graph(self, json_path: str):
        """Loads graph data from a JSON file and builds the adjacency list."""
        with open(json_path, 'r') as f:
            data = json.load(f)
            
        self.depot = data.get("start_depot", "")
        self.delivery_locations = data.get("delivery_locations", [])
        self.nodes = data.get("nodes", [])
        
        # Initialize adjacency list
        for node in self.nodes:
            self.adj_list[node] = []
            
        # Populate adjacency list (assuming undirected graph)
        for edge in data.get("edges", []):
            u = edge["u"]
            v = edge["v"]
            weight = edge["weight"]
            
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))
            
    def get_neighbors(self, node: str) -> List[Tuple[str, float]]:
        """Returns a list of (neighbor_id, weight) for a given node."""
        return self.adj_list.get(node, [])
        
    def get_weight(self, u: str, v: str) -> float:
        """Returns the weight of the edge between u and v, or infinity if no edge exists."""
        for neighbor, weight in self.adj_list.get(u, []):
            if neighbor == v:
                return float(weight)
        return float('inf')
