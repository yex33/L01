from lab8 import WeightedGraph
from min_heap import Element, MinHeap


def prim1(graph: WeightedGraph) -> WeightedGraph:
    vis = set()
    vis.add(list(graph.adj.keys())[0])
    mst = WeightedGraph(graph.number_of_nodes())
    while len(vis) < graph.number_of_nodes():
        edges = [(v1, v2[0], graph.w(v1, v2[0])) for v1 in vis for v2 in graph.adjacent_nodes(v1)]
        min_edge = (-1, -1, 10000)
        for v1, v2, w in edges:
            if w < min_edge[2] and ((v1 not in vis and v2 in vis)
                                    or (v1 in vis and v2 not in vis)):
                min_edge = (v1, v2, w)
        mst.add_edge(*min_edge)
        vis.add(min_edge[1])
    return mst


def prim2(graph: WeightedGraph) -> WeightedGraph:
    v1 = list(graph.adj.keys())[0]
    vis = set()
    vis.add(v1)
    h = MinHeap(list(Element(node, 10000) for node in graph.adj.keys() if node != v1))
    edge_to = [-1 for _ in graph.adj.keys()]
    mst = WeightedGraph(graph.number_of_nodes())
    while not h.is_empty():
        for v2, w in graph.adjacent_nodes(v1):
            if v2 not in vis:
                h.decrease_key(v2, w)
                if edge_to[v2] == -1 or graph.w(edge_to[v2], v2) > graph.w(v1, v2):
                    edge_to[v2] = v1
        edge = h.extract_min()
        v2, w = edge.value, edge.key
        mst.add_edge(edge_to[v2], v2, w)
        vis.add(v2)
        v1 = v2
    return mst
