import heapq
from typing import Dict, List, Tuple
import sys
import os

# Ensure we can import from utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.graph_builder import Graph

def dijkstra(graph: Graph, start: str) -> Tuple[Dict[str, float], Dict[str, str]]:
    """
    Computes the shortest paths from `start` to all other nodes.
    Returns:
        distances: dict mapping node -> shortest distance
        previous: dict mapping node -> previous node in the shortest path
    """
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0.0
    previous = {node: None for node in graph.nodes}
    
    pq = [(0.0, start)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        # Optimization: skip if we found a better path already
        if current_dist > distances[current_node]:
            continue
            
        for neighbor, weight in graph.get_neighbors(current_node):
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
                
    return distances, previous

def compute_apsp(graph: Graph, nodes_of_interest: List[str]) -> Tuple[Dict[str, Dict[str, float]], Dict[str, Dict[str, List[str]]]]:
    """
    Computes All-Pairs Shortest Paths restricted to a subset of nodes of interest.
    Used to build a complete graph representation for TSP algorithms.
    
    Returns:
        apsp_dist: dist[u][v] = shortest distance from u to v
        apsp_paths: paths[u][v] = list of nodes forming shortest path from u to v (inclusive)
    """
    apsp_dist = {}
    apsp_paths = {}
    
    for u in nodes_of_interest:
        apsp_dist[u] = {}
        apsp_paths[u] = {}
        distances, previous = dijkstra(graph, u)
        
        for v in nodes_of_interest:
            apsp_dist[u][v] = distances[v]
            
            # Reconstruct path from u to v
            path = []
            curr = v
            while curr is not None:
                path.append(curr)
                if curr == u:
                    break
                curr = previous[curr]
            
            path.reverse()
            if distances[v] == float('inf'):
                apsp_paths[u][v] = [] # No path exists
            else:
                apsp_paths[u][v] = path
                
    return apsp_dist, apsp_paths
