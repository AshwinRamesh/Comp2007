class graph:
    size,
    root

#this is the node object
class node:
    element,
    parent,
    children, #iterative 
    size, # size of tree from below node
    discovery, # discovery time
    finish, # finish time
    downUp, # down&up value
    cutVertex, # true/false if cut vertex
    breakableNode, # true/false if a cut vertex will immediately make this a seperate forest
    visited,
    disconnectingPower

#DFS runs in O(m) since it is a connected graph

def DFS(G):
	for vertex u in G:
		u.visted = False
		u.parent = None
	time = 0
	for vertex u in G:
		if u.visted == False:
			u.size = DFS_VISIT(u)
    return root

def DFS_VISIT(u):
	time = time + 1
	u.discovery() = time
	u.visited() = True
	for children v in u:
		if v.visted() == False:
			v.parent() = u
			DFS_VISIT(v)
	time = time + 1
	u.finish = time
    u.size = the number of nodes below the current node



#Cut Verticies Algorithm: runs O(n^2)

def getCutVertex(G):
    root = DFS(G) # run DFS on G to compute T and d[u for eac u in V
    if root.children.count > 1:
        root.cutVertex = True
        for child in root.children:
            child.breakableNode = True
    for v internal node of T:
    	for each child v of u in T:
    		if v.downUp = u.discovery:
    			v.cutVertex = True
                v.breakableNode = True
    return G

# this function will calculate the disconnecting power
def DisconnectingPower():
    G = getCutVertex()
    for vertex in G:
        if vertex.cutVertex == False:
            vertex.disconnectingPower = 0
        else:
            tempCount = G.size - 1 # take into account the removed node
            tempArray = []
            for child in vertex.children:
                if child.breakableNode:
                    tempArray.append(child.size) # append smaller forest size into array
                    G.size = G.size - child.size # remove all nodes below the child (inclusive) to get the larger forest
                vertex.disconnectingPower = sum of the multiplication of each array element in tempArray x tempCount
    return G


Simplified Algorithm:

The idea behind this algorithm to run in O(n) time is to modify the DFS algoritm to calculate how many nodes are below every other node. This will keep the running time of O(m) as we are guaranteed that this is a connected graph.

Now the cut verticies algorithm will use the result of the DFS and will take O(n^2) time to run. The idea of this algorithm is to flag all cut verticies. 

The final peice is the actual algorithm to calculate the Disconnecting Power. This algorithm will iterate through every vertex in the Graph and then iterate through the children of that vertex to calculate the DP.
The idea is to use the size attribute that we calculated in the DFS to make the process more effecient. This double iteration will ensure a n^2 running time.

Overall the running time will be O(m) + O(n^2) + O(n^2) = O(n^2)


Correctness:

This algorith is correct because:
    - The assumtion is that by removing one node, there will be one MAJOR forest above the removed node and many small forests below the node.
    - Now some of the nodes below the removed node will have back edges.
    - This means that parts of the smaller forests actually belong to the MAJOR forest.
    - The size of the major forest is (n - all the nodes that take into account back edges)
    - In the case that some nodes do not have back edges, then the size of the forest is the size attribute that we calculated during the DFS.
    - So finally you will have a value for the major forest and many values for smaller forests. Multiply across and add for the disconnecting power.