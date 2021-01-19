# https://programmers.co.kr/learn/courses/30/lessons/12930
s = "try hello world" # "TrY HeLlO WoRlD"

def solution(s):
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])

def solution2(s):
    answer = ''
    a_list = []
    for i in s.split(" "):
        answer2 = ""
        for index, ii in enumerate(range(len(i))):
            if ii % 2 == 0:
                answer2 += i[ii].upper()
            else:
                answer2 += i[ii].lower()
        a_list.append(answer2)
    return " ".join(a_list)
print(solution(s))