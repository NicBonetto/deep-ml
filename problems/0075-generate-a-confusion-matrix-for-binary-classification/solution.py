
from collections import Counter

def confusion_matrix(data):
	counts = Counter(tuple(pair) for pair in data)
	
	result = [[0 for _ in range(2)] for _ in range(2)]
	for (x, y), count in counts.items():
		result[1 - x][1 - y] = count

	return result

