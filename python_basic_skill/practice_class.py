class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        #super().__init__()#super를 이용하면 FlyableUnit의 다중상속중 첫번째 받는 클래스 Flyable만 상속받아서 출력한다.
        Unit.__init__(self)#그래서 각자 출력시켜야 다중상속이 가능
        Flyable.__init__(self)
# 드랍쉽
dropship = FlyableUnit()
