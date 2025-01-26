import sys
from collections import defaultdict, deque


def make_graph(data):
    graph = defaultdict(list)

    for i, j in data:
        graph[i].append(j)
        graph[j].append(i)

    return graph


def bfs(graph, start, visited=None):
    queue = deque([start])
    component = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            component.append(node)
            queue.extend(graph[node])

    return component


def find_all_components(graph, m):
    visited = set()
    components = []

    for v in range(1, m + 1):
        if v not in visited:
            component = bfs(graph, v, visited)
            components.append(sorted(component))

    return components


def main():
    # mock_data = [[3, 1], [1, 2], [5, 4], [2, 3]]
    # mock_m = 6
    # mock_n = 4
    data = sys.stdin.readlines()
    m, n = map(int, data[0].split())

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

