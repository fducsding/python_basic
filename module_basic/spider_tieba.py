import urllib.request
import re


class Spider:
    def __init__(self):
        #初始化起始页
        self.page=2
        #爬取开关，如果为True继续爬取
        self.switch=True


    def loadPage(self):
        #下载页面
        url="https://www.neihanba.com/dz/list_"+str(self.page)+".html"
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
        request=urllib.request.Request(url,headers=headers)
        response=urllib.request.urlopen(request)
        #获取每页的html源码
        html=response.read()
        html=html.decode("gbk")  #这个网页得用gbk解码

        # print(html)

        #创建一个正则表达式对象
        pattern=re.compile(r'<div class="f18 mb20">(.*?)</div>',re.S)

        #将正则匹配对象应用到html字符串源码里
        content_list=pattern.findall(html)

        self.dealPage(content_list)




    def dealPage(self,content_list):
        #处理每页的段子
        for item in content_list:
            item=item.replace("<p>","").replace("</p>","").replace("<br>","")
            # print(item)
            self.writePage(item)







    def writePage(self,item):
        #把每条段子逐个写入文件里
        # with open("duan.txt","a",encoding="utf-8") as f:
        f = open("duan.txt","a",encoding="utf-8")
        f.write(item)


    def startWork(self):
        #控制爬虫进行
        while self.switch:
            command=input("如果继续爬取，请按回车（退出请输入quit）")
            if command == "quit":
                self.switch=False
            self.loadPage()
            self.page+=1





if __name__ == "__main__":
    duanziSpider=Spider()
    # duanziSpider.loadPage()
    duanziSpider.startWork()



