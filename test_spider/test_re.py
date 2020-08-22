import re

# re.I  #表示忽略大小写
# re.S  #如果字符串中有换行的话，没加re.S就是在一行中进行匹配，如果一行没有，就换一行
#       #如果加了re.S就是在整个字符串中进行匹配，不会因为有换行就一行一行匹配



#创建模式对象
# pat = re.compile("AA")#此处的AA是正则表达式用来验证其他的字符串
# m=pat.search("CBA")


#没有模式对象
# m=re.search("asd","Aasd")  #前面的规则，后面的被校验的
# print(m)



# print(re.findall("a","ASDSAadaa"))#前面的是规则
# print(re.findall("[A-Z]","ASDSAadaa"))
# print(re.findall("[A-Z]+","ASDSAadaa"))
#
# print(re.sub("a","A","abcsaa"))#找到小a用A替换
# print("agfd\'tz")



#将正则表达式编译成一个pattern 规则对象
# pattern =re.compile("\d")
# print(type(pattern))

# pattern.match()    #从起始位置开始查找，返回第一个符合规则的，只匹配一次
# pattern.search(str,begin,end)   #从任何位置往后查找，返回第一个符合规则的，只匹配一次
                                  #end取不到，左闭右开
# pattern.findall(str,begin,end)  #所有的全部匹配，返回列表
# pattern.split()    #分割字符串，返回列表
# pattern.finditer() #所有的全部匹配，返回的是一个迭代器
# pattern.sub()      #替换



