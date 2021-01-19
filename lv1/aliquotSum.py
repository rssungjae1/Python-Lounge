# https://programmers.co.kr/learn/courses/30/lessons/12928
n = 12 #28

def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer

solution(n)