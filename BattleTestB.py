# надо сделать таймаут
# надо сделать таблицу СДЕЛЯЛ
# таблицу надо положить в файл. СДЕЛЯЛ
# надо придумать, чтобы по мере уменьшения power уменьшался урон

from random import randint
import numpy


class Voin():
    health = 100
    score = 0
    power = 100

    def kick(self):
        score += 1


invite = "Удар рукой - 2, удар ногой - 3, блок - 1: "
VoinUser = Voin()
VoinPC = Voin()


def printStats():
    print("Здоровье / Сила: ", VoinUser.health, " / ", VoinUser.power, "  ", VoinPC.health, " / ", VoinPC.power)


with open("battle.txt", 'r') as f:  # тут читаем файл, делаем матрицу
    l = [i.strip("\n").split() for i in f.readlines()]
x = 4
y = 4
results = (numpy.matrix(l)[:x, :y])
print(results)


def battle():
    while ((VoinUser.health > 0) & (VoinPC.health > 0)):
        choise = int(input(invite))
        choisePC = randint(1, 3)
        # 0 без выбора, 1 блок, 2 рука, 3 нога
        # блок лучше руки, рука лучше ноги, нога лучше блока
        if results[choisePC, choise] == '0':
            printStats()

        elif results[choisePC, choise] == '1':
            VoinUser.power -= 5
            VoinPC.health -= 10
            printStats()
        elif results[choisePC, choise] == '-1':
            VoinUser.health -= 10
            VoinPC.power -= 5
            printStats()
        elif results[choisePC, choise] == '2':
            VoinPC.health -= 10
            VoinUser.health -= 10
            printStats()
    if(VoinUser.health == 0):
        print("Комп победил")
    else:
        print("ты победил")

battle()
