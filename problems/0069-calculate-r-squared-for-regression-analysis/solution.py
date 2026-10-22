
import numpy as np

def r_squared(y_true, y_pred):
	y_mean = np.mean(y_true)
	ss_res = np.sum((y_pred - y_true) ** 2)
	ss_mean = np.sum((y_true - y_mean) ** 2)

	return 1 - (ss_res / ss_mean)
