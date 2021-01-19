# https://programmers.co.kr/learn/courses/30/lessons/12906

arr = [1,1,3,3,0,1,1]
arr2 = [4,4,4,3,3]

def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    answer.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer

solution(arr)    