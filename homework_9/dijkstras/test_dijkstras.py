from dijkstras import dijkstra
import pytest


def test_empty_graph():
    graph = {}

    with pytest.raises(KeyError):
        dijkstra(graph, "A", "B")


def test_single_node_graph():
    graph = {"A": {}}
    path, distance = dijkstra(graph, "A", "A")

    assert path == ["A"]
    assert distance == 0


def test_unreachable_destination():
    graph = {"A": {"B": 1}, "B": {"A": 1}, "C": {"D": 1}, "D": {"C": 1}}
    path, distance = dijkstra(graph, "A", "C")

    assert path == []
    assert distance == float("inf")


def test_same_start_and_end():
    graph = {"A": {"B": 1}, "B": {"A": 1, "C": 2}, "C": {"B": 2}}
    path, distance = dijkstra(graph, "B", "B")

    assert path == ["B"]
    assert distance == 0


def test_disconnected_graph():
    graph = {"A": {"B": 1}, "B": {"A": 1}, "C": {"D": 1}, "D": {"C": 1}, "E": {}}
    path, distance = dijkstra(graph, "A", "E")

    assert path == []
    assert distance == float("inf")


def test_multiple_paths():
    graph = {
        "A": {"B": 3, "C": 3},
        "B": {"A": 3, "D": 3.5, "E": 2.8},
        "C": {"A": 3, "E": 2.8, "F": 3.5},
        "D": {"B": 3.5, "E": 3.1, "G": 10},
        "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
        "F": {"G": 2.5, "C": 3.5},
        "G": {"F": 2.5, "E": 7, "D": 10},
    }
    path, distance = dijkstra(graph, "B", "F")

    assert path == ["B", "E", "C", "F"]
    assert distance == 9.1


def test_cycle_graph():
    graph = {"A": {"B": 1}, "B": {"C": 1}, "C": {"A": 1, "D": 1}, "D": {}}
    path, distance = dijkstra(graph, "A", "D")

    assert path == ["A", "B", "C", "D"]
    assert distance == 3


def test_zero_weight_edges():
    graph = {"A": {"B": 0}, "B": {"C": 1}, "C": {"D": 0}, "D": {}}
    path, distance = dijkstra(graph, "A", "D")

    assert path == ["A", "B", "C", "D"]
    assert distance == 1
