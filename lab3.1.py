def print_hi(name):

    print(f'Hi, {name}')
if __name__ == '__main__':
    print_hi('PyCharm')

from math import*
x_1 = float(input("Введите Xначальное(отрицательное): "))
x_2 = float(input("Введите Xконечное: "))
dx = float(input("Введите шаг dx: "))

print("+------------+------------+")
print("|     X      |     Y      |")
print("+------------+------------+")

x = x_1
while x <= x_2:
    if x < -9:
        y = 0
    elif -9 <= x < -5:
        y = 2 - sqrt(4 - (x + 7) ** 2)
    elif -5 <= x < -4:
        y = 2
    elif -4 <= x < 0:
        y = -0.5 * x
    elif 0 <= x < pi:
        y = sin(x)
    else:
        y = x - pi
    print("| {0:10.2f} | {1:10.2f} |".format(x, y))

    x = x + dx

print("+------------+------------+")