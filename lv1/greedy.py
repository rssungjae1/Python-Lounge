# https://programmers.co.kr/learn/courses/30/lessons/42862
n = 6
lost = [2,3,4,5]
reserve = [3,4,6]
def solution(n, lost, reserve):
    students = list([num for num in range(1,n+1)])
    result = list(set(lost) & set(reserve))
    # _reserve = [r for r in reserve if r not in lost]
    # _lost = [l for l in lost if l not in reserve]
    for r in result:
        lost.remove(r)
        reserve.remove(r)
    for lost_stu in lost:
        if ((lost_stu-1) in reserve):
            reserve.remove(lost_stu-1)
        elif ((lost_stu+1) in reserve):
            reserve.remove(lost_stu+1)
        else:
            students.remove(lost_stu)
    answer = len(students)
    return answer

solution(n, lost, reserve)