# https://programmers.co.kr/learn/courses/30/lessons/12926
s = "a B z"
n = 4
print(ord(s[4]))
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper(): 
            s[i]=chr((ord(s[i]) + n - ord('A')) % 26 + ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i]) + n - ord('a')) % 26 + ord('a'))
    return "".join(s)



#26개 26개
#A~Z 65~90
# 89 + 2 => 65
# 87 + 2 => 89
# 91 - 26
#a~z 97~122
solution(s,n)