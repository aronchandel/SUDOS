from typing import List, Tuple, Dict
import copy

def calculate_route_cost(route: List[str], apsp_dist: Dict[str, Dict[str, float]]) -> float:
    """Calculates the total cost of a given sequence array."""
    cost = 0.0
    for i in range(len(route) - 1):
        cost += apsp_dist[route[i]][route[i+1]]
    return cost

def solve_heuristic_tsp(initial_route: List[str], apsp_dist: Dict[str, Dict[str, float]]) -> Tuple[List[str], float]:
    """
    2-Opt local search approximation heuristic.
    Takes an initial route (e.g., from greedy algorithm) and iteratively
    attempts 2-edge swaps to improve the total distance.
    
    Returns:
        route: The optimized ordered sequence.
        total_cost: The improved total distance.
    """
    if len(initial_route) < 4:
        # Cannot perform 2-opt on route with fewer than 4 nodes (incl. depot twice)
        return initial_route, calculate_route_cost(initial_route, apsp_dist)
        
    best_route = copy.deepcopy(initial_route)
    best_cost = calculate_route_cost(best_route, apsp_dist)
    improved = True
    
    while improved:
        improved = False
        # Loop over possible segments to reverse
        # Do not swap the first and last node (Depot)
        for i in range(1, len(best_route) - 2):
            for j in range(i + 1, len(best_route) - 1):
                # Swap mechanism: reverse the items from i to j
                new_route = best_route[:i] + best_route[i:j+1][::-1] + best_route[j+1:]
                new_cost = calculate_route_cost(new_route, apsp_dist)
                
                if new_cost < best_cost:
                    # Found a shorter route
                    best_route = new_route
                    best_cost = new_cost
                    improved = True
                    break # Break inner loop, restart outer logic
            if improved:
                break
                
    return best_route, best_cost
