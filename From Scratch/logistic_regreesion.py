import numpy as np
import pandas as pd

class LogisticRegression:
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
            predictions = self.sigmoid(X.dot(self.theta))
            errors = y - predictions
            gradients = -X.T.dot(errors) / m
            self.theta -= self.learning_rate * gradients

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def predict(self, X):
        if isinstance(X, pd.DataFrame):
            X = X.values
        return np.round(self.sigmoid(X.dot(self.theta)))
