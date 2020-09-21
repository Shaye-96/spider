# -*- codeing = utf-8 -*-
# @Time : 2020/9/2115:47
# @Author : Shaye
# @File : testRe.py
# @Software : PyCharm

import re

'''
re.search() 在一个字符串中搜索匹配正则表达式的  第一个位置 ，返回 match 对象
re.match()  从一个字符串开始位置起，匹配正则表达式，返回 match 对象
re.findall()搜索字符串，返回匹配的全部值，返回 list
re.split()  将字符串按照正则表达式进行分割，返沪 list
re.finditer()搜索字符串，返回匹配结果的迭代类型，每个迭代对象是 match 对象
re.sub()    在一个字符串中提替换所有匹配正则表达式的子串，返回替换后的字符串
'''

# 1.创建模式对象
pat = re.compile("a")   # 括号里的字符串就是正则表达式
m = pat.search("abcd")
print(m)

# 2.不创建模式对象
test1 = re.search("a", "abcd")
print(test1)

test2 = re.findall("[a-z]", r"abcabcabc")
print(test2)

test3 = re.sub("ab", "A", r"abcabcabc")   # 找到 a 替换为 A
print(test3)

# 建议在正则表达式中，被比较的字符串前面加 r ，不用担心转义字符的问题
