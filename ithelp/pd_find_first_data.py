# 20230110 Ithelp 問題
# https://ithelp.ithome.com.tw/questions/10211669
import pandas as pd

def main():
    
    a = pd.Series([1,1,0,1,1,1,0,0,0,1,1,1])
    b = pd.Series([0,0,-1,0,0,0,-1,-1,-1,0,0,0])
    c = pd.DataFrame({'a':a, 'b':b})
    
    lst = []
    length = (len(c) - 1)
    
    i = 0
    while i <= length:
        # for迴圈尋找下一個相異值(中斷點)
        for j in range(1, (len(c) - i)):
            if ((c.at[i, 'a'], c.at[i, 'b']) != (c.at[(i + j), 'a'], c.at[(i + j), 'b'])):
                break
        # 把第一個重複出現的數值加入list
        lst.append((c.at[i, 'a'], c.at[i, 'b']))
        i = i + j + 1  # 更改起始點
    else:
        # 因為最後一連串的數據不會找到下一個中斷點，所以直接加入最後一筆不重複的數值
        lst.append((c.at[length, 'a'], c.at[length, 'b']))
    
    print(lst)

if __name__ == "__main__":
    main()