import random
from time import time


def BFS(G,s):
    layers = []
    current_layer = [s]
    next_layer = []
    seen = { u : False for u in G }
    seen[s] = True
    while len(current_layer) > 0:
        layers.append(current_layer)
        for u in current_layer:
            for v in G[u]:
                if not seen[v]:
                    next_layer.append(v)
                    seen[v] = True
        current_layer = next_layer
        next_layer = []

    return layers


G = { 'a': ['b', 'c'], 'b' : ['a', 'd', 'c'], 'c' : ['a', 'b'], 'd' : [ 'b' ] }
