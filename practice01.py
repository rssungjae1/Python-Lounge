#####################################################
#practice_quiz.py(quiz1~4)
# 정수 출력
# 문자열 출력
# Boolean 출력
# 변수
# 연산자
# 랜덤함수
# 문자함수
# 문자열 슬라이싱
# 문자열 처리함수
# 문자열 포맷
# 탈출문자
# list []
# dictionary
# tuple
# set
# the change of datatype
#####################################################
# # 정수 출력
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(3*(3+1))

#####################################################
# # 문자열 출력
# print('풍선')
# print('나비')
# print('ㅋ'*9)

#####################################################
# # Boolean 출력
# print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not (5<10))

#####################################################
# # 변수
# # 애완동물을 소개
# animal = "puppuy"
# name = "Tommy"
# age = 4
# hobby = "take a walk"
# is_adult = age >= 3

# print("my " + animal + " is " + name)
# print(name + " is " + str(age) + "years old, and he loves "+ hobby)
# print(name + " is old dog? " + str(is_adult))

#####################################################
# # 연산자
# print(abs(5)) # 5
# print(pow(4,2)) # 4^2 =16
# print(max(5,12)) # 5
# print(round(3.14),1) # 3

# from math import *
# print(floor(-4.99))
# print(trunc(-4.99))

#####################################################
# # 랜덤함수
# from random import *
# print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random()*10) # 0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random()*10)) # 0 ~ 10 미만의 임의의 값 생성
# print(int(random()*10)+1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random()*45)+1) # 1 ~ 45 이하의 임의의 값 생성(로또)
# print(randint(1,46)) # 1 ~ 45 이하의 임의의 값 생성(로또)

#####################################################
# # 문자함수
# sentence = "나는 소년입니다"
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬이 쉬워요
# """
# print(sentence3)

#####################################################
# # 문자열 슬라이싱
# jumin = "990120-1234567"
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) #0부터 2직전까지의 범위
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6])
# print("뒤 7자리 : " + jumin[7:])
# print("뒤 7자리 : " + jumin[-7:])

#####################################################
# # 문자열 처리함수
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python","Java"))

# index = python.index("n")#첫번째 n 자리 찾기
# print(index)
# index = python.index("n",index + 1)#두번째 n 자리 찾기
# print(index)

# print(python.find("Java")) #없으면 -1 반환
# # print(python.index("Java")) #없으면 바로 에러발생하여 다음 처리에 문제가 생길 수 있다.
# print(python.count("n"))

#####################################################
# # 문자열 포맷
# #방법1
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요" % "파이썬")
# print("나는 %s과 %s를 좋아해요" % ("파이썬","자바"))
# #방법2
# print("나는 {}살입니다." .format(20))
# print("나는 {0}과 {1}를 좋아해요" .format("파이썬","자바"))
# print("나는 {1}과 {0}를 좋아해요" .format("파이썬","자바"))
# #방법3
# print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color="red"))
# #방법4(v3.6 이상)
# age = 28
# color = "red"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

#####################################################
# # 탈출 문자
# #\n line change
# print("백문이 불여일견\n백견이 불여일타")
# #quotes in sentence
# print("i am 'nadocoding'")
# print('i am "nadocoding"')
# print("i am \"nadocoding\"")
# #\\ \ in sentence
# print("C:\\Users\\rssun\\Desktop\\PythonWorkspace")
# #\r move cusur infront of sentence
# print("Red Apples\rPine") #Pine Apples
# #\b backspace
# print("Redd\bApple")
# #\t tab
# print("Red\tApple")

#####################################################
# # list []
# #['Tom', 'George', 'Dan']
# subway =["Tom","George","Dan"]
# print(subway.index("George"))
# #['Tom', 'George', 'Dan', 'Haha']
# subway.append("Haha")
# print(subway)
# #['Tom', 'George', 'Dan', 'Haha']
# subway.insert(1, "Joe")
# print(subway)

# print(subway.pop())
# print(subway)
# print(subway.count("Tom"))

# num_list = [5,3,1,2,4,1]
# num_list.sort() #.reverse() .clear()
# print(num_list)
# mix_list=["Tom", 20, True]
# num_list.extend(mix_list)
# print(num_list)

#####################################################
# # dictionary
# # {key_num:user}
# cabinet = {3:"Tombson", 100:"Harry"}
# print(cabinet[3])
# print(cabinet.get(100))

# #print(cabinet[5]) #Error, there is not exist key about "5"
# print(cabinet.get(5)) #not Error, result "None"
# print(cabinet.get(5,"there is not key")) #not Error, result "there is not key"

# print(3 in cabinet) #True
# print(5 in cabinet) #False

# del cabinet[3]
# print(cabinet)
# print(cabinet.keys()) #cabinet.calues() cabinet.items()

#####################################################
# # tuple
# # the same list, but cant revise, more fast than list
# menu = ("donnkatsu","cheese katsu")
# print(menu[0])
# #menu.add("fish katsu") #cant use add

#####################################################
# # set
# # cant duplicate, order
# my_set= {1,2,3,3,3}
# print(my_set)
# java ={"Tom","Marry"}
# python = set(["Tom","Cheese"])
# #can java also python
# print(java & python)
# print(java.intersection(python))
# #can java or python
# print(java | python)
# print(java.union(python))
# #can java but cant python
# print(java - python)
# print(java.difference(python))
# #can java.add("") or java.remove("")

#####################################################
# # the change of datatype
# menu = {"coffee","milk","juice"}
# print(menu,type(menu))
# menu = list(menu)
# print(menu,type(menu))
# menu = tuple(menu)
# print(menu,type(menu))
# menu = set(menu)

#####################################################


