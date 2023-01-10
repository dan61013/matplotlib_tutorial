# 20230110 Ithelp 問題
# https://ithelp.ithome.com.tw/questions/10211669
import pandas as pd

def main():
    
    a = pd.Series([1,1,0,1,1,1,0,0,0,1,1,1])
    b = pd.Series([0,0,-1,0,0,0,-1,-1,-1,0,0,0])
    c = pd.DataFrame({'a':a, 'b':b})
    
    lst = []
    
    for i in range(len(c)):
        if (c.at[i, 'a'], c.at[i, 'b']) not in lst:
            lst.append((c.at[i, 'a'], c.at[i, 'b']))

    print(lst)

if __name__ == "__main__":
    main()