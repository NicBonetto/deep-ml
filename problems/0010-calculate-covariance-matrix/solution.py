def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	def covariance(vec1, vec2):
		vec1_mean = sum(vec1) / len(vec1)
		vec2_mean = sum(vec2) / len(vec2)

		sum_products = sum((x - vec1_mean) * (y - vec2_mean) for x, y in zip(vec1, vec2))

		return sum_products / (len(vec1) - 1)
	
	cov_matrix = [[0 for _ in range(len(vectors))] for _ in range(len(vectors))]

	for i in range(len(vectors)):
		for j in range(len(vectors)):
			cov = covariance(vectors[i], vectors[j])
			cov_matrix[i][j] = cov

	return cov_matrix