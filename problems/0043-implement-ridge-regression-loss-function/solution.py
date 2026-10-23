import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	preds = X @ w 
	errors = np.mean((preds - y_true) ** 2)
	reg = alpha * np.sum(w ** 2)
	return errors + reg
