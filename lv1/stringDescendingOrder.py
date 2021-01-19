# https://programmers.co.kr/learn/courses/30/lessons/12917
s = "Zbcdefg"

def solution(s):
    a_list = []
    for ss in range(len(s)):
        a_list.append(s[ss])
    a_list.sort(reverse=True)
    return "".join(a_list)

print(solution(s))