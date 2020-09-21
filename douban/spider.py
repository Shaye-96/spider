# -*- coding = utf-8 -*-
# @Time : 2020/9/1914:59
# @Author : 杨烁
# @File : spider.py
# @Software : PyCharm

# 网页解析，获取数据
from bs4 import BeautifulSoup
# 正则表达式
import re
# 制定URL，获取数据
import urllib.request
import urllib.error
# 进行excel 操作
import xlwt
# 进行sqlite 数据库操作
import sqlite3


def main():
    # 爬取 -> 分析 -> 保存
    base_url: str = "https://movie.douban.com/top250?start="
    save_path: str = ".\\Top250.xsl"
    # 爬取网页
    getData(base_url)

    saveData(save_path)


# 爬取网页
def getData(base_url):
    data_list: list = []
    # 访问网页
    for i in range(0, 10):  # 左闭右开
        url = base_url + str(0*25)
        html = askUrl(url)
        # 2. 逐一解析数据(写到循环里，拿到一个网页解析一次)
    return data_list


# 访问网页
def askUrl(url):
    # 请求头
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    # 封装请求对象
    req = urllib.request.Request(url=url, headers=head)
    html: str = ""
    # 发起请求
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):   # 用于判断对象是否包含对应的属性  hasattr(Object, name)
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def saveData(save_path):
    print("save ... to", save_path)


if __name__ == '__main__':
    print("当前文件主程序")
    main()
