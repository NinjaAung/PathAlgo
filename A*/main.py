#!/usr/bin/python3

# A* pathfinding algo
'''
A* Score = Cost Of Path + Heurestic

Unlike Djik we are using an additional heurestic with equals the A* score
This heurestic is adding E(Sum of all edges of current path) and
the A(The heuristic distance) to the goal

Important about the A(Heuristic) is that it MUST never over estimate the cost
'''


# Code
example_graph_small = {
    # vertex: (heuristic_distance, [(nxt_vertex,edge_cost), ...])
    'A', (17, [('B', 5), ('C', 3)]),
    'B', (13, [('A', 5), ('C', 1), ('D', 4)]),
    'C', (14, [('A', 3), ('B', 1), ('D', 6), ('E', 10)]),
    'D', (9, [('B', 4), ('C', 6), ('E', 8), ('G', 6)]),
    'E', (4, [('D', 8), ('C', 10), ('F', 3)]),
    'F', (1, [('G', 3), ('E', 3), ('Goal', 1)]),
    'G', (3, [('D', 6), ('F', 3), ('Goal', 3)]),
    'Goal', (0, [('G', 3), ('F', 1)])
}


def astar_static(table, start, goal):
    pass
