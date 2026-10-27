from random import *
R = float(input("Введите радиус R: "))
print("  X        Y      Результат")
print("-----------------------------")

for i in range(10):


    x = uniform(-R, R)
    y = uniform(-R, R)

    popal = False
    if (x >= 0) and (y >= 0) and (x ** 2 + y ** 2 <= R ** 2):
        popal = True
    elif (x <= 0) and (y <= 0) and (x + y >= -R):
        popal = True
    if popal:
        print("{0:7.2f}  {1:7.2f}      Yes (Попадание)".format(x, y))
    else:
        print("{0:7.2f}  {1:7.2f}      No  (Мимо)".format(x, y))