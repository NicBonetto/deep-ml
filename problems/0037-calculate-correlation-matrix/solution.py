import numpy as np

def calculate_correlation_matrix(X, Y=None):
	Y = Y if Y is not None else X
	
	Xc = X - X.mean(axis=0)
	Yc = Y - Y.mean(axis=0)

	cov = Xc.T @ Yc / X.shape[0]

	std_x = np.std(X, axis=0)
	std_y = np.std(Y, axis=0)
	corr = cov / np.outer(std_x, std_y)
	return corr





	

		

				


