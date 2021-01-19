# https://programmers.co.kr/learn/courses/30/lessons/12903

s = "abcde"
# s2 = "123456"
s2 = "123456789"

import math

def solution(s):
    le = len(s)/2
    if len(s)%2 == 0:
        answer = s[int(le)-1:int(le)+1]
    else:
        le = math.floor(le)
        answer = s[le:le+1]
    return answer

solution(s)