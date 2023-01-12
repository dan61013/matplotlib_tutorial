import numpy as np

def sample01():
    
    a = np.array([1, 2, 3, 4])
    b = np.array([2, 2, 2, 2])
    # 相乘
    print(a * b)
    
    # 廣播: 用array乘上一個係數，numpy會自動擴展成一樣長度的array
    c = 2
    print(a * c)
    
    # 進階
    x = np.arange(4)
    print(x)
    x2 = x.reshape(4, 1)
    print(x2)
    y = np.ones(5)
    print(y)
    print(x2 + y)
    
    # reshape
    s = np.arange(6)
    s = s.reshape((3, 2))
    print(s)

def sample02():
    
    # Numpy.T -> transpose
    x = np.zeros((10, 2))
    print(x)  # 10*2 values=0, matrix
    y = x.T
    print(y)  # 2*10, 旋轉矩陣
    
    x1 = np.array([[3, 4], [5, 6]])
    y1 = x1.T
    print(y1)
    
    # ndarray.base
    y = np.array([1, 2, 3, 4])
    print(y.base)
    # example
    x = np.arange(4)
    x2 = x.reshape(4, 1)
    y = np.ones(5)
    print(x2.base)  # base is x

def main():
    
    # sample01()
    
    sample02()

if __name__ == "__main__":
    main()