from collections import deque
from typing import Dict, List


def bfs_all_graph(graph: Dict[int, List[int]]) -> List[List[int]]:
    def bfs(graph: Dict[int, List[int]], root: int, visited: List[int]) -> List[int]:
        bfs_result = []
        nodes_queue = deque()

        visited.append(root)
        nodes_queue.append(root)

        while nodes_queue:
            cur_node = nodes_queue.popleft()
            bfs_result.append(cur_node)

            for neighbour in graph[cur_node]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    nodes_queue.append(neighbour)

        return bfs_result

    visited = []
    result = []

    for node in graph.keys():
        if node not in visited:
            result.append(bfs(graph, node, visited))

    return result


def dfs_all_graph(graph: Dict[int, List[int]]) -> List[List[int]]:
    def dfs(graph: Dict[int, List[int]], root: int, visited: List[int]) -> List[int]:
        dfs_result = []
        nodes_stack = []

        visited.append(root)
        nodes_stack.append(root)

        while nodes_stack:
            cur_node = nodes_stack.pop()
            dfs_result.append(cur_node)

            for neighbour in graph[cur_node]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    nodes_stack.append(neighbour)

        return dfs_result

    visited = []
    result = []

    for node in graph.keys():
        if node not in visited:
            result.append(dfs(graph, node, visited))

    return result
