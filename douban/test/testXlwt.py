# -*- codeing = utf-8 -*-
# @Time : 2020/9/2210:09
# @Author : Shaye
# @File : testXlwt.py
# @Sofeware : PyCharm

import xlwt

# 创建对象
work_book = xlwt.Workbook(encoding="utf-8")
# 创建工作表单
work_sheet = work_book.add_sheet("sheet1")
# 写入
# work_sheet.write(0, 0, "hello")
# # 保存
# work_book.save("test.xls")
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in num_list:
    for j in num_list:
        if j >= i:
            work_sheet.write(i-1, j-1, "%d * %d = %d"%(i, j, i * j))
work_book.save("test.xls")
