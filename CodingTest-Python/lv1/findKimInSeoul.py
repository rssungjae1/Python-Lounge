# https://programmers.co.kr/learn/courses/30/lessons/12919
seoul = ["Jane", "Kim"]

def solution(seoul):
    answer = "김서방은 {}에 있다".format(seoul.index("Kim"))
    return answer

print(solution(seoul))