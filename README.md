# SUDOS – Smart Urban Delivery Optimization System

## Overview
SUDOS (Smart Urban Delivery Optimization System) is a graph-based optimization system designed to model urban delivery networks and compute efficient delivery routes.

The system applies multiple algorithm design paradigms including Greedy methods, Graph algorithms, Dynamic Programming, and Approximation techniques to solve routing problems and analyze trade-offs between optimality and efficiency.

---

## Objectives
- Model a city as a weighted graph structure  
- Optimize delivery routes for one or more agents  
- Implement and compare multiple algorithmic approaches  
- Analyze performance in terms of time, space, and accuracy  

---

## Problem Modeling
- **Nodes** → Delivery locations  
- **Edges** → Roads connecting locations  
- **Weights** → Distance or travel time  
- **Agents** → Delivery vehicles  

The delivery problem is modeled as a variation of the Traveling Salesperson Problem (TSP) and shortest path optimization.

---

## Algorithms Implemented

### 1. Greedy Approach (Nearest Neighbor)
- Selects the closest unvisited node at each step  
- Fast execution but may produce suboptimal routes  

### 2. Shortest Path Algorithm
- **Dijkstra’s Algorithm** used to compute shortest paths between nodes  
- Ensures optimal path for individual segments  

### 3. Dynamic Programming (TSP)
- Bitmask-based DP solution for TSP  
- Guarantees optimal route for small datasets  
- High computational complexity  

### 4. Approximation / Heuristic Approach
- Optimized heuristic for near-optimal solutions  
- balances performance and scalability  

---

## Comparative Analysis

| Algorithm        | Time Complexity     | Optimality     | Use Case                     |
|----------------|--------------------|---------------|-----------------------------|
| Greedy         | O(n²)              | Low           | Fast approximations         |
| Dijkstra       | O(E log V)         | Medium        | Shortest path computation   |
| DP (TSP)       | O(n² · 2ⁿ)         | High          | Small datasets              |
| Heuristic      | O(n²)              | Near Optimal  | Scalable solutions          |

---

## Project Structure
```text
SUDOS/
│
├── data/
│ └── graph_data.json
│
├── algorithms/
│ ├── dijkstra.py
│ ├── greedy_tsp.py
│ ├── dp_tsp.py
│ └── heuristic.py
│
├── utils/
│ └── graph_builder.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation & Execution

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/sudos.git
cd sudos
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Project
```bash
python main.py
```

---

## Input
- Graph dataset (nodes, edges, weights)
- Delivery locations
- Number of delivery agents

## Output
- Optimized delivery routes
- Total cost (distance/time)
- Algorithm performance comparison

## Results & Observations
- **Greedy approach** provides fast but suboptimal solutions
- **Dynamic Programming** ensures optimal routes but is computationally expensive
- **Heuristic methods** achieve a balance between speed and solution quality
- **Dijkstra** enhances route accuracy when combined with other approaches

## Future Enhancements
- Real-time traffic data integration
- Multi-agent route optimization using advanced techniques
- Integration with mapping APIs
- Parallelized computation for large datasets

## Team Members
- Aron Chandel | 24BCT0200
- Sakshi Somnath | 24BCT0184
- Shlok Sharma | 24BCT0179

## References
- Introduction to Algorithms (CLRS)
- Dijkstra’s Algorithm
- Traveling Salesperson Problem (TSP)
- Approximation Algorithms in Graph Theory
