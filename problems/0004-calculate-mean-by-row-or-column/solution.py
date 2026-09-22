def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	rows = len(matrix)
	cols = len(matrix[0])

	for i in range(rows if mode == 'row' else cols):
		mean = 0
		for j in range(cols if mode == 'row' else rows):
			if mode == 'row':
				mean += matrix[i][j]
			else:
				mean += matrix[j][i]
		if mode == 'row':
			means.append(mean / cols)
		else:
			means.append(mean / rows)
		
	return means