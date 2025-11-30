from dag import find_cycle_dag


def test_simple_cycle():
    graph = {
        0: [1],
        1: [2],
        2: [0]
    }
    has_cycle, result = find_cycle_dag(graph)
    
    assert has_cycle == True
    assert len(result) == 4
    assert set(result) == {0, 1, 2}

def test_no_cycle_dag():
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": []
    }
    has_cycle, result = find_cycle_dag(graph)
    
    assert has_cycle == False
    assert len(result) == 4
    assert set(result) == {"A", "B", "C", "D"}
    # Проверяем корректность топологической сортировки
    assert result.index("D") > result.index("B")
    assert result.index("D") > result.index("C")
    assert result.index("B") > result.index("A")
    assert result.index("C") > result.index("A")

def test__loop():
    graph = {
        0: [0, 1],
        1: [2],
        2: []
    }
    has_cycle, result = find_cycle_dag(graph)
    
    assert has_cycle == True
    assert len(result) == 2
    assert result[0] == result[1] == 0

def test_multiple_cycles():
    graph = {
        0: [1],
        1: [2, 3],
        2: [0],  # цикл 0-1-2
        3: [4],
        4: [1]   # цикл 1-3-4
    }
    has_cycle, result = find_cycle_dag(graph)
    
    assert has_cycle == True
    assert len(result) >= 4

def test_disconnected_graph_with_cycle():
    graph = {
        0: [1],
        1: [0],  
        2: [3],
        3: []    
    }
    has_cycle, result = find_cycle_dag(graph)
    
    assert has_cycle == True
    assert len(result) == 3
    assert set(result) == {0, 1}

def test_disconnected_dag():
    graph = {
        "A": ["B"],
        "B": [],
        "C": ["D"],
        "D": []
    }
    has_cycle, result = find_cycle_dag(graph)
    
    assert has_cycle == False
    assert len(result) == 4
    assert set(result) == {"A", "B", "C", "D"}

def test_empty_graph():
    graph = {}
    has_cycle, result = find_cycle_dag(graph)
    
    assert has_cycle == False
    assert result == []

def test_single_vertex():
    graph = {0: []}
    has_cycle, result = find_cycle_dag(graph)
    
    assert has_cycle == False
    assert result == [0]

def test_complex_dag():
    """Тест сложного DAG"""
    graph = {
        1: [2, 3],
        2: [4],
        3: [4, 5],
        4: [6],
        5: [6],
        6: []
    }
    has_cycle, result = find_cycle_dag(graph)
    
    assert has_cycle == False
    assert len(result) == 6

def test_string_vertices_cycle():
    graph = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A", "D"],
        "D": []
    }
    has_cycle, result = find_cycle_dag(graph)
    
    assert has_cycle == True
    assert len(result) == 4
    assert set(result) == {"A", "B", "C"}

