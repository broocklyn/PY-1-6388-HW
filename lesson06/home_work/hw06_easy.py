
__author__ = 'Учускин Павел Валерьевич'


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

from math import sqrt


class Rectangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.ab = 0
        self.bc = 0
        self.ac = 0
        self.p = 0
        self.h = 0

    def perimeter(self):
        self.ab = sqrt((self.b[0] - self.a[0]) ** 2 + (self.b[1] - self.a[1]) ** 2)
        self.bc = sqrt((self.c[0] - self.b[0]) ** 2 + (self.c[1] - self.b[1]) ** 2)
        self.ac = sqrt((self.c[0] - self.a[0]) ** 2 + (self.c[1] - self.a[1]) ** 2)
        return round(self.ab + self.bc + self.ac, 3)

    def height(self):
        self.p = (self.ab + self.bc + self.ac) * 1 / 2
        self.h = 2 * sqrt(self.p * (self.p - self.ab) * (self.p - self.bc) * (self.p - self.ac)) / self.ab
        return round(self.h, 2)

    def square(self):
        square = (self.ab * self.h) / 2
        return square


rect1 = Rectangle([1, 3], [8, 7], [2, 9])

print(f"Периметр треугольника равен: {rect1.perimeter()}")
print(f"Высота треугольника равна: {rect1.height()}")
print(f"Площадь треугольника равна: {rect1.square()}")
print("---------------------------------")

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Ravine_Trapezium:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.a = sqrt((self.x1-self.x4)**2 + (self.y1-self.y4)**2)
        self.b = sqrt((self.x3-self.x2)**2 + (self.y3-self.y2)**2)
        self.H = sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2)
        self.h = sqrt((self.x4-self.x3)**2 + (self.y4-self.y3)**2)
    def is_ravine(self):
        if self.a != self.b:
            return "Трапеция не равнобочная"
        else:
            return "Трапеция равнобочная"
    def l_s(self):
        return self.H, self.b, self.h, self.a
    def S(self):
        return (self.a + self.b) * abs(self.y4 - self.y1) / 2
Trap1 = Ravine_Trapezium(1,1,5,1,4,4,2,4)
print(Trap1.is_ravine())
print(Trap1.l_s())
print(Trap1.S())
