import matplotlib.pyplot as plt

def sample01():
    
    # pie chart 圓餅圖
    labels = 'A', 'B', 'C', 'D', 'E', 'F'
    size = [33, 12, 25, 18, 62, 51]
    # 圓餅圖用plt.pie()
    # 參考: https://www.runoob.com/matplotlib/matplotlib-pie.html
    # plt.pie(size, labels= labels, autopct='%1.1f%%')  # autopct:設定百分比
    # plt.axis('equal')  # 使圓餅圖比例相等
    # plt.show()
    
    # Separated, pie(explode)
    # 負值為範圍縮小，正值為取出的距離，-1(剛好消失，但圖標會顯示)
    separated = (.2, -1, 0, 0, 0, 0)
    # 分割
    plt.pie(size, labels= labels, autopct='%1.1f%%', explode=separated)
    plt.axis('equal')
    plt.show()

def main():
    
    sample01()

if __name__ == "__main__":
    main()