#####################################################
# practice_quiz.py(quiz8~10)
# 클래스
# 상속
# 다중 상속
# 연산자 오버로딩
# pass
# super
# 예외처리
# 에러 발생시키기
# 사용자 정의 예외처리
# finally
# 모듈
# 패키지
# __all__
# pip install
# 내장 함수
# 외장 함수
#####################################################
# 클래스
# 상속
# 다중 상속
# 연산자 오버로딩(자식클래스에서 사용한 매소드를 부모클래스에서 재정의 하여 사용할 수 있음)
# pass
# super 추가설명 practice_class.py 참조
# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(\
#         name, location, damage))

# # 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        # __init__ 생성자
        self.name = name# 멤버변수, 클래스안에서만 사용하는
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다,".format(name))
        print("체력 {0}".format(hp))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다. ".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
""" marine1 = Unit("마린",40,5)
marine2 = Unit("마린",40,5)
tank = Unit("탱크",150,35)

wraith1 = Unit("레이스", 80, 5)
print("레이스 체력 {0}, 레이스 공격력 {1}\n".format(wraith1.hp,wraith1.damage))

wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True # wraith2에만 clocking변수가 만들어진 상태

if wraith2.clocking == True :
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name)) """

# # 공격유닛
class AttackUnit(Unit):#Unit클래스 상속
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.name = name
        self.hp = hp
        self.speed = speed
        self.damage = damage
        print("공격력 {0}".format(damage))
    def attack(self, location):
        print("{0} : {1} 방향으로 적국을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

# #firebat
# firebat1 = AttackUnit("파이어뱃", 50, 2, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

# # 공중유닛
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):# 다중상속
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) #지상 speed 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):# 연산자 오버로딩
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# """ # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.move( "3시")

# # 벌처 : 지상유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)
# # 배틀크루저 : 공중유닛, 체력,공격력좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name,"9시")
# battlecruiser.move("9시") """

# # 건물
# """ class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass#pass 아무것도 안하고 그냥 넘어가는 것 """

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0) #super self를 안넣는다.
#         self.location = location

# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

#####################################################
# 예외처리
# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)

#####################################################
# 에러 발생시키기
# 사용자 정의 예외처리
# finally
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")

#####################################################
# 모듈
# theater_module.py참조
# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price_soldier as price_s
# price_s(6)

#####################################################
# 패키지
# travel  -   __init__.py
#         -   thailand.py
#         -   vietnam.py
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


#####################################################
# __all__
# from travel import *
# #trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()#__init__.py에서 등록이 안되있기때문에 에러 발생
# trip_to.detail()

#####################################################
# 패키지, 모듈 위치
# from travel import *
# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

#####################################################
# pip install
""" search google 'pypi'
typing pip install ~ 
pip list                            현재설치된 패키지 버전확인
pip show beautifulsoup              해당 패키지 정보확인
pip install --upgrade beautifulsoup 해당 패키지 버전 업그레이드
pip uninstall beautifulsoup         해당 패키지 삭제
"""

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

#####################################################
# 내장 함수
# input : 사용자 입력을 받는 함수
# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random
# print(dir())
# import pickle
# print(dir())
# print(dir(random))

# lst = [1,2,3]
# print(dir(lst)) #lst에 사용할 수있는 내장함수출력
# name = "Jim"
# print(dir(name)) #str에 사용할 수있는 내장함수출력

#####################################################
# 외장 함수
# list of python builtins(구글에 외장 함수 검색)
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) #확장자가 py 인 모든 파일 출력
 
# # os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())#현재 디렉토리 출력

# folder = "sample_dir"

# if os.path.exists(folder):
#    print("이미 존재하는 폴더입니다.")
#    os.rmdir(folder)
#    print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)#폴더생성
#     print(folder, "폴더를 생성하였습니다.") 

# import time#시간 관련 함수
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 ", datetime.date.today())

# #timedelta : 두 날짜 사이의 간격
# today = datetime.date.today()
# td = datetime.timedelta(days = 100)
# print("우리가 만난지 100일은", today + td)

#####################################################
