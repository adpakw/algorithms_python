from typing import Dict, List, Tuple, Any


def find_cycle_dag(graph: Dict[Any, List[Any]]) -> Tuple[bool, List[Any]]:
    # graph keys to numbers
    vertices = list(graph.keys())
    vertex_to_idx = {vertice: i for i, vertice in enumerate(vertices)}
    idx_to_vertex = {i: vertice for i, vertice in enumerate(vertices)}

    customized_graph = dict()
    for vertex, neighbors in graph.items():
        customized_graph[vertex_to_idx[vertex]] = []
        for neighbor in neighbors:
            customized_graph[vertex_to_idx[vertex]].append(vertex_to_idx[neighbor])

    # Find cycle

    # 0 - не посещена, 1 - в обработке, 2 - обработана
    state = [0] * len(vertices)
    parent = [-1] * len(vertices)
    cycle = []

    def dfs_find_cycle(customized_graph, vertice, state, parent, cycle):
        state[vertice] = 1

        for neighbor in customized_graph[vertice]:
            if not cycle:
                if state[neighbor] == 0:
                    parent[neighbor] = vertice

                    if dfs_find_cycle(customized_graph, neighbor, state, parent, cycle):
                        return True
                elif state[neighbor] == 1:
                    current = vertice
                    while current != neighbor:
                        cycle.append(current)
                        current = parent[current]
                    cycle.append(neighbor)
                    cycle.append(vertice)
                    cycle.reverse()
                    return True

        state[vertice] = 2
        return False

    for i in range(len(vertices)):
        if state[i] == 0 and not cycle:
            dfs_find_cycle(customized_graph, i, state, parent, cycle)

    if cycle:
        cycle_vertices = [idx_to_vertex[i] for i in cycle]
        return True, cycle_vertices

    # topological_sort
    visited = [False] * len(vertices)
    topological_order = []

    def dfs_topological_sort(customized_graph, vertice, visited, topological_order):
        visited[vertice] = True
        for neighbor in customized_graph[vertice]:
            if not visited[neighbor]:
                dfs_topological_sort(
                    customized_graph, neighbor, visited, topological_order
                )
        topological_order.append(vertice)

    for i in range(len(vertices)):
        if not visited[i]:
            dfs_topological_sort(customized_graph, i, visited, topological_order)

    topological_order.reverse()
    topological_vertices = [idx_to_vertex[i] for i in topological_order]
    return False, topological_vertices
