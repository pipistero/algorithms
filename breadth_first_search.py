from collections import deque

graph = {'1': ['2', '6', '8'],
		 '2': ['1', '3'],
		 '3': ['2', '4', '5'],
		 '4': ['3', '5'],
		 '5': ['3', '4', '6'],
		 '6': ['1', '5', '7'],
		 '7': ['6', '9'],
		 '8': ['1', '9'],
		 '9': ['7', '8', '10', '11'],
		 '10': ['9'],
		 '11': ['9']
}

def is_finish(point):
	if point == '4':
		return True
	else:
		return False

def search(point):
	search_queue = deque()
	search_queue += graph[point]
	searched = []

	while search_queue:
		point_now = search_queue.popleft()
		if point_now not in searched:
			print(point_now)
			if is_finish(point_now):
				print("Finish is -", point_now)
				return True
			else:
				search_queue += graph[point_now]
				searched.append(point_now)

	return False 

search('1')
