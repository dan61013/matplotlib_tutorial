# Matplotlib

## 參考資源
1. [使用Python進行資料分析](https://ithelp.ithome.com.tw/articles/10196239)
2. [Top 50 Video Games](https://www.kaggle.com/datasets/devrimtuner/top-100-video-games?resource=download)
3. [Coffee dataset](https://www.kaggle.com/datasets/michals22/coffee-dataset)
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

## Matplotlib

### Matplotlib.pyplot.pie()
**圓餅圖**

* autopct: 設定百分比顯示格式
  *  %d%%: 整數百分比
  *  %0.1f: 一位小數
  *  %0.1f%%: 一位小數百分比
  *  %0.2f%%: 兩位小數百分比

---

## Bokeh

### 參考資料:
1. [General Visual Properities](https://docs.bokeh.org/en/latest/docs/user_guide/styling/visuals.html#ug-styling-line-properties)

## Machine Learning

### Intro

* 是實現人工智慧的一個途徑
* 涉及機率論、統計學、逼近論、凸分析、計算複雜性理論等多門學科

### 機器學習的類型
* 監督式學習 Supervised Learning
  * 提供Data以及答案
  * 讓機器學習分辨
  * 後續可以透過給新的Data得到答案
* 非監督式學習 Unsupervised Learning
  * 提供Data，但沒有答案
  * 讓機器自己去學習分辨答案
* 半監督式學習 Semi-Supervised Learning
  * 提供Data
  * 在Data中取一定數量，並提供答案
  * 剩餘的數量由機器自行學習判斷
* 增強式學習 Reinforcement Learning
  * 觀察到目前的狀態
  * 執行動作
  * 收到報酬與觀察到新的狀態
  * 重複以上動作N次，直到某個終止時間

### 機器學習的名詞

1. 特徵 Features
2. 標籤 Labels