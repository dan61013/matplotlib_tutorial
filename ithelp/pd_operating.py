import pandas as pd

def operating01():
    
    # 讀取csv檔
    df = pd.read_csv('./file/List of best-selling video games.csv')
    print(df.head(3))  # 可以顯示5筆資料，default: 5
    print(df.tail())  # 顯示最後5筆資料
    
    # 查看資料內容&大小
    print(df.info())
    print(df.shape)
    
    # 選擇資料
    print(df['Title'])
    print(df['Title'][0:5])
    # 多項選擇
    print(df[['Title', 'Sales']])
    
    # 新增資料
    df.insert(3, column='Test', value='Test01')
    print(df[['Test', 'Title']])

def operating02():
    df = pd.read_csv('./file/List of best-selling video games.csv')
    
    # 刪除NaN的資料
    print(df.dropna()['Sales'])  # NaN資料會直接display
    print(df.fillna(0)['Sales'])  # Nan資料會直接覆蓋成0
    
    # sort 資料排序
    df = df.fillna(0)
    df = df.sort_values("Title")
    df = df.sort_values("Title", ascending=False)  # 倒序
    print(df)

def main():
    
    # operating01()
    
    operating02()

if __name__ == "__main__":
    main()