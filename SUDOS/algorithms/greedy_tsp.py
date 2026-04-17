from typing import List, Tuple, Dict

def solve_greedy_tsp(depot: str, delivery_locations: List[str], apsp_dist: Dict[str, Dict[str, float]]) -> Tuple[List[str], float]:
    """
    Nearest Neighbor Greedy approach for TSP.
    Starts at `depot` and iteratively visits the nearest unvisited delivery location,
    and finally returns to the depot.
    
    Returns:
        route: The ordered sequence of visited locations (Depot -> ... -> Depot).
        total_cost: The total distance traveled.
    """
    unvisited = set(delivery_locations)
    current_node = depot
    route = [depot]
    total_cost = 0.0
    
    while unvisited:
        nearest_node = None
        min_dist = float('inf')
        
        for candidate in unvisited:
            dist = apsp_dist[current_node][candidate]
            if dist < min_dist:
                min_dist = dist
                nearest_node = candidate
                
        if nearest_node is None:
            # Graph is disconnected, cannot visit all nodes
            return [], float('inf')
            
        route.append(nearest_node)
        total_cost += min_dist
        current_node = nearest_node
        unvisited.remove(nearest_node)
        
    # Return to depot
    return_dist = apsp_dist[current_node][depot]
    if return_dist == float('inf'):
        return [], float('inf')
        
    route.append(depot)
    total_cost += return_dist
    
    return route, total_cost
