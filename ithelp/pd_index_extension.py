import pandas as pd

def sample_multi_index():
    
    df = pd.read_csv("./file/List of most-subscribed YouTube channels.csv")
    print(df.head(2))
    
    # set_index()，可以設定多個index欄位
    df.set_index(keys=["Category", "Country"], inplace=True)
    print(df)
    print(df.index.names)  # 顯示目前的index欄位名稱
    print(type(df.index))  # MultiIndex

def sample_get_lv_val():
    
    df = pd.read_csv("./file/List of best-selling video games.csv", index_col=["Rank", "Title"])
    print(type(df.index))
    print(df.index.names)
    df.sort_index(inplace=True)
    print(df.head())
    
    # 取得index(0)的資料
    print(df.index.get_level_values(0))  # 用位置取得資料
    print(df.index.get_level_values("Title"))  # 也可以用名稱取得資料
    
    # Multi Set Names
    df.index.set_names(["No.", "Names"], inplace=True)
    print(df)

def main():
    
    # sample_multi_index()
    
    sample_get_lv_val()

if __name__ == "__main__":
    main()