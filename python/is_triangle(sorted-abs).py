# https://www.codewars.com/kata/56606694ec01347ce800001b

def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)

def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c

def is_triangle(a, b, c):
  return abs(a-b) < c < a+b

def is_triangle(a, b, c):
    return 2 * max(a, b, c) < a + b + c

def is_triangle(a, b, c):
    return all([a < b+c, b < a+c, c < a+b]) 

def is_triangle(a, b, c):
# my code
    if (a + b > c)&(a + c > b)&(b + c > a):
        return True
    else:
        return False
