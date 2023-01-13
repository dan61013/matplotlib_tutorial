from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# KNN分類演算法
# K Nearest Neighbor
# 鳶尾花資料集做測試
def main():
    
    iris = datasets.load_iris()
    iris_data = iris.data
    iris_label = iris.target
    
    # print(iris_data[0:3])
    
    # 一般來說資料會分成: 訓練及測試資料
    # 使用train_test_split()
    train_data, test_data, train_label, test_label = train_test_split(iris_data, iris_label, test_size=0.2)
    knn = KNeighborsClassifier()
    knn.fit(train_data, train_label)
    
    print(knn.predict(test_data))
    print(test_label)

if __name__ == "__main__":
    main()