import numpy as np

def sample01():
    """
    npy -> np.array儲存的檔案格式\n
    npz -> np.array[a] and [b]，兩個array合併的儲存格式\n
    npz可以用variable[index]取得對應的資料
    """
    
    # Binary Format
    x = np.arange(10)
    # np.save('./ithelp/np_files/array_01', x)  # save as npy file
    
    # load npy file
    print(np.load("./ithelp/np_files/array_01.npy"))

    data_01 = [1, 2, 3, 4, 5, 6]
    data_02 = [7, 8, 9, 10, 11, 12]
    # np.savez("./ithelp/np_files/archive_01", a=data_01, b=data_02)  # save as npz file
    my_archive = np.load("./ithelp/np_files/archive_01.npz")
    print(my_archive['a'])
    print(my_archive['b'])

def sample02():
    
    # loadtxt() or genfromtxt讀取txt檔案
    my_arr = np.loadtxt("./ithelp/np_files/array_02.txt", delimiter=',')  # 分隔符號','
    print(my_arr)
    # save txt
    np.savetxt("./ithelp/np_files/array_03.txt", my_arr)

def main():
    
    # sample01()

    sample02()

if __name__ == "__main__":
    main()