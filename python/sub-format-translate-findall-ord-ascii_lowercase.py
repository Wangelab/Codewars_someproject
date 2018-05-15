# In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.
# 在工厂里，打印机打印盒子的标签。对于一种盒子，打印机必须使用颜色，为简单起见，这些颜色用字母命名a to m
# Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm.
# 有时会出现问题：缺少颜色，技术故障和“坏”控制字符串，例如aaaxbbbbyyhwawiwjjjwwm
# You have to write a function printer_error which given a string will output the error rate of the printer as a string representing a rational whose numerator is the
# number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.
# 您必须编写一个函数printer_error，给定一个字符串将输出打印机的
# 错误率作为一个字符串表示一个有理数，其分子是错误的数量，分母是控制字符串的长度。不要将这部分减少到更简单的表达式。
# s="aaabbbbhaijjjm"
# error_printer(s) => "0/14"
# s="aaaxbbbbyyhwawiwjjjwwm"
# error_printer(s) => "8/22"

from re import sub
def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))
    
def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))
    
def printer_error(s):
    errors = 0
    count = len(s)
    for i in s:
        if i > "m":
            errors += 1
    return str(errors) + "/" + str(count)
    
def printer_error(s):
    return "%s/%s" % (len(s.translate(None, "abcdefghijklm")), len(s))

def printer_error(s):
    import re
    return str(len(re.findall('[n-z]', s))) + "/" + str(len(s))
    
def printer_error(s):
    return '{}/{}'.format(sum(color > 'm' for color in s), len(s))
    
import string
ERROR_CODES = string.ascii_lowercase[13:]
def printer_error(s):
    return "{}/{}".format(len([x for x in s if x in ERROR_CODES]), len(s))
    
def printer_error(s):
    s1 = len([ x for x in s if ord(x) > ord('m')])
    return str(s1) +'/' + str(len(s))
    
import re
def printer_error(s):
    # my code
    # 匹配
    s2 = re.findall(r'[nopqrstuvwxyz]',s) 
    return '%s/%s'%(len(s2),len(s))
