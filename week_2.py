# -*- coding: utf-8 -*-
"""week 2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1x1qNhDWV6U4cyznnNSaVanridIlYFgZr
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load dataset
iris = load_iris(as_frame=True)
df = iris.frame

# AI vs ML vs DL
print("AI: Any machine mimicking human intelligence.")
print("ML: Algorithms that learn from data.")
print("DL: Neural network-based learning.")

# Linear Regression
X = df[['petal length (cm)']]
y = df['sepal length (cm)']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr = LinearRegression()
lr.fit(X_train, y_train)
print("Linear Regression Score:", lr.score(X_test, y_test))

# Decision Tree Classifier
X = df.drop(columns='target')
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average="macro"))
print("Recall:", recall_score(y_test, y_pred, average="macro"))
print("F1 Score:", f1_score(y_test, y_pred, average="macro"))