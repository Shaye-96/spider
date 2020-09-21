# -*- codeing = utf-8 -*-
# @Time : 2020/9/2110:45
# @Author : Shaye
# @File : testBS4.py
# @Software : PyCharm

from bs4 import BeautifulSoup
import re

'''
BeautifulSoup4  将复杂的html 文档转化为一个复杂的树形结构，每个节点都是一个 python 对象，所有对象可以归为四类：
- Tag   标签及其内容，拿到它所找到的第一个内容
- NavigableString   标签里的内容
- BeautifulSoup     表示整个文档
- Comment       特殊的 NavigableString，表示标签内注释掉的内容（不包括注释符号）
'''

file = open('./baidu.html', 'rb')  # rb 打开文件的方式，以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头
html = file.read().decode('utf-8')
bs = BeautifulSoup(html, "html.parser")  # 两个参数分别表示：解析内容，解析器

'''
print(bs.title)  # Tag
print(type(bs.title))
print(bs.title.string)  # NavigableString
print(bs.a.attrs)   # 返回标签属性
print(type(bs))     # BeautifulSoup
'''

# ----------------------------------------------
# 遍历文档
# print(bs.head.contents)  # 返回的是一个 list 列表
# 更多内容搜索BeautifulSoup 文档

# 搜索文档
# (1) find_all    查找所有符合条件的值，返回的是一个 list 列表

# - 字符串过滤
t_list = bs.find_all("a")
# print(t_list)

# - 正则表达式搜索: 使用 search() 方法进行搜索
t_list1 = bs.find_all(re.compile("a"))
# print(t_list1)


# - 方法：传入一个方法（函数），根据函数要求进行搜素
def name_is_exists(tag):
    return tag.has_attr("name")


t_list2 = bs.find_all(name_is_exists)
# print(t_list2)

# (2) kwargs    参数

t_list3 = bs.find_all(class_=True)
# print(t_list3)

# (4) text    文本参数
t_list4 = bs.find_all(text="hao123")
t_list5 = bs.find_all(text=["hao123", "地图"])
t_list6 = bs.find_all(text=re.compile("\d"))    # 应用正则表达式查找 包含特定文本的内容（标签内的字符串）
# print(t_list4)
# print(t_list5)
# print(t_list6)

# (5) limit   参数,限制查找个数
t_list7 = bs.find_all("a", limit=3)
# print(t_list7)

# (6) css选择器
print(bs.select("head > title"))
print(bs.select("title"))
print(bs.select("#head"))
print(bs.select("a[class='bri']"))  # 属性选择器
