def square(m):
    return (m * m)


m = int(input("Сторона квадрата = "))

print(f'Площадь квадрата = {square(m)}')

square(m)
#

from math import ceil


def square(m):
    return ceil(m * m)


m = float(input("Сторона квадрата = "))

print(f'Площадь квадрата = {square(m)}')
