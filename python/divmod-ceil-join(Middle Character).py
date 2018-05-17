# https://www.codewars.com/kata/56747fd5cb988479af000028
# return the middle character of the word. 
# If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
# 返回单词的中间字符。如果单词的长度是奇数，则返回中间字符。如果单词的长度是偶数，则返回中间的2个字符
# Kata.getMiddle("test") should return "es"
# Kata.getMiddle("testing") should return "t"
# Kata.getMiddle("middle") should return "dd"
# Kata.getMiddle("A") should return "A"

def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]

def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]

from math import ceil
def get_middle(s):
  return s[int(ceil(len(s) / 2.0)) - 1:len(s) // 2 + 1]
  
def get_middle(s):
    if len(s) % 2 == 0: # Even?
        index = len(s)/2 
        return "".join([s[index-1], s[index]]) # join the chars at the midpoint
    if len(s) % 2 == 1: # Odd?
        index = len(s)/2 
        return s[index]

def get_middle(s):
    #my code here
    s_len = len(s)
    strings = ''
    if 0 < s_len < 1000:
        mid = s_len / 2
        if s_len % 2 == 0: 
            strings = s[mid-1:mid+1]
        elif s_len % 2 != 0:
            strings = s[int(mid)]
    return strings

