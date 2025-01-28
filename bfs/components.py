""" Not the best way to find components. DFS works perfect for such purposes. Here is my first try."""
import sys
from collections import defaultdict, deque


def make_graph(data):
    """Parse data from stdin to make graph"""
    graph = defaultdict(list)

    for i, j in data:
        graph[i].append(j)
        graph[j].append(i)

    return graph


def bfs(graph, start, visited=None):
    """BFS algorythm itself"""
    queue = deque([start])  # Much faster and more convenient than list
    component = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            component.append(node)
            queue.extend(graph[node])

    return component


def find_all_components(graph, m):
    """Function to go through all vertex in a graph"""
    visited = set()
    components = []

    for v in range(1, m + 1):
        if v not in visited:
            component = bfs(graph, v, visited)
            components.append(sorted(component))

    return components


def main():
    """Bgi function again for parsing data mostly"""
    # mock_data = [[3, 1], [1, 2], [5, 4], [2, 3]]
    # mock_m = 6
    # mock_n = 4
    data = sys.stdin.readlines()
    m, n = map(int, data[0].split())  # Don't actually know why I need n which stands for edge

    data = [list(map(int, line.split())) for line in data[1:]]

    graph = make_graph(data)
    components = find_all_components(graph, m)

    result_list = [[len(components)]]

    for com in components:
        result_list.append([len(com)])
        result_list.append(com)

    return result_list


if __name__ == "__main__":
    final_data = main()

    for i in final_data:
        print(*i)

