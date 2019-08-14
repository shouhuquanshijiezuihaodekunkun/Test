# Python3交互模式下，执行如下代码：
# a = [("b",2), ("a",1), ("c", 1),  ("d",4)]
# b = a.sort()
# print(a, b)
# 则显示的是？（）

# [("b",2), ("a",1), ("c", 1),  ("d",4)]...
#
# a = {}，以下说法正确都是？（）是字典还是集合
# 字典
# d = {"a": 3, "b": 2, "c": 1}，sorted(d)得到的是？
#a,b,c


# class A:
#     a =1
# obj = A()
# obj.a = 2
# print(obj.a)
# print(A.a)
# A.a = 3
# print(obj.a)
# 打印结果为：？？？
#
# 2 1 2

#
# 以下说法正确的是
# A.静态方法能访问实例变量和类变量
# B.实例方法一定有方法能访问类变量
# C.类方法不能访问实例变量
# D.实例方法只能访问实例变量
# E.set内有__add__方法
# F.int类内有__mod__方法
# G.list类内有__iadd__方法
# H.dict内有__getitem__方法
# BGH


# 输入三个整数x,y,z，请把这三个数由小到大输出
# (不使用列表等容器)
#

# x = int(input("请输入x:"))
# y = int(input("请输入y:"))
# z = int(input("请输入z:"))
# if x > y:
#     x,y = y,x
# if x > z:
#     x,z = z,x
# if y > z:
#     y,z = z,y
# print(x,y,z)


#
#
# 有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。
# 问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？

# a = 10
# b = a + 2
# c = b + 2
# d = c + 2
# e = d + 2
# print(e)

#
#  \


# def 装饰器名字(装饰器参数):
#     def 中间函数(func): #func 代表需要传入的(旧)功能函数
#         def middle(**a,**b):
#             判断装饰器参数
#             print("新功能")
#             func(**a,**b)
#             return
#         return middle
#     return 中间函数



# def print_():
#     def print_1(func):
#         def middle(*args,**kwargs):
#             func(*args,**kwargs)
#             if:
#                 ...
#             print("这是一个装饰器")
#             return
#         return middle
#     return print_1
#
#
# @print_
