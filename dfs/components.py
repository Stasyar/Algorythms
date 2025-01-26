import sys
from collections import defaultdict, deque


def make_graph(data, m):
    connected_ver = set(sum(data, []))
    all_ver = set([i for i in range(1, m + 1)])
    unconnected_ver = all_ver - connected_ver

    for i in unconnected_ver:
        data.append([i, i])

    graph = defaultdict(list)

    for i, j in data:
        graph[i].append(j)
        graph[j].append(i)

    return graph


def dfs(graph, start, visited=None):
    # if not visited:
    #     visited = []
    #
    # if start not in visited:
    #     visited.append(start)
    #
    #     for next in graph.get(start):
    #         dfs(graph, next, visited)
    #
    # return visited

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
            component = dfs(graph, v, visited)
            components.append(sorted(component))

    return components


def main():
    # mock_data = [[3, 1], [1, 2], [5, 4], [2, 3]]
    # mock_m = 6
    # mock_n = 4
    data = sys.stdin.readlines()
    m, n = map(int, data[0].split())

    data = [list(map(int, line.split())) for line in data[1:]]

    graph = make_graph(data, m)
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

