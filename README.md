# Matplotlib

## 參考資源
1. [使用Python進行資料分析](https://ithelp.ithome.com.tw/articles/10196239)
2. csv file from [Top 50 Video Games](https://www.kaggle.com/datasets/devrimtuner/top-100-video-games?resource=download)
---

## Main Package
1. Pandas
   
   基於numpy的package，可輕易的處理數據，pandas有2種特有的資料結構
    * DataFrame
    * Series

2. Numpy
   
   Numpy主要可以提供建立多維數據及矩陣運算，pandas算是以其為基礎的延伸套件

3. Matplotlib
   
   將處理好的數據，轉換成數據可視化的圖形

4. Scipy
   
   以Numpy為基礎做科學、工程等運算處理的package，包含統計、優化、整合、線性代數、傅立葉轉換圖像等高階的科學運算

---

## Pandas Notes

### Series
1. 主要建立類似array(list)資料，例如: [1, 3, 5, 7, 5]
2. Series可以用values, index or [] 取出指定的數值
   ```python
   import pandas as pd
   data = pd.Series([1, 2, 3])
   print(data[1])
   print(data.index)
   print(data.values)
   ```
3. 可以設定index欄位的數值
   ```python
   import pandas as pd
   pd.Series([1, 2, 3], index=['a', 'b', 'c'])
   ```
4. 