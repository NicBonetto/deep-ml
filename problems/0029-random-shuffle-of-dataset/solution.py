import numpy as np

def shuffle_data(X, y, seed=None):
	np.random.seed(seed)
	for i in range(len(X) - 1, 0, -1):
		j = np.random.randint(0, i+1)
		X[[i, j]] = X[[j, i]]
		y[[i, j]] = y[[j, i]]
	return (X, y)

	