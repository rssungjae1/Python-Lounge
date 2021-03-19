# https://programmers.co.kr/learn/courses/30/lessons/12933
# 정수 내림차순으로 배치하기

n = 118372
# 873211

def solution(n):
    return int("".join(sorted(reversed(list(str(n))),reverse=True)))

# reversed를 할 필요가 없었네;
print(solution(n))