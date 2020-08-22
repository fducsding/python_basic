import urllib.request
import re
from bs4 import BeautifulSoup

url="https://www.qiushibaike.com/text/page/2/"
head={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
request=urllib.request.Request(url,headers=head)
response=urllib.request.urlopen(request)
html=response.read().decode("utf-8")
#print(html)

bs=BeautifulSoup(html,"html.parser")
datalist=[]
contents=[]
find_author=re.compile(r'<h2>\n(.*?)\n</h2>')  #要忽略换行
find_content=re.compile(r'<span>(.*?)</span>',re.S)
for item in bs.find_all("div",class_="article block untagged mb15 typs_hot"):
    # print(item)
    data=[]
    item=str(item)
    #print(item)
    author=re.findall(find_author,item)
    content=re.findall(find_content,item)
    content = "".join(content).strip()
    data.append(author)
    data.append(content)
    datalist.append(data)

duanzi={"author":author,"content":contents}
print(datalist)
# print(duanzi)


# data=[]
# soup=str(soup)
# find_author=re.compile(r'<h2>(.*?)</h2>')
# author=re.findall(find_author,soup)
#data.append(author)
# print(author)