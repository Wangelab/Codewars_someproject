# https://www.codewars.com/kata/vowel-count
# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, and u as vowels for this Kata.
# The input string will only consist of lower case letters and/or spaces.
# 返回给定字符串中元音的数量（数量）。
# 我们将考虑一个，e，i，o和u作为这个Kata的元音。
# 输入字符串将只包含小写字母和/或空格。
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")
    
def getCount(s):
    return sum(c in 'aeiou' for c in s)
    
import re
def getCount(str):
    return len(re.findall('[aeiou]', str, re.IGNORECASE))

def getCount(inputStr):
    return sum(inputStr.count(char) for char in ['a', 'e', 'i', 'o', 'u'])

getCount = lambda s: sum(s.count(i) for i in 'aeiou')

def getCount(inputStr):
    list_vowels = ['a', 'e', 'i', 'o', 'u']
    return sum([inputStr.count(vowel) for vowel in list_vowels])

def getCount(inputStr):
    import re 
    num_vowels = 0
    # my code here
    vowels = re.findall(r'[aeiou]', inputStr)
    num_vowels = len(vowels)
    return num_vowels
