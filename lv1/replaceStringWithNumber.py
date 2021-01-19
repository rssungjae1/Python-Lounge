# https://programmers.co.kr/learn/courses/30/lessons/12925
s = "+12s"

def solution(s):
    answer = 0
    try:
      answer = int(s)
    except:
      print("not num type")
    return answer


solution(s)