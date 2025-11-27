import heapq
from typing import Dict, List, Tuple, Union


def dijkstra(
    graph: Dict[Union[int, str], Dict[Union[int, str], Union[int, float]]],
    start: Union[int, str],
    end: Union[int, str],
) -> Tuple[List[Union[int, str]], Union[int, float]]:
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    parent = {node: None for node in graph}

    priority_queue = [(0, start)]  # или minheap, здесь сути не меняет

    while priority_queue:
        cur_distance, cur_node = heapq.heappop(priority_queue)

        if cur_node == end:
            break

        if cur_distance > distances[cur_node]:
            continue

        for neighbour_node, dist in graph[cur_node].items():
            distance = cur_distance + dist

            if distance < distances[neighbour_node]:
                distances[neighbour_node] = distance
                parent[neighbour_node] = cur_node
                heapq.heappush(priority_queue, (distance, neighbour_node))

    if distances[end] == float("inf"):
        return [], float("inf")

    path = []
    cur = end

    while cur is not None:
        path.append(cur)
        cur = parent[cur]

    path.reverse()

    return path, distances[end]
