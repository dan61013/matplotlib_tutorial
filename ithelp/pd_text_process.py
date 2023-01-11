import pandas as pd

def sample01():
    
    df = pd.read_csv("./file/List of most-subscribed YouTube channels.csv", index_col="Rank")
    
    # 先用astype()將資料轉成category，以節省大小
    df["Name"] = df["Name"].astype("category")
    print(df.head(10))
    # print(df["Name"].title())  # Series 沒有title屬性
    print(df["Name"].str.title())  # 輸出所有的name title
    print(type(df["Name"].str))  # pandas StringMethods
    print(df["Name"].str.lower().head(3))  # 全小寫
    print(df["Name"].str.upper().head(3))  # 全大小
    print(df["Name"].str.len().head(3))  # 全部name的長度
    # title() -> 轉換成單字首字大寫

    # replace
    df["Name"] = df["Name"].str.replace("India", "Taiwan")  # Rank: 3, Name
    print(df.head())

def sample02():
    """
    使用contains, startswitch, endswitch，
    製作mask以篩選資料
    """
    
    df = pd.read_csv("./file/List of most-subscribed YouTube channels.csv", index_col="Rank")
    df["Name"] = df["Name"].astype("category")
    print(df.tail(3))
    
    # 取出channel中的Yes
    # df["Brand channel"].str.lower()  # 先將數據轉成小寫
    mask01 = df["Brand channel"].str.contains("Ye")  # 找出包含ye的字串
    print(df[mask01].head())  # 用mask方式可以filter
    
    # startswith
    mask02 = df["Country"].str.lower().str.startswith(" south")
    print(df[mask02].head())
    
    # endswitch
    mask03 = df["Country"].str.lower().str.endswith("states")
    print(df[mask03].head())

def sample03():
    """
    Split Strings by Characters
    切割字元
    """
    
    # dropna, how='all'，會刪除全部的Na資料
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html
    df = pd.read_csv("./file/List of most-subscribed YouTube channels.csv", index_col="Rank").dropna(how='all')
    print("Hello my name is Dan".split(' '))  # python
    
    # 每一個Name會依照空格切割
    print(df["Name"].str.split(' ').head())
    # 取出每一筆切割好的資料的第0項
    print(df["Name"].str.split(' ').str.get(0).head())
    
    
def main():
    
    # sample01()
    
    # sample02()
    
    sample03()

if __name__ == "__main__":
    main()