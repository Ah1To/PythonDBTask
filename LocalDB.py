#Импортируем модуль random для генерации рандомных чисел
import random

#обьявляю метод для вывода списка в обратном порядке
def reversPrint(revList):
    if(type(revList) != list): return print("Entered object, not list")
    i = len(revList) - 1
    while i > 0:
        print(revList[i], end=" ")
        i -= 1

#создаю массив который будет заполнен введенными данными
NumList = []

#запускаю цикл дял генерации чисел и запись их в массив 
while True:
    rand_number = random.randint(-100, 100)
    #добавление рандомного числе в конец списка(массива)
    NumList.append(rand_number)
    #создание условий выхода из цикла соответствующие нуждам задачи
    if rand_number == -42 : break
    if len(NumList) > 99 : break
#вывод списка в обратном порядке
reversPrint(NumList)

