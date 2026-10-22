import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    """
    Perform gradient descent optimization.
    
    Args:
        X: Feature matrix of shape (m, n)
        y: Target values of shape (m,)
        weights: Initial weights of shape (n,)
        learning_rate: Step size for gradient descent
        n_epochs: Number of complete passes through the dataset
        batch_size: Size of batches for mini-batch gradient descent (default: 1)
        method: Type of gradient descent ('batch', 'stochastic', or 'mini_batch')
    
    Returns:
        Optimized weights
    """
    m = len(y)
    
    for _ in range(n_epochs):
        if method == "batch":
            preds = X @ weights 
            errors = preds - y
            grad = 2 * X.T @ errors / m 
            weights -= learning_rate * grad 
        
        elif method == "stochastic":
            for i in range(m):
                xi, yi = X[i], y[i]
                pred = xi @ weights 
                errors = pred - yi
                grad = 2 * xi * errors
                weights -= learning_rate * grad
        
        else:
            for start in range(0, m, batch_size):
                Xb = X[start:start+batch_size]
                yb = y[start:start+batch_size]
                preds = Xb @ weights 
                errors = preds - yb 
                grad = 2 * Xb.T @ errors / len(yb)
                weights -= learning_rate * grad
        
    return weights
