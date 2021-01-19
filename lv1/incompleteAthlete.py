# https://programmers.co.kr/learn/courses/30/lessons/42576
"""
완주하지 못한 선수
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다
"""
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for idx, p in enumerate(participant):
#         if idx + 1 == len(participant):
#             answer = p
#             break
#         if p != completion[idx]:
#             answer = p
#             break
#     return answer

# import collections
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        # 해쉬함수로 가져온 값을 주소로 해서 그 주소에 part값을 넣는다.
        temp += int(hash(part))
        # 주소값(idx)를 전부 더한다.
        # 1,4,12,33 이라고 한다면 60
    for com in completion:
        temp -= hash(com)
        # com값의 해쉬값(key가 같으니깐 같은 문자열이면 해쉬값이 같다)을 이전에 주소값 더한 temp에 하나씩 뺀다.
        # 60 - 1 -4 -12 = 33
        # 남은값의 주소 33, 나머지 값들을 전부 빼기때문에 남는 주소값이 하나 없는 주소값인것
    answer = dic[temp]
    return answer

solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])