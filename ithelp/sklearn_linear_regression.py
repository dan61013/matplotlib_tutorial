from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import datasets

def sample01():
    
    # 參數依序為: 樣品數量、特徵值、應用於輸出時，高斯噪聲的標準差
    x, y = datasets.make_regression(n_samples=200, n_features=1, n_targets=1, noise=10)
    plt.scatter(x, y, linewidths=0.1)
    plt.show()

def sample02():
    
    x, y = datasets.make_regression(n_samples=200, n_features=1, n_targets=1, noise=10)
    model = LinearRegression()
    model.fit(x, y)  # 放進模型內訓練
    predict = model.predict(x[:200, :])
    
    plt.plot(x, predict, c='red')
    plt.scatter(x, y)
    plt.show()

def main():
    
    # sample01()
    
    sample02()

if __name__ == "__main__":
    main()