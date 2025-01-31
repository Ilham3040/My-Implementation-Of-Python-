
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("./apple_quality.csv")

# null_places = df.isnull().any(axis=1)
# df = df[~null_places]

df.dropna(inplace=True)

df.drop("A_id",axis=1,inplace=True)

df['Acidity'] = df['Acidity'].astype(float)

# df['Quality'] = df['Quality'].map({'good':1, 'bad':0})


le = LabelEncoder()

df['Quality'] = le.fit_transform(df['Quality'])

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1


outlier_mask = (df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))

outlier_indices = outlier_mask.any(axis=1)

df.drop(df[outlier_indices].index, inplace=True)


X = df.drop("Quality",axis=1)
y = df["Quality"]


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)



from sklearn.preprocessing import StandardScaler,MinMaxScaler

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)



from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()


knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)



from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")


k = [3,5,7,9,11,13]



for i in k:
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    y_pred = knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy * 100:.2f}%")



knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")


class KNN:
    def __init__(self, k=3):
        self.k = k
    
    def fit(self, X_train, y_train):
        self.X_train = X_train.values if isinstance(X_train, pd.DataFrame) else X_train
        self.y_train = y_train.values if isinstance(y_train, pd.Series) else y_train
    
    def predict(self, X_test):
        X_test = X_test.values if isinstance(X_test, pd.DataFrame) else X_test
        predictions = [self._predict(x) for x in X_test]
        return np.array(predictions)
    
    def _predict(self, x):
        distances = [np.sqrt(np.sum((x - x_train) ** 2)) for x_train in self.X_train]
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        most_common = np.bincount(k_nearest_labels).argmax()
        return most_common


knn = KNN(k=3)
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")





