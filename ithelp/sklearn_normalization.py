from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.datasets._samples_generator import make_classification
from sklearn.svm import SVC
import numpy as np
import matplotlib.pyplot as plt

def sample01():
    
    x, y = make_classification(n_samples=300, n_features=2, n_redundant=0, n_informative=2, \
        random_state=3, scale=100, n_clusters_per_class=1)
    plt.scatter(x[:,0], x[:, -1], c=y)
    plt.show()

def sample02():
    
    # SVC分類法進行訓練
    x, y = make_classification(n_samples=300, n_features=2, n_redundant=0, n_informative=2, \
         random_state=3, scale=100, n_clusters_per_class=1)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    clf = SVC()
    clf.fit(x_train, y_train)
    print(clf.score(x_test, y_test))

def main():
    
    # sample01()
    
    sample02()

if __name__ == "__main__":
    main()