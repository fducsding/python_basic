import urllib.request


#获取一个get请求
# response =urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8")) #对获取到的网页解码


#获取一个post请求
# import urllib.parse    #解码
# data =bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))


#超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out")



import  urllib.parse
url = "http://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}

# data = bytes(urllib.parse.urlencode({"name11":"eric"}),encoding="utf-8")

req =urllib.request.Request(url=url,headers=headers)#进行封装

response=urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
