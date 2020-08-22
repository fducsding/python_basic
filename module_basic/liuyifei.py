# import requests
# import os
#
# def getManyPages(keyword,pages):
#     params=[]
#     for i in range(30,30*pages+30,30):
#         params.append({
#                         'tn': 'resultjson_com',
#                         'ipn': 'rj',
#                         'ct': 201326592,
#                         'is': '',
#                         'fp': 'result',
#                         'queryWord': keyword,
#                         'cl': 2,
#                         'lm': -1,
#                         'hd':'',
#                         'latest':'',
#                         'copyright':'',
#                         'ie': 'utf-8',
#                         'oe': 'utf-8',
#                         'adpicid':'',
#                         'st':'',
#                         'z':'',
#                         'ic':'',
#                         'word': keyword,
#                         's':'',
#                         'se':'',
#                         'tab':'',
#                         'width':'',
#                         'height':'',
#                         'face':'',
#                         'istype':'',
#                         'qc':'',
#                         'nc': 1,
#                         'fr':'',
#                         'pn': i,
#                         'rn': 30,
#                         'gsm': '14a',
#                         '1593381420733':''
#                   })
#     url='http://image.baidu.com/search/acjson'
#     urls = []
#     # print(type(requests.get(url,params[0]).json()["data"][0]["thumbURL"]))
#     for i in params:
#         urls.append(requests.get(url,params[0],headers=headers).json().get("data"))
#     # print(urls)
#     return urls
#
# headers = {
#     "referer":"http://image.baidu.com/search/",
#     "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
#
# def getImg(dataList, localPath):
#
#     if not os.path.exists(localPath):  # 新建文件夹
#         os.mkdir(localPath)
#     print(dataList)
#     x = 0
#
#     for list in dataList:
#         for i in list:
#             # print(i)
#             if i.get('middleURL') != None:
#                 print('正在下载：%s' % i.get('middleURL'))
#                 ir = requests.get(i.get('middleURL'),headers=headers)
#                 open(localPath + '%d.jpg' % x, 'wb').write(ir.content)
#                 x += 1
#             else:
#                 print('图片链接不存在')
#
# if __name__ == '__main__':
#     dataList = getManyPages('刘亦菲',5)  # 参数1:关键字，参数2:要下载的页数
#     getImg(dataList,'E:/meizi/') # 参数2:指定保存的路径

def a():
    keys="liu"
    params = []
    for i in range(30, 90, 30):
        params.append({
            'tn': 'resultjson_com',
            'ipn': 'rj',
            'ct': 201326592,
            'is': '',
            'fp': 'result',
            'queryWord': keys,
            'cl': 2,
            'lm': -1,
            'hd': '',
            'latest': '',
            'copyright': '',
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': '',
            'z': '',
            'ic': '',
            'word': keys,
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': '',
            'istype': '',
            'qc': '',
            'nc': 1,
            'fr': '',
            'pn': i,
            'rn': 30,
            'gsm': '14a',
            '1593381420733': ''
        })

    urls=[]
    base_url = "http://image.baidu.com/search/acjson"
    for i in params:
        print(i)
        # urls.append(base_url + params[i])

    # print(urls)

a()