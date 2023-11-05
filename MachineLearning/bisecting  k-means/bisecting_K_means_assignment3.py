from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1, 2], [2, 1], [1, 1.5], [1.5, 1],
               [10, 2], [10, 4], [10, 0], [10, 1],
               [1, 10], [2, 11], [1.5, 9], [1, 10.5],
               [10.5, 9], [9, 9.5], [9.5, 9], [10, 10]])

K = 4
current_clusters = 1
# Initialize a list of clusters
clusters = [X]

while current_clusters != K:
    kmeans = KMeans(n_clusters=2, n_init=10).fit(X)
    current_clusters += 1
    cluster_centers = kmeans.cluster_centers_
    labels = kmeans.labels_

    # Calculate SSE for each cluster
    sse = [0] * 2
    for i in range(2):
        cluster_points = X[labels == i]
        sse[i] = np.sum((cluster_points - cluster_centers[i]) ** 2)

    # Find the cluster with the higher SSE
    if sse[0] > sse[1]:
        high_sse_cluster = 0
    else:
        high_sse_cluster = 1

    # Split the cluster with the higher SSE into two sub-clusters
    sub_clusters = KMeans(n_clusters=2, n_init=10).fit(X[labels == high_sse_cluster]).cluster_centers_

    # Remove the original cluster and add the sub-clusters to the list of clusters
    clusters.pop()
    clusters.extend(sub_clusters)

# Convert the list of clusters to a numpy array for plotting
clusters = np.array(clusters)

plt.figure(figsize=(8, 6))
for i in range(K):
    cluster_points = X[labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1])

# Plot the centroids with a red 'X'
plt.scatter(clusters[:, 0], clusters[:, 1], c='red', marker='*', s=150)
plt.title("Bisecting K-means with Clusters and Centroids")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()