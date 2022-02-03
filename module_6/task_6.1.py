# Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.

a = float(input())
b = float(input())
print(1 / 2 * a * b)

print("-" * 30)

# Две старушки идут навстречу друг другу с постоянными скоростями V_1 V_2  км/ч. Определите,
# через какое время старушки встретятся, если расстояние между ними равно SS км.

s = float(input())
v_1 = float(input())
v_2 = float(input())
print(s / (v_1 + v_2))

print("-" * 30)

# Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему.
# Если при этом введённое с клавиатуры число – ноль, то вывести «Обратного числа не существует» (без кавычек).

num = float(input())
if num != 0:
    print(1 / num)
else:
    print("Обратного числа не существует")

print("-" * 30)

# У известного американского писателя Рэя Бредбери есть роман «451 градус по Фаренгейту».
# Напишите программу, которая определяет, какой температуре по шкале Цельсия соответствует
# указанное значение по шкале Фаренгейта.

temp = float(input())
print(5 / 9 * (temp - 32))

print("-" * 30)

# На вход программе подается число nn – количество собачьих лет. Напишите программу, которая
# вычисляет возраст собаки в человеческих годах.

t = int(input())
print(min(2, t) * 10.5 + max(t - 2, 0) * 4)

print("-" * 30)

# Дано положительное действительное число. Выведите его первую цифру после десятичной точки

num = float(input())
print(int(num * 10) % 10)

print("-" * 30)

# Дано положительное действительное число. Выведите его дробную часть.

num = float(input())
print(num - int(num))

print("-" * 30)

# Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
num_4 = int(input())
num_5 = int(input())

print(f"Наименьшее число = {min(num_1, num_2, num_3, num_4, num_5)}")
print(f"Наибольшее число = {max(num_1, num_2, num_3, num_4, num_5)}")

print("-" * 30)

# Напишите программу, которая упорядочивает три числа от большего к меньшему.

a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c))
print(a + b + c - min(a, b, c) - max(a, b, c))
print(min(a, b, c))

print("-" * 30)

# Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется
# средней по величине цифре. Напишите программу, которая определяет интересное число или нет.
# Если число интересное, следует вывести – «Число интересное» иначе «Число неинтересное».

x = int(input())
a = x % 10
b = x // 10 % 10
c = x // 100
if a + b + c == 2 * max(a, b, c):
    print("Число интересное")
else:
    print("Число неинтересное")

print("-" * 30)

# Абсолютная сумма

num_1 = float(input())
num_2 = float(input())
num_3 = float(input())
num_4 = float(input())
num_5 = float(input())
print(abs(num_1) + abs(num_2) + abs(num_3) + abs(num_4) + abs(num_5))

print("-" * 30)

# Прогуливаясь по Манхэттену, вы не можете попасть из точки А в точку Б по кратчайшему пути.
# Если только вы не умеете проходить сквозь стены, вам обязательно придется идти вдоль
# его параллельно-перпендикулярных улиц.

p1, p2, q1, q2 = [int(input()) for _ in range(4)]
print(abs(p1 - q1) + abs(p2 - q2))

print("-" * 30)
