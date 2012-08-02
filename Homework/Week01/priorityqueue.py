min_priority = 100
min_item = ""
queue = [[2,"A"],[1,"C"],[3,"B"]]

for item in queue:
	if item[0] < min_priority:
		min_priority = item[0]
		min_item = item

print min_item
print min_priority
