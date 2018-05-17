# https://www.codewars.com/kata/5a91a7c5fd8c061367000002
# Given an array of N integers, you have to find how many times you have to add up the smallest numbers in the array until their Sum becomes greater or equal to K.
# List size is at least 3.
# All numbers will be positive.
# Numbers could occur more than once , (Duplications may exist).
# Threshold K will always be reachable.
# 鉴于 N个整数数组，你必须找到 多少次 ，你必须 加起来最小的数字 数组中，直到 它们的总和 变得大于或等于 ķ。
# 列表大小 为至少3。
# 所有数字 都是 正数。
# 数字 可能 会出现多次， （可能存在重复）。
# 阈值 K 将始终可达。
# minimumSteps({1, 10, 12, 9, 2, 3}, 6)

def minimum_steps(arr, n):
    arr = sorted(arr)
    s = 0
    for i,v in enumerate(arr): 
        s += v
        if s >= n: return i

def minimum_steps(r,n):
  def get_short(r):
    mn = r[0]
    q = 0
    for i,v in enumerate(r):
      if v < mn:
        mn = v
        q = i
    del r[q]
    return mn 
  ix = r[:]
  q = get_short(ix)
  c = 0
  while q < n:
    q += get_short(ix)
    c += 1
  return c

def minimum_steps(nums, value):
    sortNums = sorted(nums)
    return minimum_steps(sortNums[:-1], value) if (sum(sortNums[:-1]) >= value) else len(sortNums) - 1

from heapq import heapify, heappop
def minimum_steps(numbers, value):
    h = numbers
    heapify(h)
    i, s = 0, 0
    while s < value:
        s += heappop(h)
        i += 1
    return max(i - 1, 0)

from itertools import takewhile, accumulate
def minimum_steps(numbers, value):
    return sum(1 for _ in takewhile(lambda x: x < value, accumulate(sorted(numbers))))
#用于删除并返回数组的最后一个元素

def minimum_steps(numbers, value):
    numbers.sort(reverse=True)
    s = 0
    c = -1
    while s < value:
        s += numbers.pop()
        c += 1
    return c

def minimum_steps(arr, goal):
    steps = 0
    sum = 0
    while True:
        sum += min(arr)
        if sum >= goal: return steps
        else: steps += 1
        arr.remove(min(arr))
        
  def minimum_steps(numbers, value):
    #my code here   
    sumnum = 0 
    count = -1
    for element in sorted(numbers):
        if sumnum < value:
            sumnum += element
            count +=1
        else:
            break
    return count




