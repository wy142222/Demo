'''
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额
'''
from Test2.send_money import *
sum_salary=send_money()
# print("总工资为{0}".format(sum_salary))
print(f"总存款金额为{sum_salary}")



