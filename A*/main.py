#!/usr/bin/python3

# A* pathfinding algo
'''
A* Score = Cost Of Path + Heurestic

A* is Djik with a heurestic that is the A* score
This heurestic is adding E(Sum of all edges of current path) and
the A(The heuristic distance) to the goal

Important about the A(Heuristic) is that it MUST never over estimate the cost


A* Score gives the computer/code an idea of how far we are to the end point
'''


# Code
example_graph = {
    # vertex: (heuristic_distance, [(nxt_vertex,edge_cost), ...])
    'A': (17, [('B', 5), ('C', 3)]),
    'B': (13, [('A', 5), ('C', 1), ('D', 4)]),
    'C': (14, [('A', 3), ('B', 1), ('D', 6), ('E', 10)]),
    'D': (9, [('B', 4), ('C', 6), ('E', 8), ('G', 6)]),
    'E': (4, [('D', 8), ('C', 10), ('F', 3)]),
    'F': (1, [('G', 3), ('E', 3), ('Goal', 1)]),
    'G': (3, [('D', 6), ('F', 3), ('Goal', 3)]),
    'Goal': (0, [('G', 3), ('F', 1)])
}

example_graph_large = {
        # vertex: (heuristic_distance, [(nxt_vertex,edge_cost), ...])
        'A': (16, [('B', 5), ('C', 5)]),
        'B': (17, [('A', 5), ('C', 4), ('D', 3)]),
        'C': (13, [('A', 5), ('B', 4), ('D', 7), ('E', 7), ('H', 8)]),
        'D': (16, [('B', 3), ('C', 7), ('H', 11), ('M', 14), ('L', 13), ('K', 16)]),
        'E': (16, [('C', 7), ('F', 4), ('H', 5)]),
        'F': (20, [('E', 4), ('G', 9)]),
        'G': (17, [('F', 9), ('N', 12)]),
        'H': (11, [('C', 8), ('D', 11), ('E', 5), ('I', 3)]),
        'I': (10, [('H', 3), ('J', 4)]),
        'J': (8,  [('I', 4), ('N', 3), ('P', 8)]),
        'K': (4,  [('D', 16), ('L', 5), ('N', 7), ('P', 4)]),
        'L': (7,  [('D', 13), ('K', 5), ('M', 9), ('O', 4)]),
        'M': (10, [('D', 14), ('L', 9), ('O', 5)]),
        'N': (7,  [('G', 12), ('J', 3), ('K', 7), ('P', 7)]),
        'O': (5,  [('L', 4),  ('M', 5)]),
        'P': (0,  [('J', 8), ('K', 4), ('N', 7)])
    }


def astar(graph, start, goal):
    '''
    '''
    # Here we are generating a "table" to build a refrence of shortest distance
    table = {}
    for vertex in graph.keys():
        if vertex == start:
            table[vertex] = (0, start)
            continue
        table[vertex] = (float('inf'), None)  # (distance, from node)

    # here we are generating the shortest distance to the goal
    table_vertices = set(table.keys())
    visted = [start]
    unvisted = table_vertices ^ set(visted)

    # Unlike empty visted in Djik, With A* nodes won't be visted
    while not visted[-1] == goal:
        current = visted[-1]
        min = (None, float("inf"))
        for vertex_connection in graph[current][1]:
            # Adding the heuristic to change Djiski
            heurestic = graph[current][0]
            total_distance = table[current][0] + \
                vertex_connection[1] + heurestic

            if total_distance < table[vertex_connection[0]][0]:
                table[vertex_connection[0]] = (total_distance, current)

            if not vertex_connection[0] in visted:
                nxt_vertix = vertex_connection
                if min[1] > nxt_vertix[1]:
                    min = nxt_vertix

        if not min[1] == float("inf"):
            nxt_vertix = min

        visted.append(nxt_vertix[0])
        unvisted.remove(nxt_vertix[0])

    # get the shortest path from the goal
    path = [goal]
    while not path[0] == start:
        pre_vertex = table[path[0]][1]
        path.insert(0, pre_vertex)
    return tuple(path)


print(astar(example_graph_large, 'A', 'Goal'))

