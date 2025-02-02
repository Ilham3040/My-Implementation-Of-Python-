import numpy as np
import pandas as pd

class SVM:
    def __init__(self, learning_rate=0.01, n_iterations=1000, regularization_param=0.01):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.regularization_param = regularization_param
        self.theta = None

    def fit(self, X, y):
        if isinstance(X, pd.DataFrame):
            X = X.values
        if isinstance(y, pd.Series):
            y = y.values
        
        m, n = X.shape
        self.theta = np.zeros(n)
        y = 2 * y - 1  # Convert labels from {0, 1} to {-1, 1}

        for _ in range(self.n_iterations):
            for i in range(m):
                condition = y[i] * np.dot(X[i], self.theta) >= 1
                if condition:
                    self.theta -= self.learning_rate * (2 * self.regularization_param * self.theta)
                else:
                    self.theta -= self.learning_rate * (2 * self.regularization_param * self.theta - np.dot(X[i], y[i]))
    
    def predict(self, X):
        if isinstance(X, pd.DataFrame):
            X = X.values
        return np.sign(X.dot(self.theta))
