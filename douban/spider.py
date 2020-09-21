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


# 全局变量，创建正则表达式，方便全局调用
find_link = re.compile(r'<a href="(.*?)">')     # 详情链接
find_img = re.compile(r'<img.*src="(.*?)"', re.S)     # re.S 让换行符包含在字符中
find_title = re.compile(r'<span class="title">(.*)</span>')
find_score = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
find_judge = re.compile(r'<span>(\d*)人评价</span>')
find_intro = re.compile(r'<span class="inq">(.*)</span>')
find_about = re.compile(r'<p class="">(.*)</p>', re.S)
# 爬取网页
def getData(base_url):
    data_list: list = []
    # 访问网页
    for i in range(0, 10):  # 左闭右开
        url = base_url + str(0*25)
        html = askUrl(url)
        # 2. 逐一解析数据(写到循环里，拿到一个网页解析一次)
        soup = BeautifulSoup(html, "html.parser")   # 解析爬取回来的代码，形成树形结构对象
        for item in soup.find_all('div', class_="item"):    # 查找符合条件的值，返回list
            data = []   # 保存一部电影的信息
            item = str(item)    # 转换为字符串，方便后面使用正则表达式进行解析
            link = re.findall(find_link, item)[0]   # findall() 返回值为 list
            data.append(link)
            img = re.findall(find_img, item)[0]
            data.append(img)
            titles = re.findall(find_title, item)
            if len(titles) == 2:
                ctitel = titles[0]
                data.append(ctitel)
                otitle = titles[1].replace("/","")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append("")     # 留空
            score = re.findall(find_score, item)[0]
            data.append(score)
            judge = re.findall(find_judge, item)[0]
            data.append(judge)
            intro = re.findall(find_intro, item)[0]
            if len(titles) != 0:
                intro = intro.replace("。", "")
                data.append(intro)
            else:
                data.append("")     # 留空
            about = re.findall(find_about, item)[0]
            data.append(about)
            print(about)
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
