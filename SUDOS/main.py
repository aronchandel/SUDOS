import time
import os
from utils.graph_builder import Graph
from algorithms.dijkstra import compute_apsp
from algorithms.greedy_tsp import solve_greedy_tsp
from algorithms.dp_tsp import solve_dp_tsp
from algorithms.heuristic import solve_heuristic_tsp

def expand_route_with_paths(compact_route, apsp_paths):
    """
    Expands the compact TSP wrapper route into a physical continuous path through the original graph.
    """
    if not compact_route:
        return []
        
    full_path = [compact_route[0]]
    for i in range(len(compact_route) - 1):
        u = compact_route[i]
        v = compact_route[i+1]
        
        # Segment from u to v
        segment = apsp_paths[u][v]
        
        # The segment includes u and v. To prevent duplicates (since full_path already has u),
        # we append from segment[1:]
        if len(segment) > 1:
            full_path.extend(segment[1:])
            
    return full_path

def print_result_row(algo_name, route_str, cost, exec_time):
    print(f"| {algo_name:<10} | {route_str:<40} | {cost:<10.2f} | {exec_time * 1000:<12.4f} |")

def main():
    print("Initializing SUDOS...")
    data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'graph_data.json')
    g = Graph(data_path)
    
    nodes_of_interest = [g.depot] + g.delivery_locations
    print(f"Depot: {g.depot}")
    print(f"Deliveries: {g.delivery_locations}\n")
    
    print("Computing Shortest Paths (Dijkstra APSP)...")
    apsp_dist, apsp_paths = compute_apsp(g, nodes_of_interest)
    
    # 1. Greedy
    start_t = time.perf_counter()
    greedy_route, greedy_cost = solve_greedy_tsp(g.depot, g.delivery_locations, apsp_dist)
    greedy_time = time.perf_counter() - start_t
    
    g_full_path = expand_route_with_paths(greedy_route, apsp_paths)
    
    # 2. DP
    start_t = time.perf_counter()
    dp_route, dp_cost = solve_dp_tsp(g.depot, g.delivery_locations, apsp_dist)
    dp_time = time.perf_counter() - start_t
    
    dp_full_path = expand_route_with_paths(dp_route, apsp_paths)
    
    # 3. Heuristic
    # 2-Opt is seeded with the greedy output.
    start_t = time.perf_counter()
    heur_route, heur_cost = solve_heuristic_tsp(greedy_route, apsp_dist)
    heur_time = time.perf_counter() - start_t
    
    heur_full_path = expand_route_with_paths(heur_route, apsp_paths)
    
    print("\n" + "="*85)
    print(f"| {'Algorithm':<10} | {'Physical Route':<40} | {'Cost':<10} | {'Time (ms)':<12} |")
    print("-" * 85)
    
    def path_to_str(path):
        s = " -> ".join(path)
        if len(s) > 37:
            return s[:34] + "..."
        return s
        
    print_result_row("Greedy", path_to_str(g_full_path), greedy_cost, greedy_time)
    print_result_row("DP", path_to_str(dp_full_path), dp_cost, dp_time)
    print_result_row("Heuristic", path_to_str(heur_full_path), heur_cost, heur_time)
    print("="*85)

if __name__ == "__main__":
    main()
