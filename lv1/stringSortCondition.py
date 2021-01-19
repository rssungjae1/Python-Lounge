# https://programmers.co.kr/learn/courses/30/lessons/12915

strings = ["abce", "abcd", "cdx"]
n = 2

def solution(strings, n):
    for i, string in enumerate(strings):
        for s in range(i+1,len(strings)):
            if strings[i][n] > strings[s][n]:
                s1 = strings[i]
                s2 = strings[s]
                strings[i] = s2 
                strings[s] = s1
            elif strings[i][n] == strings[s][n]:
                if strings[i] > strings[s]:
                    s3 = strings[i]
                    s4 = strings[s]
                    strings[i] = s4 
                    strings[s] = s3
    # sorted(strings, key=lambda x: x[n])
    print(sorted(strings, key=lambda x: x[n]))
    return strings

solution(strings, n)