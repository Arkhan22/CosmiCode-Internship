# -*- coding: utf-8 -*-
"""week 3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cTjF5Wt0ee5FH5REFnnA8BmjDLfvtis8
"""

# WEEK 3: KMeans, Elbow, Hierarchical Clustering

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage

# Load data
iris = load_iris(as_frame=True)
df = iris.frame.drop('target', axis=1)

# KMeans
wcss = []
for k in range(1, 10):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df)
    wcss.append(kmeans.inertia_)

# Plot elbow method
plt.plot(range(1, 10), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Clusters")
plt.ylabel("WCSS")
plt.show()

# Final Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(df)

# Hierarchical Clustering
linked = linkage(df.drop('Cluster', axis=1), method='ward')
dendrogram(linked)
plt.title("Dendrogram")
plt.show()

# Print difference
print("Supervised = With labels (target)\nUnsupervised = Without labels")