from lab8 import WeightedGraph


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
