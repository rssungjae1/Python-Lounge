# https://programmers.co.kr/learn/courses/30/lessons/68935
n = 45	

def solution(n):
    answer = 0
    answer_list = []
    while True:
        n, r = divmod(n,3)
        answer_list.append(r)
        if n == 0:
            break
    answer_list.reverse()
    for a in range(len(answer_list)):
        answer += answer_list[a]*(3**a)
    return answer




solution(n)