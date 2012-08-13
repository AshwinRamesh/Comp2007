y = {
		"A": ["B"],
		"B": ["A","B","C","E"],
		"C": ["B","D"],
		"D": ["B","C"],
		"E": ["B"]
	}

for node in y:
	print node + ": " + str(y[node])

def DFS(G):
	#mark verticies as unvisited"
	#set verticies parent as None"
	time = 0
	for node in G:
		if 