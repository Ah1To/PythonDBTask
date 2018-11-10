import random

def reversPrint(revList):
    if(type(revList) != list): return print("Entered object, not list")
    i = len(revList) - 1
    while i > 0:
        print(revList[i], end=" ")
        i -= 1


NumList = []

while True:
    rand_number = random.randint(-100, 100)
    NumList.append(rand_number)
    if rand_number == -42 : break
    if len(NumList) > 99 : break

reversPrint(NumList)

