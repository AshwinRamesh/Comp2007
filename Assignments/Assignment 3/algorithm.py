def findMST(graph):
    set nodeA, nodeB, edgeA, edgeB
    for node in graph:
        if node.singleConnect == False:
            nodeA.append(node)
        else:
            nodeB.append(node)
    for edge in graph:
        if edge connects two black nodes:
            edgeA.append(edge)
        elif edge connects two green nodes:
            remove edge
        else:
            edgeB.append(edge)
    graph = Kruskal(graph,nodeA,edgeA) # run for black nodes
    graph = Kruskal(graph,nodeB,edgeA) # run for green nodes
    return graph

def Kruskal(graph,nodeA,edgeA):
    sort edgeA by increasing c-value:
    answer = []
    components = make_sets(nodeA)
    for (u,v) in edgeA:
        if find(components,u) != find(components,v):
            answer.append((u,v))
            union(components,u,v)
    return answer