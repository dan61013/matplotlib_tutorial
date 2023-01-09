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
    
    df = pd.read_csv("./file/List of best-selling video games.csv")
    print(df)

def main():
    
    # sample_multi_index()
    
    sample_get_lv_val()

if __name__ == "__main__":
    main()