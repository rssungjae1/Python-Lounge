#####################################################
# practice01.py(quiz1~4)
# practice02.py(quiz5~7)
# practice03.py(quiz8~10)
#####################################################
# # quiz1
""" 변수를 이용하여 다음 문장을 출력하시오
변수명 : station
변수값 : "사당", "신도림", "인천공항"
출력문장 : xx 행 열차가 들어오고 있습니다. """
# (코드)
# station = "사당"
# print(station + "행 열차가 들어오고 있습니다.")
# station = "신도림"
# print(station + "행 열차가 들어오고 있습니다.")
# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다.")

#####################################################
# # quiz2
""" 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번으은 오프라인으로 하기로했습니다.
아래 조건에 맞는 오프라인 모임날짜를 정해주는 프로그램을 작성하시오.
조건1 랜덤으로 날짜를 뽑아야 함
조건2 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함
조건3 매월1~3일은 스터디 준비를 해야하므로 제외
출력문장 : 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다. """
# (코드)
# from random import *
# day = int(random()*25+4)
# date = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(day) + "일로 선정되었습니다.")

#####################################################
# # quiz3
""" 사이트별로 비밀번호를 만들어주는 프로그램 작성
예)http://naver.com
규칙1 http:// 부분은 제외 => naver.com
규칙2 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
예)생성된 비밀번호 nav51! """
# (코드)
# url = "http://naver.com"
# url2 = "http://google.com"
# my_str = url.replace("http://","")
# my_str = my_str[:my_str.index(".")]
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0} `s password is {1}" .format(url,password))

#####################################################
# # quiz4
""" 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.
조건1 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
조건2 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 random 모듈의 shuffle과 sample을 활용
출력예제
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2,3,4]
-- 츅하합니다 -- """
# (코드)
# from random import *
# lst = list(range(1,21))
# shuffle(lst)
# winners = sample(lst, 4)

# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {}".format(winners[0]))
# print("커피 당첨자 : {}".format(winners[1:]))
# print("-- 축하 합니다 --")

#####################################################
# # quiz5
""" 50명의 승객과 매칭기회가 있을때, 총 탑승 승객수를 구하는 프로그램을 작성하시오.
조건1 승객별 운행소요 시간은 5~50분 사이의 난수로 정해집니다.
조건2 당신은 소요시간 5~15분 사이의 승객만 매칭해야합니다.
출력예제
[0] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분) 
...
[ ] 50번째 손님 (소요시간 : 16분) 

총 탑승 승객 : 2 분 """
# (코드)
# from random import *
# count = 0
# for guest_no in range(1,51):
#     take_time = int(random()*46+5) #randrange(5,51)
#     if 5 <= take_time <= 15:
#         print("[0] {0}_no guest (taking time : {1})" .format(guest_no,take_time))
#         count += 1
#     else:
#         print("[ ] {0}_no guest (taking time : {1})" .format(guest_no,take_time))
# print("boarding guest no : {0}" .format(count))

#####################################################
# # quiz6
""" 표준 체중 : 각 개인의 키에 적당한 체중
성별에 따른 공식
남자 : 키(m) * 키(m) * 22
여자 : 키(m) * 키(m) * 21
조건1 표준 체중은 별도의 함수 내에서 계산
함수명 std_weight
전달값 height, gender
조건2 표준 체중은 소수점 둘째자리까지 표시
출력예제
키 175cm 남자의 표준 체중은 67.38kg 입니다. """
# (코드)
# from math import *
# def std_weight(height, gender):
#     if gender == "M":
#         std_weight = (height/100)*(height/100)*22
#     elif gender == "W":
#         std_weight = (height/100)*(height/100)*21
#     std_weight = round(std_weight,2)
#     print("the standard weight of {0}cm ({1}) : {2}kg" .format(height,gender,std_weight))
# gender = input("Please typing your gender(M,W)") 
# height = input("Please typing your height(cm)") 
# std_weight(int(height),gender)

#####################################################
# # quiz7
""" 회사에서 매주 1회 작성해야하는 보고서가 있다.
보고서 형태
- X 주차 주간보고 -
부서 :
이름 : 
업무 요약 :

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
조건 : 파일명은 '1주차.txt', '2주차.txt'... 와 같이 만듭니다. """
# (코드)
# for weekno in range(1,51):
#     with open(str(weekno) + "주차.txt", "w", encoding="utf8") as reportfile:
#         reportfile.write("- {0} 주차 주간보고 -".format(weekno))
#         reportfile.write("부서 : ")
#         reportfile.write("이름 : ")
#         reportfile.write("업무 요약 : ")

#####################################################
# # quiz8
# (출력 예제)
""" 총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년 """

# (코드)
# class House:
#     #매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     #매물 정보 표시
#     def show_detail(self):
#         print("{0} {1} {2} {3} {4}년".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))
#         self

# kangnam = House("강남", "아파트", "매매", "10억", 2010)
# mapo = House("마포", "오피스텔", "전세", "5억", 2017)
# soungpa = House("송파", "아파트", "월세", "500/50", 2000)

# House_units = []
# House_units.append(kangnam)
# House_units.append(mapo)
# House_units.append(soungpa)

# House_count = len(House_units)

# print("총 {}대의 매물이 있습니다.".format(str(House_count)))
# for unit in House_units:
#     unit.show_detail()

#####################################################
# # quiz9
""" 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
        출력 메시지 : "잘못된 값을 입력하였습니다."
조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
        치킨소진시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
        출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다." """

# (코드)
# chicken = 10
# waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작

# class SoldOutError(Exception):
#     pass

# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken: # 남은 치킨보다 주문량이 많을때
#             print("재료가 부족합니다. 남은 치킨량 [{0}] 이하로 주문해주십시요.".format(chicken))
#         elif order <= 0:
#             raise ValueError            
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
#                 .format(waiting, order))
#             waiting += 1
#             chicken -= order 

#         if chicken == 0:
#             raise SoldOutError
#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError:
#         print("재료가 소진되어 더 이상 주문을 받지 않습니다.")
#         break
#####################################################
# # quiz10
""" 조건 : 모듈 파일명은 byme.py로 작성
(모듈 사용 예제)
import byme
byme.sign()
(출력 예제)
이 프로그램은 나도코딩에 의해 만들어졌습니다.
유튜브 : http://youtube.com
이메일 : nadocoding@gmail.com """
# byme.py참조
# import byme
# byme.sign()
#####################################################
