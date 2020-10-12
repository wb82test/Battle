from random import randint

class Voin():
    health=100
    score=0
    power=100
    def kick(self):
        score+=1
invite="Удар рукой - 2, удар ногой - 3, блок - 1: "
VoinUser=Voin()
VoinPC=Voin()
def printStats():
    print("Здоровье / Сила: ", VoinUser.health," / ",VoinUser.power,"  ",VoinPC.health," / ",VoinPC.power)

def battle():
    while ((VoinUser.health>0) & (VoinPC.health>0)):
        choise=int(input(invite))
        choisePC=randint(1,3)
        # 0 без выбора, 1 блок, 2 рука, 3 нога
        # блок лучше руки, рука лучше ноги, нога лучше блока
        if (choise == 0) & (choisePC == 2): #таймаут, комп бьёт рукой
            VoinUser.health-=10
            VoinPC.power-=5
            print("Вы промедлили, и получили по лицу.. ")
            printStats()
        elif (choise == 1) & (choisePC == 2):#блок против руки
            VoinPC.health-=10
            VoinPC.power-=5
            print("Удачно блокирован удар рукой")
            printStats()
        elif (choise == 1) & (choisePC == 3):#лок против ноги
            VoinPC.power-=5
            VoinUser.health-=10
            print("Блокируешь руки, а тебя с ноги... ")
            printStats()
        elif (choise == 1) & (choisePC == 1):
            print("оба заблокировались. деритесь уже... ")
        elif (choise == 2) & (choisePC == 1):
            VoinUser.health-=10
            VoinUser.power-=5
            printStats()
            print("Хотел с руки и промахнулся")
        elif (choise == 2) & (choisePC == 2):
            VoinUser.health-=10
            VoinUser.power-=5
            VoinPC.health-=10
            VoinPC.power-=5
            print("Одновременно по лицу. Красота")
            printStats()
        elif (choise == 2) & (choisePC == 3):
            VoinUser.power -= 5
            VoinPC.health -= 10
            print("Комп махал ногами, а ты его в бороду. ")
            printStats()

        elif (choise == 3) & (choisePC == 1):
            VoinUser.power-=5
            VoinPC.health-=10
            printStats()
            print("С ноги пробил блок")
        elif (choise == 3) & (choisePC == 2):
            VoinUser.health-=10
            VoinPC.power-=5
            printStats()
            print("Пока замахивался ногой пропустил в бороду")
        elif (choise == 3) & (choisePC == 3):
            VoinUser.health-=10
            VoinUser.power-=5
            VoinPC.health-=10
            VoinPC.power-=5
            printStats()
            print("оба друг друга с ноги. смешно.")

battle()