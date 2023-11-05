# Melinda Vigh and Raelyn Mendoza
# CS 422- Assignment 2

import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt 
import seaborn as sns

sns.set()

# Load the Iris dataset
iris = datasets.load_iris()
X, y = iris.data, iris.target


# 1a

# Get top 70% of the rows
seen_data_set = int(len(X) * 0.7)
X_seen, y_seen = X[:seen_data_set], y[:seen_data_set]

# 1b

# Split the dataset into training and testing sets (80% training - 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X_seen, y_seen, test_size=0.2, random_state=1234)

# Get test score for k = 5
clf = KNeighborsClassifier(n_neighbors=5)
clf.fit(X_train, y_train)

# Compute training and test scores
training_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)

# Print the test score
print("Test Score:", test_score)


# 2 testing the model with k ranging from 3-15

# Initialize empty lists to store scores for different k values
K = []
training = []
test = []
scores = {}

# Perform k-nearest neighbors classification for k values ranging from 3 to 15
for k in range(3, 16):
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_train, y_train)

    # Compute training and test scores
    training_score = clf.score(X_train, y_train)
    test_score = clf.score(X_test, y_test)
        
    # Store the scores in the respective lists and dictionary
    K.append(k)
    training.append(training_score)
    test.append(test_score)
    scores[k] = [training_score, test_score]

# Print the scores for each k value
for key, value in scores.items():
    print(key, ':', value)

# Plot the training scores using a strip plot
ax = sns.stripplot(x=K, y=training)
ax.set(xlabel='Values of k', ylabel='Training Score')
plt.title("Training Score vs. k Value")
plt.show()

# Plot the test scores using a strip plot
ax = sns.stripplot(x=K, y=test)
ax.set(xlabel='Values of k', ylabel='Test Score')
plt.title("Test Score vs. k Value")
plt.show()

# Plot the training and test scores using scatter plots
plt.scatter(K, training, color='r')
plt.scatter(K, test, color='g')
plt.show()

# 2 Applying the model to the bottom 30% of unseen iris database data
X_unseen, y_unseen = X[seen_data_set:], y[seen_data_set:]

# Apply the trained model to the unseen_data_set
unseen_predictions = clf.predict(X_unseen)

# Create a list to store values
list = []

# Perform K-means clustering for each K value
for k in range(3, 16):
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_seen, y_seen)
    unseen_predictions_k = clf.predict(X_unseen)
    list.append(np.sum(unseen_predictions_k == y_unseen) / len(y_unseen))
    

# Plotting the SSE values against K values
plt.plot(range(3, 16), list, marker='o')
plt.title("Elbow Plot - Unseen Data Set")
plt.xlabel("Number of Neighbors (K)")
plt.ylabel("Values")
plt.show()
