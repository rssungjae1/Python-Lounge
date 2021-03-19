# 실력체크 레벨1
"""
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
예를 들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.
"""
# def solution(s):
#     if len(s) == 4 or len(s) == 6:
#         try:
#             int(s)
#             answer = True
#         except :
#             answer = False
#     else:
#         answer = False
#     return answer
# solution("a234")

"""
정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.
arr은 길이 1 이상, 100 이하인 배열입니다.
arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.
"""
# def solution(arr):
#     temp = 0
#     for a in arr:
#         temp += a
#     answer = temp/len(arr)
#     return answer

# def solution(arr):
#     answer = sum(arr)/len(arr)
#     return answer
# solution([1,2,3,4])