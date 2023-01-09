# 參考資料: https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
import pandas as pd
import numpy as np

def sample_groupby_base():
    
    df = pd.read_csv("./file/List of most-subscribed YouTube channels.csv", index_col="Rank")
    # 使用groupby分組
    sectors = df.groupby("Category")
    print(type(sectors))
    print(sectors.size())
    print(sectors.groups)
    
    # 取得資料
    print(sectors.get_group("Music").head())

def sample_groupby_cal():
    
    df = pd.DataFrame({
        'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
        'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
        'C': np.random.randn(8),
        'D': np.random.randn(8)
    })
    
    print(df)
    
    # 計算分組總和
    print(df.groupby('A').sum())  # 計算單組總和
    print(df.groupby(['A', 'B']).sum())  # 計算兩組總和

def main():
    
    # sample_groupby_base()
    
    sample_groupby_cal()

if __name__ == "__main__":
    main()