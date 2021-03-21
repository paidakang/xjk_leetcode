import urllib.request,urllib.error
import bs4
import re
import sqlite3
import xlwt
from bs4 import BeautifulSoup
#导包
#分三步：1.爬取  2.解析  3.保存
def main():
    URL = "https://movie.douban.com/top250?start="
    datalist = getdata(URL)
    # savepath = ".\\豆瓣电影Top250.xls"
    #savedata(savepath)
findlink = re.compile(r'<a href="(.*?)">')
findname = re.compile(r'<span class="title">(.*)</span>')
def getdata(URL):
    datalist=[]
    for i in range(0,10):
        url = URL + str(i*25)
        html = askURL(url)
        #逐一解析
        soup = BeautifulSoup(html,"html.parser")
        #print(soup)
        for item in soup.find_all('div',class_="item"):
            data = []
            item = str(item)
            link = re.findall(findlink,item)[0]
            print(link)                          #查找符合要求的字符串形成列表
            name = re.findall(findname,item)[0]
            print(name)
    return datalist
def askURL(URL):
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54"}
    request = urllib.request.Request(URL,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
        
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print("fuck")
        if hasattr(e,"reason"):
            print(e.reason)
    return html
# def exmdata():


# def savedata():

if __name__ == "__main__":
    main()