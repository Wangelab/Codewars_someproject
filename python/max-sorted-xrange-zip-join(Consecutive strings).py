# https://www.codewars.com/kata/56a5d994ac971f1ac500003e
# 给你一个strarr字符串和一个整数的数组k。您的任务是返回数组中第一个由连续 k 个字符串组成的最长字符串。
# You are given an array strarr of strings and an integer k.
# Your task is to return the first longest string consisting of k consecutive strings taken in the array.
# Example: longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
# n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

def longest_consec(s, k):
    return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""

def longest_consec(strarr, k):
    result = ""   
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s          
    return result
  
def longest_consec(strarr, k):
    if (len(strarr) == 0 or k <= 0) or len(strarr) < k:
        return ""
    lst = [''.join(strarr[i:i+k]) for i in xrange(len(strarr))]
    return max(lst, key= lambda x: len(x))
    
def longest_consec(s, k):
    n = len(s)
    if n == 0 or k > n or k <= 0:
      return ''
    return sorted([''.join(s[i:i+k]) for i in range(0, n-k+1)], key=len, reverse=True)[0]
    
def longest_consec(strarr, k):
    return max([''.join(tuple) for tuple in zip(*[strarr[i:] for i in range(k)])] + [''], key=len)

def longest_consec(strarr, k):
    if len(strarr)!=0 and k<=len(strarr) and k>0:
        max=""
        for i in range(len(strarr)-k+1):
            temp=""
            for j in range(k):
                temp+=strarr[i+j]
            if len(temp)>len(max):
                max=temp
        return max
    else:
        return ""

def longest_consec(st, k):
    res = []
    n = len(st); 
    if n <= 0 or k > n or k <= 0: 
        return ''
    for i in st:
        res.append(''.join(st[st.index(i):st.index(i)+k]))
    return max(res, key=len)




def longest_consec(strarr, k):
    # my code  
    n = len(strarr) 
    strfin = "" 
    if n == 0 or k > n or k <= 0:
        return ""
    else:
        for i in range(n-k+1):
            strd = "".join(strarr[i:i+k])
            if len(strd) > len(strfin):
                strfin = strd
        return strfin





