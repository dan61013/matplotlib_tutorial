import pandas as pd

def sample_series01():
    """
    Series是一個類似Array的物件，可包含Array的資料
    """
    
    # my_obj -> 不包含index設定
    my_obj = pd.Series([4, 7, 10, -3, 0])
    print(my_obj)
    print(my_obj.values, type(my_obj.values))
    print(my_obj.index)
    
    # my_obj2 -> 包含index設定
    my_obj02 = pd.Series([8, 9, 10, 11, -5], index=['a', 'b', 'c', 'd', 'e'])
    print(my_obj02, type(my_obj02))
    print(f"my_obj02['e']: {my_obj02['e']}")
    print(True if ('z' in my_obj02) else False)
    
    # dict 轉成 Series
    dict_data = {'name':'Dan', 'birthday':'1995-1-1', 'luckynumber':7}
    my_obj03 = pd.Series(dict_data)
    print(my_obj03)
    
    # boolean to Series
    registration = [True, False, False, True, False]
    registration = pd.Series(registration)
    print(registration)

def sample_dataframe01():
    """
    與使用Excel表格類似，是一個2維的數據有index and columns，\n
    可以透過index and columns尋找我們需要的一筆資料
    """
    
    # 基本形式
    data = {
        'name': ['Dan', 'Ken', 'Ivy', 'May', 'Kevin'],
        'year': [1990, 1992, 1994, 1996, 1998],
        'month': [1, 1, 3, 7, 5],
        'day': [11, 21, 3, 5, 3]
    }
    
    myframe = pd.DataFrame(data)
    print(myframe)
    
    # 更改columns順序, day在month之前
    myframe2 = pd.DataFrame(data, columns=['name', 'year', 'day', 'month'])
    print(myframe2)
    
    # 新增column
    myframe3 = pd.DataFrame(data, columns=['name', 'year', 'day', 'month', 'code'])
    # 沒有資料會顯示 NaN
    print(myframe3)
    
    # 建立資料，並提供給myframe3
    code = ['3', '1', '10', '55', '2']
    code = pd.Series(code)
    myframe3['code'] = code
    print(myframe3)

def main():
    
    # 查看pandas的版本
    # print(pd.__version__)
    
    # sample_series01()
    
    sample_dataframe01()

if __name__ == "__main__":
    main()