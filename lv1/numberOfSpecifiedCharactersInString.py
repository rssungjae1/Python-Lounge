# https://programmers.co.kr/learn/courses/30/lessons/12916
s = "pPoooyY"

def solution(s):
    answer = True
    if s.upper().count("P") != s.upper().count("Y"):
        answer = False
    return answer

solution(s)