from bokeh.plotting import figure, show

def sample01():
    
    # Scatter plot 散佈圖 定義繪圖板高寬
    p = figure(plot_width=500, plot_height=500)
    x = [1,2,3,4,5,6,7,8,9,10,11]
    y = [6,3,7,2,4,6,1,2,3,5,6]
    p.circle(x, y, size=20, color='gray', alpha=0.6)
    
    show(p)

def sample02():
    
    # Single Lines
    p = figure(width=500, height=500)
    x = [1,2,3,4,5,6,7,8,9,10,11]
    y = [6,3,4,2,5,2,5,1,3,5,4]
    p.line(x, y, line_width=3)
    
    show(p)

def sample03():
    
    # Multiple Lines
    p = figure(width=500, height=500)
    x1 = [1, 2, 3]
    x2 = [2, 3, 4, 5, 6]
    y1 = [3, 2, 5]
    y2 = [3, 2, 4, 1, 3]
    p.multi_line([x1, x2], [y1, y2], color=["firebrick", "navy"], alpha=[0.8, 0.3], line_width=5)
    
    show(p)

def sample04():
    
    # Bar
    p = figure(width=500, height=500)
    p.vbar(x=[1, 2, 3, 4], width=0.5, bottom=0, top=[1.2, 2.5, 3.7, 2.9], color="black", alpha=0.4)
    
    show(p)

def sample05():
    
    # Multiple Patches
    p = figure(width=500, height=500)
    x1 = [1, 4, 5, 2]
    x2 = [3, 4, 5, 6]
    x3 = [1,3,2]
    y1 = [2, 3, 5, 6]
    y2 = [4, 7, 7, 5]
    y3 = [7,8,5.5]
    p.patches([x1, x2, x3], [y1, y2, y3], color=["black", "navy", "firebrick"], \
        alpha=[0.2, 0.2, 0.3], line_width=2)
    
    show(p)

def main():
    
    # sample01()
    
    # sample02()
    
    # sample03()
    
    # sample04()
    
    sample05()

if __name__ == "__main__":
    main()