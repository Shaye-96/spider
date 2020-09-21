# -*- codeing = utf-8 -*-
# @Time : 2020/9/219:23
# @Author : Shaye
# @File : testUrllib.py
# @Safeware : PyCharm

import urllib.request

# 获取一个get请求
response = urllib.request.urlopen("http://www.baidu.com")  # 封装为一个 对象 Object
# print(response.read().decode('utf-8'))  # read()读取获取到的对象，.decode('utf-8')更改解析对象的编译模式

# 获取一个post请求
import urllib.parse  # 按照一定格式解析键值对

data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")  # bytes 将数据转换为二进制的数据包
response1 = urllib.request.urlopen("http://httpbin.org/post", data=data)  # 封装为一个 对象 Object
# print(response1.read().decode("utf-8"))

# 超时处理
try:
    response2 = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
    # print(response2)
except urllib.error.URLError as e:
    print("time out!")

response3 = urllib.request.urlopen("http://www.baidu.com")
print(response3.status)  # 状态码是418 表示网站发现这次访问是 爬虫访问
print(response3.getheaders())  # 请求头
print(response3.getheader("Bdpagetype"))  # 请求头内的某一项值

# 如何解决网页禁止爬虫访问
url = "https://www.douban.com"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")  # 封装请求对象，但没有进行请求
req = urllib.request.Request(url=url, headers=headers) # method 默认为 get
response4 = urllib.request.urlopen(req)
print(response4.read().decode("utf-8"))

