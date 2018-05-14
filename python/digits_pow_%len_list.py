# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n. In other words:
# 给定一个写成abcd ...（a，b，c，d ...为数字）的正整数n和一个正整数p，我们希望找到一个正整数k，如果存在的话，比如数字的总和对于p的连续幂的n等于k * n。换一种说法：
# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
# 是否有整数k，例如：（a ^ p + b ^（p + 1）+ c ^（p + 2）+ d ^（p + 3）+ ...）= n * k
# If it is the case we will return k, if not return -1.
# 如果是这种情况，我们将返回k，否则返回-1。
# Note: n, p will always be given as strictly positive integers.
# 注意：n，p将始终作为严格正整数给出。
# dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
# dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
# dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
# dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1

def dig_pow(n, p):
    k, fail = divmod(sum(int(d)**(p + i) for i, d in enumerate(str(n))), n)
    return -1 if fail else k
 
def dig_pow(n, p):
    import math
    # your code
    # mycode
    list_n = list(str(n))
    len_n = len(list_n)
    total = 0
    for m in range(0,len_n):
        total += int(math.pow(int(list_n[m]), p+m))
    k = total / n
    q = total % n
    if q == 0:
        return k
    else:
        return -1
