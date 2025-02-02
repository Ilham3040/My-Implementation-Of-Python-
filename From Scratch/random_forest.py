import numpy as np
from decision_tree import DecisionTree

class RandomForest:
    def __init__(self, n_trees=100, max_depth=None, max_features=None):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.max_features = max_features
        self.trees = []

    def fit(self, X, y):
        for _ in range(self.n_trees):
            tree = DecisionTree(max_depth=self.max_depth)
            X_sample, y_sample = self._bootstrap_sample(X, y)
            tree.fit(X_sample, y_sample)
            self.trees.append(tree)

    def _bootstrap_sample(self, X, y):
        n_samples = X.shape[0]
        indices = np.random.choice(n_samples, size=n_samples, replace=True)
        X_sample = X[indices]
        y_sample = y[indices]
        return X_sample, y_sample

    def predict(self, X):
        tree_preds = np.asarray([tree.predict(X) for tree in self.trees])
        tree_preds = tree_preds.T  # Transpose to shape (n_samples, n_trees)
        return [self._majority_vote(preds) for preds in tree_preds]

    def _majority_vote(self, preds):
        return np.bincount(preds).argmax()
