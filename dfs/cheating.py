from collections import defaultdict
import sys


def make_graph(data):
    graph = defaultdict(list)

    for i, j in data:
        graph[i].append(j)
        graph[j].append(i)

    return graph


def dfs(graph, start, color, colors):
    colors[start] = color

    for neighbour in graph[start]:
        if colors[neighbour] == 0:
            if not dfs(graph, neighbour, -color, colors):
                return False
        else:
            if colors[neighbour] == colors[start]:
                return False
    return True


def go_through_each_student(graph, m):
    colors = [0 for _ in range(m + 1)]

    for st in graph:
        if colors[st] == 0:
            if not dfs(graph, st, 1, colors):
                return 'NO'

    return 'YES'


def main():
    m, n = (sys.stdin.readline().split())
    data = [list(map(lambda x: int(x), line.strip().split())) for line in sys.stdin.readlines()]
    # m = 3
    # data = [[1, 2], [2, 3], [1, 3]]
    # data1 = [[1, 2], [2, 3]]
    graph = make_graph(data)
    return go_through_each_student(graph, int(m))


if __name__ == '__main__':
    d = main()
    print(d)