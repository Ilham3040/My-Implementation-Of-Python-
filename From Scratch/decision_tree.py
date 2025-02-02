import numpy as np
import pandas as pd

class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
        self.tree = None

    def fit(self, X, y):
        if isinstance(X, pd.DataFrame):
            X = X.values
        self.tree = self._build_tree(X, y, depth=0)

    def _build_tree(self, X, y, depth):
        if len(np.unique(y)) == 1:
            return {'label': np.unique(y)[0]}
        
        if self.max_depth is not None and depth >= self.max_depth:
            return {'label': self._majority_class(y)}
        
        best_split, (X_left, y_left), (X_right, y_right) = self._best_split(X, y)
        
        if best_split is None:
            return {'label': self._majority_class(y)}
        
        feature_index, threshold = best_split
        left_tree = self._build_tree(X_left, y_left, depth + 1)
        right_tree = self._build_tree(X_right, y_right, depth + 1)
        
        return {
            'feature_index': feature_index,
            'threshold': threshold,
            'left': left_tree,
            'right': right_tree
        }

    def _best_split(self, X, y):
        best_gini = float("inf")
        best_split = None
        best_left, best_right = None, None
        
        n_features = X.shape[1]
        
        for feature_index in range(n_features):
            thresholds = np.unique(X[:, feature_index])
            for threshold in thresholds:
                X_left, y_left, X_right, y_right = self._split_dataset(X, y, feature_index, threshold)
                gini = self._gini_impurity(y_left, y_right)
                
                if gini < best_gini:
                    best_gini = gini
                    best_split = (feature_index, threshold)
                    best_left, best_right = (X_left, y_left), (X_right, y_right)
        
        return best_split, best_left, best_right

    def _gini_impurity(self, y_left, y_right):
        m_left, m_right = len(y_left), len(y_right)
        total_size = m_left + m_right
        return (m_left / total_size) * self._gini(y_left) + (m_right / total_size) * self._gini(y_right)

    def _gini(self, y):
        m = len(y)
        return 1.0 - sum((np.sum(y == c) / m) ** 2 for c in np.unique(y))

    def _split_dataset(self, X, y, feature_index, threshold):
        left_mask = X[:, feature_index] <= threshold
        right_mask = ~left_mask
        X_left, y_left = X[left_mask], y[left_mask]
        X_right, y_right = X[right_mask], y[right_mask]
        return X_left, y_left, X_right, y_right

    def _majority_class(self, y):
        return np.bincount(y).argmax()

    def predict(self, X):
        if isinstance(X, pd.DataFrame):
            X = X.values
        return [self._predict_one(x, self.tree) for x in X]

    def _predict_one(self, x, tree):
        if 'label' in tree:
            return tree['label']
        
        feature_index = tree['feature_index']
        threshold = tree['threshold']
        
        if x[feature_index] <= threshold:
            return self._predict_one(x, tree['left'])
        else:
            return self._predict_one(x, tree['right'])
