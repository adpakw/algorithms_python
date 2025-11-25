from graph import bfs_all_graph, dfs_all_graph


def sort_list_result(result):
    return sorted([sorted(group) for group in result])


def test_single_component():
    graph = {
        0: [1, 2, 3],
        1: [0, 4, 5],
        2: [0, 6],
        3: [0, 7],
        4: [1],
        5: [1],
        6: [2],
        7: [3],
    }
    expected = sort_list_result([[0, 1, 2, 3, 4, 5, 6, 7]])

    result_bfs = sort_list_result(bfs_all_graph(graph))
    result_dfs = sort_list_result(dfs_all_graph(graph))

    assert result_bfs == expected
    assert result_dfs == expected


def test_multiple_components():
    graph = {1: [2], 2: [1], 3: [4], 4: [3], 5: [6, 7], 6: [5], 7: [5]}
    expected = sort_list_result([[1, 2], [3, 4], [5, 6, 7]])

    result_bfs = sort_list_result(bfs_all_graph(graph))
    result_dfs = sort_list_result(dfs_all_graph(graph))

    assert result_bfs == expected
    assert result_dfs == expected


def test_isolated_nodes():
    graph = {1: [], 2: [3], 3: [2], 4: [], 5: [6], 6: [5]}
    expected = sort_list_result([[1], [4], [2, 3], [5, 6]])

    result_bfs = sort_list_result(bfs_all_graph(graph))
    result_dfs = sort_list_result(dfs_all_graph(graph))

    assert result_bfs == expected
    assert result_dfs == expected


def test_empty_graph():
    graph = {}
    expected = []

    result_bfs = sort_list_result(bfs_all_graph(graph))
    result_dfs = sort_list_result(dfs_all_graph(graph))

    assert result_bfs == expected
    assert result_dfs == expected


def test_single_node():
    graph = {1: []}
    expected = [[1]]

    result_bfs = sort_list_result(bfs_all_graph(graph))
    result_dfs = sort_list_result(dfs_all_graph(graph))

    assert result_bfs == expected
    assert result_dfs == expected


def test_cycle_graph():
    graph = {1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3]}
    expected = sort_list_result([[1, 2, 3, 4]])

    result_bfs = sort_list_result(bfs_all_graph(graph))
    result_dfs = sort_list_result(dfs_all_graph(graph))

    assert result_bfs == expected
    assert result_dfs == expected


def test_star_graph():
    graph = {1: [2, 3, 4, 5], 2: [1], 3: [1], 4: [1], 5: [1]}
    expected = sort_list_result([[1, 2, 3, 4, 5]])

    result_bfs = sort_list_result(bfs_all_graph(graph))
    result_dfs = sort_list_result(dfs_all_graph(graph))

    assert result_bfs == expected
    assert result_dfs == expected


def test__loops():
    graph = {1: [1, 2], 2: [1, 3], 3: [2], 4: [4, 4]}
    expected = sort_list_result([[1, 2, 3], [4]])

    result_bfs = sort_list_result(bfs_all_graph(graph))
    result_dfs = sort_list_result(dfs_all_graph(graph))

    assert result_bfs == expected
    assert result_dfs == expected


def test_complete_graph():
    graph = {1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2, 4], 4: [1, 2, 3]}
    expected = sort_list_result([[1, 2, 3, 4]])

    result_bfs = sort_list_result(bfs_all_graph(graph))
    result_dfs = sort_list_result(dfs_all_graph(graph))

    assert result_bfs == expected
    assert result_dfs == expected
