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
    
def main():
    
    sample01()

if __name__ == "__main__":
    main()