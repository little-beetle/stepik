import math

# Евклидово расстояние

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

print(math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2)))

print("-" * 30)

# Площадь и длина

r = float(input())
print(math.pi * pow(r, 2))
print(2 * math.pi * r)

print("-" * 30)

# Средние значения

import math

a = float(input())
b = float(input())
print((a + b) / 2)
print(math.sqrt(a * b))
print((2 * a * b) / (a + b))
print(math.sqrt((math.pow(a, 2) + math.pow(b, 2)) / 2))

print("-" * 30)

# Тригонометрическое выражение

x = math.radians(float(input()))
print(math.sin(x) + math.cos(x) + math.tan(x) ** 2)

print("-" * 30)

# Пол и потолок

a = float(input())
print(math.ceil(a) + math.floor(a))

print("-" * 30)

# Квадратное уравнение 🌶️🌶️

a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c

if d < 0:
    print('Нет корней')
elif d == 0:
    print(-b / (2 * a))
elif d > 0:
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))

print("-" * 30)

# Правильный многоугольник

n = float(input())
a = float(input())
print((n * a ** 2) / (4 * math.tan(math.pi / n)))