from functools import partial

from lab9 import *


def bellman_ford_approx(G: DirectedWeightedGraph, source, k):
    freq = {node: 0 for node in G.adj.keys()} # relaxation count
    dist = {} # Distance dictionary
    nodes = list(G.adj.keys())

    #Initialize distances
    for node in nodes:
        dist[node] = 99999
    dist[source] = 0

    #Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour) and freq[neighbour] <= k:
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    freq[neighbour] += 1
    return dist


def bellman_ford_approx2(G: DirectedWeightedGraph, source, k):
    freq = {node: 0 for node in G.adj.keys()} # relaxation count
    done: set = set(G.adj.keys())

    dist = {} # Distance dictionary
    nodes = list(G.adj.keys())

    #Initialize distances
    for node in nodes:
        dist[node] = 99999
    dist[source] = 0
    done.remove(source)

    #Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if len(done) == 0:
                    return dist
                if dist[neighbour] > dist[node] + G.w(node, neighbour) and freq[neighbour] <= k:
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    freq[neighbour] += 1
                elif freq[neighbour] == k:
                    done.discard(neighbour)
    return dist


def all_pairs_dijkstra(G: DirectedWeightedGraph):
    # return list(map(partial(dijkstra, G), sorted(list(G.adj.keys()))))
    return list(map(list, map(dict.values, map(partial(dijkstra, G), sorted(list(G.adj.keys()))))))


def all_pairs_bellman_ford(G: DirectedWeightedGraph):
    return list(map(list, map(dict.values, map(partial(bellman_ford, G), sorted(list(G.adj.keys()))))))
