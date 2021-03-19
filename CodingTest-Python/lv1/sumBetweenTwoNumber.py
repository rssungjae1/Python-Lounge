# https://programmers.co.kr/learn/courses/30/lessons/12912

a = 3
b = 5

def solution(a, b):
    answer = 0
    if a<b:
        ss = list(range(a,b+1))
    else:
        ss = list(range(b,a+1))
    for s in ss:
         answer += s
    return answer

solution(a, b)