# https://programmers.co.kr/learn/courses/30/lessons/68644
numbers = [2,1,3,4,1]

def solution(numbers):
    li = []
    for num in range(len(numbers)-1):
        for n in range(num+1,len(numbers)):
            li.append(numbers[num] + numbers[n])
    answer = sorted(list(set(li)))
    return answer

solution(numbers)
print(solution(numbers))