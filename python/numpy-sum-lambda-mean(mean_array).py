# https://www.codewars.com/kata/563e320cee5dddcf77000158
# It's the academic year's end, fateful moment of your school report. The averages must be calculated.
# All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.
# Return the average of the given array rounded down to its nearest integer.
# The array will never be empty.
# 这是学年结束，你学校报告的决定性时刻。平均值必须计算。所有的学生都来找你，并恳求你计算他们的平均值。简单 ！你只需要写一个脚本。
# 将给定数组的平均值向下舍入为最接近的整数。
# 该数组永远不会为空
import numpy
def get_average(marks):
    return int(numpy.mean(marks))

def get_average(marks):
    return sum(marks) / len(marks)

import math
import numpy
def get_average(marks):
    number =  numpy.average(marks)
    return math.floor(number)

get_average = lambda m: int(__import__("numpy").mean(m))

def get_average(marks):
    sum = 0
    count = 0
    for m in marks:
        sum += m
        count += 1 
    return sum/count

def get_average(marks):
    result = 0
    for i in marks:
        result += i
    return(round(result/len(marks)))

def get_average(l):
    return reduce(lambda x, y: x + y, l) / len(l)

from numpy import mean
from math import floor
def get_average(marks):
    return floor(mean(marks))
# NumPy系统是Python的一种开源的数值计算扩展
# mean()函数功能：求取均值
# numpy.mean(now2) # 对所有元素求均值
# numpy.mean(now2,0) # 压缩行，对各列求均值
# numpy.mean(now2,1) # 压缩列，对各行求均值

def get_average(marks):
# my code
    total = 0
    for i, element in enumerate(marks):
        total += element
    return total/(len(marks))
    raise NotImplementedError("TODO: get_average")
