print("hello world")

import os
def showDir(path):
    for (dirpath, dirnames, filenames) in os.walk(path):
        for dirname in dirnames:
            print(os.path.join(dirpath,dirname))
        for filename in filenames:
            print(os.path.join(dirpath,filename))
print(os.getcwd())
search_path ='C:\\Users\\rssun\\Desktop\\PythonWorkspace\\python_basic_skill'
showDir(search_path)


""" 
리스트(list)
셋은 순서가 없는 중복이 불가능한 collection 자료형이다. -> 내장모듈 collections 알아두면 좋음
mutable(가변성) 함
요소들 간의 순서가 없음 -> 따라서, indexing이 불가 -> not iterable
중복제거 교집합, 합집합, 차집합 등의 수학적인 계산이 가능
셋은 add(요소 1개 추가), update(여러요소 추가), remove 메소드를 활용하여 요소를 추가/삭제한다.
합집합은 a | b로 표현, 차집합은 a - b로 표현, 교집합은 a & b로 표현 
"""