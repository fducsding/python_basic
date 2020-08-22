import urllib.request

ua_headers ={"User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.6"}

request = urllib.request.Request("http://www.baidu.com/", headers = ua_headers)

response = urllib.request.urlopen(request)

html = response.read()

print(response.getcode())

print(response.info)



