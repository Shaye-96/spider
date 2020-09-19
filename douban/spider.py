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
    base_url: str = "https://movie.douban.com/top250"
    print(base_url)
if __name__ == '__main__':
    print("当前文件主程序")
    main()
