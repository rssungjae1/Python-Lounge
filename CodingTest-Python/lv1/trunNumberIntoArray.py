# https://programmers.co.kr/learn/courses/30/lessons/12932
# 자연수 뒤집어 배열로 만들기
n = 12345

def solution(n):
    answer = [int(i) for i in list(reversed(str(n)))]
    return answer

print(solution(n))