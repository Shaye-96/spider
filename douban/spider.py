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
    excel_path: str = "movie_Top250.xls"
    db_path = "movie_Top250.db"
    # 爬取网页
    data = getData(base_url)
    print(data)
    # 保存数据
    saveDataToSqlite(db_path, data)
    saveDataToExcel(excel_path, data)


# 全局变量，创建正则表达式，方便全局调用
find_link = re.compile(r'<a href="(.*?)">')  # 详情链接
find_img = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S 让换行符包含在字符中
find_title = re.compile(r'<span class="title">(.*)</span>')
find_score = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
find_judge = re.compile(r'<span>(\d*)人评价</span>')
find_intro = re.compile(r'<span class="inq">(.*)</span>')
find_about = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页
def getData(base_url):
    data_list: list = []
    # 访问网页
    for i in range(0, 10):  # 左闭右开
        url = base_url + str(0 * 25)
        html = askUrl(url)
        # 2. 逐一解析数据(写到循环里，拿到一个网页解析一次)
        soup = BeautifulSoup(html, "html.parser")  # 解析爬取回来的代码，形成树形结构对象
        for item in soup.find_all('div', class_="item"):  # 查找符合条件的值，返回list
            data = []  # 保存一部电影的信息
            item = str(item)  # 将每一小块 转换为字符串，方便后面使用正则表达式进行解析

            # 链接
            link = re.findall(find_link, item)[0]  # findall() 返回值为 list
            data.append(link)
            # 图片
            img = re.findall(find_img, item)[0]
            data.append(img)
            # 名称
            titles = re.findall(find_title, item)
            if len(titles) == 2:  # 名称数量不同，做不同的处理
                ctitel = titles[0]
                data.append(ctitel)
                otitle = titles[1].replace("/", "")  # 字符串的替换
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append("")  # 留空
            # 评分
            score = re.findall(find_score, item)[0]
            data.append(score)
            # 评论人数
            judge = re.findall(find_judge, item)[0]
            data.append(judge)
            # 介绍
            intro = re.findall(find_intro, item)[0]
            if len(intro) != 0:
                intro = intro.replace("。", "")
                data.append(intro)
            else:
                data.append("")  # 留空
            # 其他
            about = re.findall(find_about, item)[0]
            about = re.sub(r'<br(\s+)?/>(\s+)?', "", about)  # 替换<br/>
            about = re.sub(r'/', "", about)  # 替换斜杠
            about = about.strip()  # 去掉 空格
            data.append(about)

            data_list.append(data)  # 将一部电影的信息放入 data_list

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
        if hasattr(e, "code"):  # 用于判断对象是否包含对应的属性  hasattr(Object, name)
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def saveDataToExcel(save_path, data):
    # 创建对象
    work_book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    # 创建工作表单
    work_sheet = work_book.add_sheet("sheet1", cell_overwrite_ok=True)  # cell_overwrite_ok 表示是否可以覆盖重写
    # list
    col = ["电影详情链接", "图片链接", "影片中文名", "影片外文名", "评分", "评价人数", "概况", "相关信息"]
    # 向 列表list 任意位置 插入元素，append 只可以插到末尾
    data.insert(0, col)
    index_i = 0
    for i in data:
        index_j = 0
        for j in i:
            work_sheet.write(index_i, index_j, j)
            index_j += 1
        index_i += 1
        work_book.save(save_path)


def saveDataToSqlite(path, data):
    # 初始化数据库
    init_db(path)
    # 连接数据库
    conn = sqlite3.connect(path)
    # 创建数据库对象
    c = conn.cursor()
    for item in data:
        for index in range(0, len(item)):
            if index == 4 or index == 5:
                continue
            item[index] = '"' + item[index] + '"'
            insert_table = '''
                insert into movies (info_link,img_link,cname,ename,score,judge,intro,about)
                values(%s)''' % ",".join(item)
        # 执行数据库语言
        c.execute(insert_table)
    # 提交操作
    conn.commit()
    # 关闭数据库连接
    conn.close()


def init_db(path):
    creat_table = '''
        create table movies
        (id integer not null primary key autoincrement,
         info_link text,
         img_link  text,
         cname     varchar,
         ename     varchar,
         score     numeric,
         judge     numeric,
         intro     text,
         about     text);
    '''
    # 创建数据库
    conn = sqlite3.connect(path)
    # 创建数据库对象
    c = conn.cursor()
    # 执行数据库语言
    c.execute(creat_table)
    # 提交操作
    conn.commit()
    # 关闭数据库连接
    conn.close()


if __name__ == '__main__':
    print("当前文件主程序")
    main()
