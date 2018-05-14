# 任务
# 功能编码splitAndMerge，功能接受2个参数：str和sp。str是一个句子。sp是一个字符作为分隔符。
# 首先，我们需要将句子分成单词（使用分隔符空格）; 然后将每个单词分成字符（使用分隔符空字符串）; 
# 然后将每个字符与指定的合并sp; 最后合并所有单词（使用分隔符空格）并将其返回。
# 例如：
# splitAndMerge("My name is John"," ") should return "M y n a m e i s J o h n"
# splitAndMerge("My name is John","-") should return "M-y n-a-m-e i-s J-o-h-n"
# splitAndMerge("Hello World!",".") should return "H.e.l.l.o W.o.r.l.d.!"
# splitAndMerge("Hello World!",",") should return "H,e,l,l,o W,o,r,l,d,!"`

def split_and_merge(string, sp):
    return ' '.join(sp.join(word) for word in string.split())

def split_and_merge(string, sp):
    return ' '.join(map(sp.join, string.split()))
    # map()以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表
    
def split_and_merge(string, sp):
    newstring = string.split(' ')
    # enumerate(sequence, [start=0])将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
    # 同时列出数据和数据下标，一般用在 for 循环当中。
    for i, thing in enumerate(newstring):
        newstring[i] = sp.join(list(thing))
    return ' '.join(newstring)
