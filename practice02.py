#####################################################
# practice_quiz.py(quiz5~7)
# if
# for
# while
# continue, break
# one line for
# function
# function2
# global variable/local variable
# sep
# 표준 입출력
# ljust, rjust
# 다양한 출력포맷
# 파일 입출력
# pickle
# with
#####################################################
# # if
# weather = input("how about weather? today?") #micro dust, sunny, rain
# if weather == "rain" or weather == "snow":
#     print("get your umbrella")
# elif weather == "micro dust":
#     print("get yout mask")
# else:
#      print("negative needs")

#####################################################
# # for
# for wating_no in range(1, 6): #1,2,3,4,5
#     print("wating no : {0}" .format(wating_no))

# starbucks = ["ironman","thor","grut"]
# for customer in starbucks:
#     print("{0}, ready to coffe." .format(customer))

####################################################
# # while
# customer = "thor"
# index = 5
# while index >= 1:
#     print("{0}, ready to coffe. {1} count left" .format(customer, index))
#     index -= 1
#     if index == 0:
#         print("the coffee is over")
# # roof
# customer = "ironman"
# index = 1
# while True:
#     print("{0}, ready to coffe. {1} count" .format(customer, index))
#     index += 1

# customer = "thor"
# person = "Unknown"

# while person != customer :
#     print("{0}, ready to coffe." .format(customer))
#     person = input("what is your name?")

#####################################################
# # continue, break
# absent = [2,5]
# no_book = [7]
# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("class is over, {0} follow the my room" .format(student))
#         break
#     print("{0}, read the book" .format(student))

#####################################################
# # one line for
# students = list(range(1,6))
# print(students)
# students = [i+100 for i in students]
# print(students)

# students = ["ironman","thor","groot"]
# students = [len(i) for i in students]
# print(students)

# students = ["ironman","thor","groot"]
# students = [i.upper() for i in students]
# print(students)

#####################################################
# # function
# def open_account():
#     print("the new account is availed")

# def deposit(balance, money):
#     print("deposit is completed. the balance is {0}" .format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("withdraw is completed. the balance is {0}" .format(balance - money))
#         return balance - money
#     else:
#         print("withdraw isn't completed. the balance is {0}" .format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     print("withdraw is completed. the night commission is {0}. the balance is {1}" .format(commission, balance - money - commission))
#     return commission, balance - money - commission

# balance = 0
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 1100)
# commission, balance = withdraw_night(balance, 500)

#####################################################
# # function2
# def profile(name, age=17, main_lang="Python"):#default data
#     print("name:{0}\t age:{1}\t main lang:{2}"\
#         .format(name, age, main_lang))

# profile("Tom", "20", "Python") 
# profile("Sam", "25", "Java")
# profile("Renny")

# def profile(name, age=17, main_lang="Python"):#default data
#     print("name:{0}\t age:{1}\t main lang:{2}"\
#         .format(name, age, main_lang))

# profile(name = "Tom", main_lang= "Python", age="20") #the procedure is not order

# def profile(name, age, lang1, lang2, lang3, lang4):
#     print("name:{0}\t age:{1}\t " .format(name, age), end=" ")#, end=" " means stay the result line
#     print(lang1, lang2, lang3, lang4)
# def profile(name, age, *language):
#     print("name:{0}\t age:{1}\t " .format(name, age), end=" ")#, end=" " means stay the result line
#     for lang in language:
#         print(lang, end="")
#     print()
# def profile2(name, age, language2):
#     print("name:{0}\t age:{1}\t " .format(name, age), end=" ")#, end=" " means stay the result line
#     for lang in language2:
#         print(lang, end=" ")
#     print()
#
# profile2("Tom", 20, {"Python", "C", "C#", "C++"})
# profile("Sam", 22, "Python", "C", "C#", "C++")

#####################################################
# # global variable/local variable
# gun = 10
# def checkpoint(soldiers):
#     global gun
#     #gun = 20
#     gun = gun - soldiers
#     print("inside of function's gun : {0}".format(gun))

# print("all gun : {0}".format(gun))
# checkpoint(2)
# print("all gun : {0}".format(gun))

#####################################################
# # sep
# print("Python","Java", "JavaScript", sep=", ", end="?") #seperate
# print("Which one is most interst?")

#####################################################
# # 표준 입출력
# import sys
# print("Python","Java", "JavaScript", file=sys.stdout)
# print("Python","Java", "JavaScript", file=sys.stderr)

#####################################################
# # ljust, rjust
# scores={"math":0,"english":50,"coding":100}
# for subject, score in scores.items():
#     #print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# for num in range(1,21):
#     print("waiting num : "+str(num).zfill(3))

# answer = input("input : ")
# print(type(answer))
# print("the input data is {0}" .format(answer))
#####################################################
# # 다양한 출력포맷
# # 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10 자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸은 _로 채움
# print("{0:_<+10}".format(500))
# # 3자리 마다 콤마 찍어주기
# print("{0:+,}".format(10000000000))
# print("{0:+,}".format(-10000000000))
# # 3자리 마다 콤마를 찍어주고, 부호붙이고, 자릿수 확보하기(빈자리는 ^로 채우기)
# print("{0:^<+30,}".format(10000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수 까지만 표시
# print("{0:.2f}".format(5/3))

#####################################################
# # 파일 입출력
# # w덮어쓰기
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close() 

# # a열어서편집하기
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# # r읽어오기
# score_file = open("score.txt", "r", encoding="utf8")

# # 한번에 다 읽어오기
# print(score_file.read()) 

# # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") 
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())

# # 줄 수를 모를경우, 반복문
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)

# # list형태로 저장해서 출력
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close() 

#####################################################
# # pickle
# # 프로그램 상의 데이터를 파일형태로 저장하는 것
# import pickle

# profile_file = open("profile.pickle","wb") #b는 바이너리
# profile={"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle","rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

#####################################################
# # with
# # close를 딱히 안해도된다는 간편함
# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")
    
# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

#####################################################


