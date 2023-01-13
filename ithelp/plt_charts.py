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

def sample02():
    """
    bar chart 長條圖\n
    matplotlib.pyplot.bar()
    """
    
    # Scores Data
    scores_a = (533, 571, 567)
    scores_b = (421, 323, 476)
    scores_c = (357, 565, 501)
    scores_d = (456, 313, 506)
    labels = ["Math", "Reading", "Science"]
    
    x = np.arange(len(labels))  # the label locations
    bar_width = 0.2  # the width of the bars
    
    fig, ax = plt.subplots()
    
    # 定義Bar的圖形
    a = ax.bar(x, scores_a, bar_width, label='K')
    b = ax.bar(x + 0.2, scores_b, bar_width, label='C')
    c = ax.bar(x + 0.4, scores_c, bar_width, label='N')
    d = ax.bar(x + 0.6, scores_d, bar_width, label='F')
    
    ax.set_ylabel("Mean score")
    ax.set_xlabel("Subject")
    ax.set_title("Test Scores by Country")
    ax.legend()
    ax.grid(True)
    ax.set_xticks(x + .6 / 2, labels)  # 設定底下的文字
    
    ax.bar_label(a, padding=0)
    ax.bar_label(b, padding=0)
    ax.bar_label(c, padding=0)
    ax.bar_label(d, padding=0)
    
    fig.tight_layout()
    plt.show()

def sample03():
    """
    補充: plt.subplots\n
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots
    """
    
    # Create Data
    x = np.linspace(0.2 * np.pi, 400)  # 50筆資料，最大值400
    y = np.sin(x ** 2)
    
    # Create just a figure and only one subplot
    fig, ax = plt.subplots()  # Figure(640x480) AxesSubplot(0.125,0.11;0.775x0.77)
    # plt.subplots() -> (<Figure size 640x480 with 1 Axes>, <AxesSubplot: >)
    ax.plot(x, y)
    ax.set_title("Simple plot")

    # Create two subplots and unpack the output array immediately
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    # Figure(640x480) AxesSubplot(0.125,0.11;0.352273x0.77) AxesSubplot(0.547727,0.11;0.352273x0.77)
    ax1.plot(x, y)
    ax1.set_title("Sharing Y axis")
    ax2.scatter(x, y)
    
    # Create four polar axes and access them through the returned array
    fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))  # 極座標
    axs[0, 0].plot(x, y)
    axs[1, 1].scatter(x, y)
    
    plt.show()

def main():
    
    # sample01()
    
    # sample02()
    
    sample03()

if __name__ == "__main__":
    main()