# https://www.codewars.com/kata/bit-counting/python
# Write a function that takes an (unsigned) integer as input, and returns the number of bits 
# that are equal to one in the binary representation of that number.
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
# 编写一个将（无符号）整数作为输入的函数，并返回该数字二进制表示中等于1的位数。
# 例如：1234is 的二进制表示10011010010，所以5在这种情况下函数应该返回


def countBits(n):
    return bin(n).count("1")
    
def countBits(n):
    total = 0
    while n > 0:
        total += n % 2
        n >>= 1
    return total
    
def countBits(n):
    """ count_bits == PEP8, forced camelCase by CodeWars """
    return '{:b}'.format(n).count('1')
    
def countBits(n):
    ret = 0
    while n:
        ret += n & 1
        n >>= 1
    return ret
    
def countBits(n):
    total = 0
    binaryNum = bin(n)[2:]
    for num in str(binaryNum):
        if num == "1":
            total += 1
    return total

def countBits(n):
    result =0
    while (n > 0):
        if(n%2)==1: result+=1
        n = int(n/2)
    return result

def countBits(n):
    return sum(int(x) for x in bin(n)[2:])    

def countBits(n):
    c = 0
    while n:
        c += 1
        n &= n - 1
    return c

def countBits(n):
    return 0 if n <= 0 else n % 2 + countBits(n // 2)

def countBits(n):
    binary = format(n, 'b')
    return sum(map(int, list(binary)))

from math import floor,log
countBits = lambda n:sum([ (n//2**i)%2 for i in range(floor(log(n,2)) + 1) ]) if n>0 else 0

def countBits(n):
    # 求二进制
    #n2 = bin(n)
    my code
    count = 0 # 计数
    while n:
        if n & 1:
            count += 1
        n = n >> 1
    return count



