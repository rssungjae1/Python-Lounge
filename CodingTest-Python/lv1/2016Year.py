# https://programmers.co.kr/learn/courses/30/lessons/12901
a = 2
b = 1

def solution(a, b):
    answer = ''
    date = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dif = b-1
    for idx in range(a-1):
        dif += month[idx]
    answer = date[dif % 7]
    return answer




solution(a, b)