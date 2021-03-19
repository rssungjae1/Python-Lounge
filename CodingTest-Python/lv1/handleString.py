# https://programmers.co.kr/learn/courses/30/lessons/12918
s = "01234z"

def solution(s):
    if len(s)==4 or len(s)==6:
        answer = s.isdigit()
    else:
        answer = False
    return answer

print(solution(s))