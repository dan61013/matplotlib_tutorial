import numpy as np

def sample01():
    """
    array, ndim, shape, dtype
    """
    
    data = np.array([[0.226, -0.1, 2.32], [0.132, 0.564, 0.12332]])
    print(data, type(data))
    
    # Type Provide
    print(np.array([1, 2, 3], dtype=complex))
    
    # creating ndarrays
    data01 = [1, 10.5, 3, 4.87]
    print(np.array(data01))
    data02 = [[1, 2, 3, 4, 5], [1.1, 2.2, 3.3, 4.4, 5.5]]  # 數量要一致
    arr02 = np.array(data02)
    print(arr02, np.ndim(arr02))
    print(arr02.shape, arr02.dtype)

def sample02():
    """
    arange(等於range用法), slice, 更改指定位置的數值
    """
    
    arr01 = np.arange(10)
    print(arr01)
    print(arr01[5:8])
    arr01[5:8] = 111
    print(arr01)
    
    # slice
    slice = arr01[5:8]
    slice[1] = 123
    print(arr01)

def main():
    
    # sample01()
    
    sample02()

if __name__ == "__main__":
    main()