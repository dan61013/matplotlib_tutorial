import pandas as pd
import numpy as np

def sample_get_series_value():
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

def sample_set_index():
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

def sample_loc():
    
    # 用index取出資料(by loc)
    df = pd.read_csv("./file/Coffee_domestic_consumption.csv", index_col="Country")
    print(df.loc["Brazil"])
    print(df.loc[["Brazil", "Malawi"]])  # 一次取出多筆資料
    
    # iloc是用index位置來取出資料
    df = pd.read_csv("./file/Coffee_domestic_consumption.csv")
    print(df.iloc[15])
    # 一次提出多筆資料
    print(df.iloc[0:2])  # 取出0~2
    print(df.iloc[[0, 4]])  # 取出0 & 4
    
    # loc & iloc 進階使用
    df = pd.read_csv("./file/Coffee_domestic_consumption.csv", index_col="Country")
    print(df.loc["Burundi", "Coffee type"])  # 取出Burundi的Coffee type

def sample_rename():
    
    # Change column name
    df = pd.read_csv("./file/Coffee_domestic_consumption.csv", index_col="Country")
    df.rename(columns={"Coffee type":"Type", "1990/91":"test001"}, inplace=True)
    print(df.head(2))
    
    # Change index name
    df.rename(index={"Angola":"New Taipei City", "Bolivia (Plurinational State of)":"None"}, inplace=True)
    print(df.head(2))

def sample_drop():
    
    # drop刪除資料
    df = pd.read_csv("./file/Coffee_domestic_consumption.csv", index_col="Country")
    print(df.drop(labels=["1990/91", "1991/92"], axis="columns")[0:2])
    # axis=0(row), 1(column)
    print(df.drop(labels=["1990/91", "1991/92"], axis=1)[0:2])

def main():
    
    # sample_get_series_value()
    
    # sample_set_index()
    
    # sample_loc()
    
    # sample_rename()
    
    sample_drop()

if __name__ == "__main__":
    main()