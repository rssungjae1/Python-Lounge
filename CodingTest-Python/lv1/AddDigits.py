n = "123"

def solution(n):
    answer = 0
    strN = str(n)
    for i in range(len(strN)):
        answer += int(strN[i])
    return answer

solution(n)