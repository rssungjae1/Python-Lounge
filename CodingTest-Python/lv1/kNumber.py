# https://programmers.co.kr/learn/courses/30/lessons/42748
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    
    for command in commands:
        test = sorted(array[command[0]-1:command[1]])[command[2]-1]
        answer.append(test)

    return answer

solution(array, commands) 