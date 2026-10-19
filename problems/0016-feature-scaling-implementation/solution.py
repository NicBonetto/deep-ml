import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	means = data.mean(axis=0, keepdims=True)
	dev = data.std(axis=0, keepdims=True)
	standardized_data = (data - means) / dev

	matrix_min = data.min(axis=0, keepdims=True) 
	matrix_max = data.max(axis=0, keepdims=True)
	normalized_data = (data - matrix_min) / (matrix_max - matrix_min)

	return standardized_data, normalized_data