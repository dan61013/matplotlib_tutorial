import matplotlib.pyplot as plt
import numpy as np

def sample_case01():
    
    # Create data
    years = [1000,1500,1600,1700,1750,1800,1850,
        1900,1950,1960,1965,1970,1975,1980,
        1985,1990,1995,2000,2005,
        2010,2015]
    
    pops = [200,400,458,580,662,791,1000,
        1262,1650,2525,2758,3018,3322,3682,
        4061,4440,4853,5310,6520,
        6930,7349]
    
    # plt.plot() 將資料放到函數中
    plt.plot(years, pops, color=(255/255, 100/255, 100/255))
    plt.show()

def sample_case02():
    
    # Data
    years = [1950,1960,1965,1970,1975,1980,
        1985,1990,1995,2000,2005,
        2010,2015]
    
    pops = [2.5,2.7,3,3.3,3.6,4.0,
            4.4,4.8,5.3,6.1,6.5,6.9,7.3]
    
    # Multilines
    deaths = [1.2,1.7,1.8,2.2,2.5,2.7,2.9,3,3.1,3.2,3.5,3.6,4]
    
    plt.title("Population Growth")  # title
    plt.ylabel("Population in billions")  # y label
    plt.xlabel("Population growth by year")  # x label
    # lines = plt.plot(years, pops, years, deaths)
    plt.plot(years, pops)
    plt.plot(years, deaths, '--')  # Multilines
    plt.show()

def sample_case03():
    
    # Configure graph
    years = [1950,1960,1965,1970,1975,1980,
        1985,1990,1995,2000,2005,
        2010,2015]
    
    pops = [2.5,2.7,3,3.3,3.6,4.0,
            4.4,4.8,5.3,6.1,6.5,6.9,7.3]
    
    deaths = [1.2,1.7,1.8,2.2,2.5,2.7,2.9,3,3.1,3.2,3.5,3.6,4]
    
    lines = plt.plot(years, pops, years, deaths)
    plt.setp(lines, marker="o")
    plt.grid(True)
    plt.show()

def sample_case04():
    """
    matplotlib with numpy
    """
    
    x = np.arange(0, 1.0, 0.01)
    y1 = np.sin(4*np.pi*x)
    y2 = np.sin(2*np.pi*x)
    lines = plt.plot(x, y1, x, y2)
    plt.setp(lines, linestyle='--')
    plt.show()    

def main():
    
    # sample_case01()
    
    # sample_case02()
    
    # sample_case03()
    
    sample_case04()

if __name__ == "__main__":
    main()