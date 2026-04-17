from typing import List, Tuple, Dict

def solve_dp_tsp(depot: str, delivery_locations: List[str], apsp_dist: Dict[str, Dict[str, float]]) -> Tuple[List[str], float]:
    """
    Held-Karp Dynamic Programming algorithm using bitmasks for exact TSP optimization.
    
    Returns:
        route: The ordered sequence of visited locations (Depot -> ... -> Depot).
        total_cost: The minimum total distance traveled.
    """
    n = len(delivery_locations)
    if n == 0:
        return [depot, depot], 0.0
        
    # Mapping indices to node names for bitmask
    nodes = delivery_locations
    
    # Memoization table
    # memo[(mask, curr_idx)] = (min_cost, prev_idx)
    memo = {}
    
    def tsp(mask: int, u_idx: int) -> float:
        # Base case: if all locations visited, return cost from last location back to depot
        if mask == (1 << n) - 1:
            u_node = nodes[u_idx]
            return apsp_dist[u_node][depot]
            
        if (mask, u_idx) in memo:
            return memo[(mask, u_idx)][0]
            
        min_cost = float('inf')
        best_v_idx = -1
        u_node = nodes[u_idx]
        
        for v_idx in range(n):
            if not (mask & (1 << v_idx)):  # If v is not visited
                v_node = nodes[v_idx]
                cost = apsp_dist[u_node][v_node] + tsp(mask | (1 << v_idx), v_idx)
                
                if cost < min_cost:
                    min_cost = cost
                    best_v_idx = v_idx
                    
        memo[(mask, u_idx)] = (min_cost, best_v_idx)
        return min_cost
        
    # Try starting from depot to every first location
    best_total_cost = float('inf')
    best_start_idx = -1
    
    for i in range(n):
        start_node = nodes[i]
        cost = apsp_dist[depot][start_node] + tsp(1 << i, i)
        if cost < best_total_cost:
            best_total_cost = cost
            best_start_idx = i
            
    if best_total_cost == float('inf'):
        return [], float('inf')
        
    # Reconstruct optimal route
    route = [depot]
    curr_mask = 1 << best_start_idx
    curr_idx = best_start_idx
    
    route.append(nodes[curr_idx])
    
    while curr_mask != (1 << n) - 1:
        # Fetch the next node choice from memo
        _, next_idx = memo[(curr_mask, curr_idx)]
        curr_mask |= (1 << next_idx)
        curr_idx = next_idx
        route.append(nodes[curr_idx])
        
    route.append(depot)
    
    return route, best_total_cost
