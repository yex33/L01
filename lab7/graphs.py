from collections import deque
from typing import Dict, List

from lab7 import Graph


def BFS2(G, node1, node2):
    if node1 == node2:
        return [node1]
    Q = deque([node1])
    marked = {node1: True}
    prev = {}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                prev[node] = current_node
    if node2 not in prev:
        return []
    else:
        path = []
        at = node2
        while not at == node1:
            path.append(at)
            at = prev[at]
        path.append(node1)
        path.reverse()
        return path


def DFS2(G: Graph, source: int, target: int) -> List[int]:
    if source == target:
        return [source]
    stack = [source]
    marked = {node: False for node in G.adj}
    marked[source] = True
    path = []
    while len(stack) != 0:
        cur = stack[-1]
        if len(path) == 0 or path[-1] != cur:
            path.append(cur)
        has_unvisited = False
        for node in G.adj[cur]:
            if node == target:
                return path + [node]
            if not marked[node]:
                stack.append(node)
                marked[node] = True
                has_unvisited = True
        if not has_unvisited:
            path.pop()
            stack.pop()
    return []


def BFS3(G: Graph, source: int) -> Dict[int, int]:
    queue = deque([source])
    marked = {node: False for node in G.adj}
    marked[source] = True
    pred = {}
    while len(queue) != 0:
        cur = queue.popleft()
        for node in G.adj[cur]:
            if not marked[node]:
                pred[node] = cur
                queue.append(node)
                marked[node] = True
    return pred


def DFS3(G: Graph, source: int) -> Dict[int, int]:
    stack = [source]
    marked = {node: False for node in G.adj}
    pred = {}
    while len(stack) != 0:
        cur = stack.pop()
        if not marked[cur]:
            for node in G.adj[cur]:
                if node not in pred and not marked[node]:
                    pred[node] = cur
                stack.append(node)
            marked[cur] = True
    return pred


def has_cycle(G: Graph) -> bool:
    sources = set(G.adj.keys())
    while len(sources) > 0:
        source = list(sources)[0]
        queue = deque([source])
        marked = {node: False for node in G.adj}
        marked[source] = True
        while len(queue) != 0:
            cur = queue.popleft()
            sources.remove(cur)
            for node in G.adj[cur]:
                if not marked[node]:
                    marked[node] = True
                    queue.append(node)
                elif node in queue:
                    return True
    return False


# def has_cycle(G: Graph) -> bool:
#     sources = set(G.adj.keys())
#     while len(sources) > 0:
#         source = list(sources)[0]
#         stack = [source]
#         marked = {node: False for node in G.adj}
#         marked[source] = True
#         path = []
#         while len(stack) != 0:
#             cur = stack[-1]
#             if len(path) == 0 or path[-1] != cur:
#                 path.append(cur)
#             if cur in sources:
#                 sources.remove(cur)
#             has_unvisited = False
#             for node in G.adj[cur]:
#                 if marked[node] and node != cur:
#                     return True
#                 if not marked[node]:
#                     stack.append(node)
#                     marked[node] = True
#                     has_unvisited = True
#             if not has_unvisited:
#                 path.pop()
#                 stack.pop()
#     return False


def is_connected(G: Graph):
    for i in range(G.number_of_nodes()):
        for j in range(i + 1, G.number_of_nodes()):
            keys = list(G.adj.keys())
            if DFS2(G, keys[i], keys[j]) == []:
                return False
    return True
