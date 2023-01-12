import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def sample01():
    
    data01 = {'name':['a', 'b', 'c', 'd', 'e'],
              'january':[122, 121, 130, 150, 171],
              'feburary':[101, 111, 131, 143, 152],
              'march':[61, 22, 30, 50, 27]}
    df = pd.DataFrame(data01, columns=['name', 'january', 'feburary', 'march'])
    df['total'] = df['january'] + df['feburary'] + df['march']
    # print(df)
    # print(df['total'])
    # 定義顏色
    colors = [(1, .4, .4), (1, .6, 1), (.5, .3, 1), (.7, .7, .2), (.6, .2, .6)]
    plt.pie(df['total'], labels=df['name'], colors=colors, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

    # bar chart 長條圖
    # 使用numpy建資料
    col_count = 3
    scores01 = (533, 571, 567)
    scores02 = (421, 323, 476)
    scores03 = (357, 565, 501)
    scores04 = (456, 313, 506)

def main():
    
    sample01()

if __name__ == "__main__":
    main()