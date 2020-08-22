import urllib.request

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}


# #构建一个HTTPHandler处理器对象，支持处理HTTP的请求
# http_handler=urllib.request.HTTPHandler()
#
# #在HTTPHandler增加参数 debuglevel=1 将会自动打开Debug log模式
# #在程序执行的时候会打印收发包的信息
# # http_handler=urllib.request.HTTPHandler(debuglevel=1)
#
#
#
#
# #调用build_opener()方法构建一个自定义的opener对象，参数是构建的处理器对象
# opener=urllib.request.build_opener(http_handler)
#
# request=urllib.request.Request("http://www.baidu.com/")
#
# response=opener.open(request)
#
# print(response.read().decode("utf-8"))




#代理开关，表示是否启用代理
proxyswitch=True

#构建一个Handler处理器对象，参数是一个字典类型，包括代理类型和代理服务器IP+PROT
httpproxy_handler=urllib.request.ProxyHandler({"http":"183.154.214.186:9000"})

#构建一个没有代理得处理器对象
nullproxy_handler=urllib.request.ProxyHandler({})


if proxyswitch:
    opener=urllib.request.build_opener(httpproxy_handler)
else:
    opener=urllib.request.build_opener(nullproxy_handler)

#构建了一个全局的opener,之后所有的请求都可以用urlopen()方式去发送，也附带Handler的功能
urllib.request.install_opener(opener)

request=urllib.request.Request("http://www.baidu.com/",headers=headers)
reponse=urllib.request.urlopen(request)

print(reponse.read())