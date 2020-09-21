# -*- codeing = utf-8 -*-
# @Time : 2020/9/2110:45
# @Author : Shaye
# @File : testBS4.py
# @Software : PyCharm

from bs4 import BeautifulSoup

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
print(bs.head.contents)  # 返回的是一个 list 列表
# 更多内容搜索BeautifulSoup 文档

# 搜索文档





