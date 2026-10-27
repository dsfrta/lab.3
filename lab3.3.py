from math import *
print("Ряд Тейлора для Arcth x,Область сходимости")
x_beg = float(input("Введите Xначальное: "))
x_end = float(input("Введите Xконечное: "))
dx = float(input("Введите шаг dx: "))
eps = float(input("Введите точность епс: "))

print("+------------+------------+------------+")
print("|     X      |     Y      | Кол-во (n) |")
print("+------------+------------+------------+")

x = x_beg
while x <= x_end:
    if abs(x) <= 1:
        print("| {0:10.2f} |   Ошибка   |     0      |".format(x))
        print("|            |  (|x|<=1)  |            |")
    else:
        n = 0
        a_n = 1.0 / x
        y = a_n
        count = 1
        while True:
            k = ((2 * n + 1) / (2 * n + 3)) * (1.0 / (x * x))
            a_n = a_n * k
            y = y + a_n
            n = n + 1
            count = count + 1
            if abs(a_n) < eps:
                break
        print("| {0:10.2f} | {1:10.5f} | {2:10d} |".format(x, y, count))
    x = x + dx

print("+------------+------------+------------+")