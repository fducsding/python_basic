from bs4 import BeautifulSoup  #将Html文档转换成一个复杂的树形结构

file=open("./douban.html","rb")#二进制读取

html =file.read()
bs=BeautifulSoup(html,"html.parser")#BeautifulSoup解析html用html.parser解析


#1.标签及其内容：拿到找到的第一个内容,拿到的是标签
# print(bs.title)     #拿到的是title标签内的所有的内容
# print(bs.title.string)   #只拿到了title标签的内容
# print(bs.a)
# print(bs.a.attrs)
# print(bs.name)
# print(bs)

#文档的遍历
# print(bs.head.contents)  返回的是一个列表，所以可以用[]来遍历
# print(bs.head.contents[1])


#文档的搜索    这是最重要的
t_list=bs.find_all("a")   #返回一个列表，找到所有的a标签
#<a>()</a> 为一个内容
print(t_list)

# import re
# #正则表达式使用search来匹配内容
# t_list=bs.find_all(re.compile("a"))
#
# for item in t_list:
#     print(t_list)
#
# #find_all里面给参数,具体百度
# t_list=bs.find_all(href="")
