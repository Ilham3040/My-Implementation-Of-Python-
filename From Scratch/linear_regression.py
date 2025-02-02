import numpy as np
import pandas as pd

class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.theta = None

    def fit(self, X, y):
        if isinstance(X, pd.DataFrame):
            X = X.values
        if isinstance(y, pd.Series):
            y = y.values
        
        m, n = X.shape
        self.theta = np.zeros(n)
        for _ in range(self.n_iterations):
            gradients = -2 * X.T.dot(y - X.dot(self.theta)) / m
            self.theta -= self.learning_rate * gradients

    def predict(self, X):
        if isinstance(X, pd.DataFrame):
            X = X.values
        return X.dot(self.theta)
