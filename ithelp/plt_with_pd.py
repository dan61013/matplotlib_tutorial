import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    
    df = pd.DataFrame(np.random.randn(100, 4), index=pd.date_range("1/1/2022", periods=100), \
        columns=list('ABCD'))
    
    df = df.cumsum()
    
    df.plot()
    
    plt.show()

if __name__ == "__main__":
    main()