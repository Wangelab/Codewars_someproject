# https://www.codewars.com/kata/551dc350bf4e526099000ae5
# 假设一首歌包含一些单词。为了制作这首歌的dubstep remix，Polycarpus在歌曲的第一个单词（数字可能为零），最后一个单词（数字可能为零）
# 之后以及单词之间插入一定数量的单词“WUB”至少在任何一对相邻单词之间），然后男孩将所有单词（包括“WUB”）粘在一起，然后在俱乐部播放歌曲。
# 输入包含一个非空字符串，只包含大写英文字母，字符串的长度不超过200个字符 ,用空格分开单词
# song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND
def song_decoder(song):
    return " ".join(song.replace('WUB', ' ').split())

def song_decoder(song):
    import re
    return re.sub('(WUB)+', ' ', song).strip()

def song_decoder(song):
    return ' '.join([a for a in song.split('WUB') if a])

def song_decoder(song):
    """ Simple WUB decoder :) """
    # Splitting strings by "WUBs" and filtering out voids
    list = filter(lambda x: x != '', song.split('WUB'))
    # Returning the joint items separed by spaces
    return ' '.join(list)

def song_decoder(song):
# my code
    import re
# 匹配
    song2 = song.replace("WUB",".")
    song3 = []
    for i, element in enumerate(song2.split(".")):
        if element == "":
            continue
        else:
            song3.append(element)
    return " ".join(song3)


