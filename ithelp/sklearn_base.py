from sklearn import tree

"""
標籤: 0=橘子、1=蘋果
表面: 0=平滑、1=皺
"""

def main():
    
    features = [[150, 1], [170, 1], [130, 0], [140, 0], [155, 1]]
    labels = [0, 0, 1, 1, 0]
    
    # Decision TreeClassifier
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features, labels)
    
    want_predict = clf.predict([[120, 1]])
    if want_predict == [1]:
        print("This is an apple.")
    elif want_predict == [0]:
        print("This is an orange.")

if __name__ == "__main__":
    main()