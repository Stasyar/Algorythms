def dfs(g, node, visited=None):
    """DFS algorythm itself"""
    if not visited:
        visited = set()  # Set for visited vertex (set allows to keep only unique objects)

    visited.add(node)

    for next in g[node]:
        if next not in visited:
              dfs(graph, next, visited)

    return visited

def main(graph):
    """Function to go through all vertex in a graph"""
    components = []

    for ver in graph:
        component = dfs(graph, ver)
        if component not in components:
            components.append(component)

    return components


if __name__ == '__main__':
    graph = {1: [2, 3],
             2: [1, 4, 5],
             3: [1],
             4: [2],
             5: [2],
             6: []
    }

    print(dfs(graph, 1))
    print(main(graph))