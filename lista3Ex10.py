import math

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

delta = b * b - 4 * a * c

if delta < 0:
    print("Impossível resolver a equanção!")
else:
    x_1 = (-b - math.sqrt(delta)) / (2 * a)
    x_2 = (-b + math.sqrt(delta)) / (2 * a)

    print("x1: ", x_1)
    print("x2: ", x_2)
