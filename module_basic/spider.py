from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3



def main():

    baseurl = "https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist=getData(baseurl)
    #savepath="豆瓣电影.xls"
    dbpath="movie.db"
    #3.保存数据
    #saveData(datalist,savepath)
    saveData2DB(datalist,dbpath)


    # askURL("https://movie.douban.com/top250?start=")


#影片的电影链接
findLink=re.compile(r'<a href="(.*?)">')     #创建正则表达式对象，表示规则（字符串的模式）
#影片的图片链接
findImgSrc=re.compile(r'<img.*src="(.*?)"',re.S)   #re.S的意思是忽略换行
#影片片名
findTitle=re.compile(r'<span class="title">(.*?)</span>')
#影片评分
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
#找到评价人数
findJudge=re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findInq=re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)


#爬取网页
def getData(baseurl):
    datalist=[]
    for i in range(0,10):  #调用获取页面信息的函数
        url = baseurl+str(i*25)
        html = askURL(url)  #保存获取到的网页源码

        # 2.解析数据
        soup=BeautifulSoup(html,"html.parser")#将html解析形成soup这样的树形对象
        #find_all返回的是一个列表，所以可以用for循环
        for item in soup.find_all('div',class_="item"):   #查找所有的div,并且是class=item的div
            #class_这里加个下划线，因为是个类，不能混淆于class类
            # print(item)        #测试，查看电影item全部信息
            data=[]             #保存一部电影的所有信息
            item=str(item)   #因为find_all返回的是一个列表，str将其转化成字符串
            #print(item)

            link=re.findall(findLink,item)[0] #re库通过正则表达式查找指定的字符串
            data.append(link)
            imgSrc=re.findall(findImgSrc,item)[0]
            data.append(imgSrc)
            titles=re.findall(findTitle,item)
            if len(titles)==2 :
                ctitle=titles[0]
                data.append(ctitle)   #添加中国名
                otitle=titles[1].replace("/","")    #去掉无关的符号
                data.append(otitle)   #添加外国名
            else:
                data.append(titles[0])
                data.append(' ')    #留空外国名


            rating=re.findall(findRating,item)[0]
            data.append(rating)

            judgeNum=re.findall(findJudge,item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq=inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")  #留空

            bd = re.findall(findBd, item)[0]
            bd=re.sub('<br(\s+)?/>(\s+)?'," ",bd) #去掉<br/>
            bd=re.sub('/'," ",bd)
            data.append(bd.strip())

            datalist.append(data)

            #print(link)

    #print(datalist)


    return datalist



#得到指定一个URL的网页的内容
def askURL(url):

    #用户代理告诉豆瓣服务器，我们是什么类型的浏览器
    head={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}

    request =urllib.request.Request(url,headers=head)    #进行封装然后进行请求
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html










#保存数据
def saveData(datalist,savepath):
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建这个对象
    sheet = book.add_sheet("豆瓣电影",cell_overwrite_ok=True)  # 创建工作表
    col=("电影详情链接","图片链接","影片中文名","影片外国名","评分","评分数","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])#列名
    for i in range(0,250):
        print("第%d条" % i)
        data=datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])



    book.save("student2.xls")



def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn=sqlite3.connect(dbpath)
    cur=conn.cursor()


    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index]='"'+data[index]+'"'
        sql='''
            insert into movie250(
                info_link,pic_link,cname,ename,score,rated,instroduction,info)
            values(%s)'''%",".join(data)   #用,与值链接起来，填补%s
        #print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()






def init_db(dbpath):
    sql='''
        create table movie250
        (
            id integer primary key autoincrement,
            info_link text,
            pic_link text,
            cname varchar,
            ename varchar,
            score numeric,
            rated numeric,
            instroduction text,
            info text
        );
    '''      #创建数据表
    conn=sqlite3.connect(dbpath)
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
    #init_db("movietest.db")
    print("爬取完毕")

