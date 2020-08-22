import requests
import re
import urllib.request

url='http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1593527411960_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E5%B0%8F%E5%A7%90%E5%A7%90'
headers = {
    "referer":"http://image.baidu.com/search/",
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
img_store="E:/meizi/"

def getimg(url):
    reponse=requests.get(url,headers=headers)
    contents=reponse.content.decode("utf-8")
    # print(content)
    img_list=re.findall(r'"thumbURL":"(.*?)"',contents,re.S)
    # print(img_list)
    i=1
    for img in img_list:
        print(img)
        reponse=requests.get(img,headers=headers)
        content=reponse.content
        with open(img_store+"{}.jpg".format(i),"wb") as f:
            f.write(content)
        i+=1


getimg(url)