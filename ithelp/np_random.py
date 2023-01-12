import numpy as np

def sample01():
    """
    np.random建立隨機資料
    """
    
    # randn
    print(np.random.randn())  # 隨機標準數
    print(np.random.randn(2, 4) + 1.32426)  # 2*4的矩陣，再加上1.32426
    
    # randint
    print(np.random.randint(4, size=10))  # range<4, size=10
    print(np.random.randint(low=4, high=100, size=10))  # low, high設定上下限

def sample02():
    """
    Methods 數學運算
    """
    
    x = np.random.randn(5, 4)
    print(x)
    print(f"array:x 的平均值: {x.mean()}")
    print(f"array:x 的加總值: {x.sum()}")
    print(f"array:x 的最大值: {x.max()}")
    print(f"array:x 的最小值: {x.min()}")
    
    # cumsum() -> 回傳累積數值 (累加)
    x = np.array([[2, 3, 4], [5, 6, 7]])
    print(x.cumsum())  # [ 2  5  9 14 20 27]
    
    # std 標準差
    x = np.array([[9, 2], [3, 11]])
    print(f"array:x 的標準差: {x.std()}")

def main():
    
    # sample01()
    
    sample02()

if __name__ == "__main__":
    main()