import pandas as pd
import numpy as np

def sample01():
    """
    按照Coulmn的資料，做Boolean判斷，\n
    並篩選出對應的row數據
    """
    
    # series取值
    series_obj = pd.Series(range(10), index=['a', 'a', 'b', 'b', 
                                             'b', 'c', 'c', 'c', 'd', 'd'])
    print(series_obj['c'])
    
    # DataFrame取值，np.random
    df = pd.DataFrame(np.random.randn(4, 2), index=['a', 'a', 'b', 'b'])
    print(df)
    print(df.loc['b'])
    
    # filter 基本篩選資料
    df = pd.read_csv("./file/Coffee_domestic_consumption.csv")
    filter = (df["Coffee type"] == "Arabica")
    print(filter)
    print(df[filter])
    
    # filter 進階篩選資料
    df = pd.read_csv("./file/List of best-selling video games.csv")
    mask1 = df["Rank"] >= 10
    mask2 = df["Platform(s)"] == "Multi-platform"
    print(df[(mask1 & mask2)])  # and
    print(df[(mask1 | mask2)])  # or
    
    # isin()
    mask = df["Publisher(s)[a]"].isin(["Nintendo", "Sega"])
    print(df[mask])
    
    # isnull & notnull
    mask3 = df["Sales"].isnull()
    mask4 = df["Sales"].notnull()
    print(mask3, mask4)
    # between
    mask5 = df["Rank"].between(10, 20)
    print(df[mask5])

def sample02():
    """
    設定index欄位
    """
    
    # 沒有設定index
    df = pd.read_csv("./file/Coffee_domestic_consumption.csv")
    print(df.head())
    
    # 設定index
    df = pd.read_csv("./file/Coffee_domestic_consumption.csv", index_col="Country")  # 第一種方式
    print(df.head())
    # 查看index欄位資料
    print(df.index)
    # set_index
    df = pd.read_csv("./file/Coffee_domestic_consumption.csv")
    df.set_index("Country", inplace=True)  # 第二種方式
    print(df.head(2))
    
    # reset index column
    df.reset_index(inplace=True)
    print(df.head(2))

def sample3():
    
    df = pd.read_csv("./file/Coffee_domestic_consumption.csv", index_col="Country")
    

def main():
    
    # sample01()
    
    sample02()

if __name__ == "__main__":
    main()