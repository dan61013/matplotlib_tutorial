from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
    <body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

def sample01():
    
    # 解析
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    # print(soup.prettify())  # prettify 美化
    
    print(soup.title)  # <title>The Dormouse's story</title>
    print(soup.head)  # <head><title>The Dormouse's story</title></head>
    print(soup.head.title)  # 同title
    print(soup.title.string)  # The Dormouse's story
    print(soup.findAll('p'))  # 找出所有標籤
    
    # 找出所有連結，找不到會回傳None
    for link in soup.find_all('a'):
        print(link.get('href'))
        
    # 找出所有標籤內的class name
    for class_name in soup.find_all('p'):
        print(class_name.get('class')[0])
    
    # find(id)
    print(soup.find(id="link3"))
    
    # 取出文字
    print(soup.get_text())

def main():
    
    sample01()

if __name__ == "__main__":
    main()