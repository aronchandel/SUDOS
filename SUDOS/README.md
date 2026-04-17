# SUDOS: Smart Urban Delivery Optimization System

SUDOS is a graph-based optimization system designed to model urban delivery networks and compute efficient delivery routes. 
It analyzes the trade-offs between optimality and efficiency by comparing several algorithmic paradigms for solving a variation of the Traveling Salesperson Problem (TSP) on city graphs.

## Algorithms Examined
1. **Dijkstra’s Algorithm:** Used as a vital precursor to normalize sparse real-city grids by determining the true shortest paths strictly between the Delivery Nodes and the Start Depot.
2. **Greedy (Nearest Neighbor):** Starting from the Depot, the route constantly jumps to the closest unvisited point. This evaluates in $O(n^2)$ time but may fall into poor local traps leading back to the start.
3. **Dynamic Programming (Held-Karp):** Utilizes bitmasks and memoization to find the literal optimal path. Extremely memory/compute heavy at $O(n^2 \cdot 2^n)$ but guarantees the purest shortest length.
4. **Heuristic (2-Opt Local Search):** Seeding off an initial approximation (like the result of Greedy), this algorithm uncrosses intersection paths iteratively. Scalable and fast, rendering near-optimal solutions.

## Setup & Running

This project relies purely on Python Standard Libraries. No external pip installations are strictly necessary to benchmark the core module!

```bash
# Clone or navigate to directory
cd SUDOS

# Run the comparative benchmark
python main.py
```
