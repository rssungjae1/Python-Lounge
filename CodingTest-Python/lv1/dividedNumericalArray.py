# https://programmers.co.kr/learn/courses/30/lessons/12910

arr = [5, 9, 7, 10]	
divisor = 1

def solution(arr, divisor):
    answer = []
    for a in arr:
        if a%divisor == 0:
            answer.append(a)
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    return answer

solution(arr, divisor)