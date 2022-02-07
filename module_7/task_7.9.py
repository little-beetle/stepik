# Численный треугольник 3

p = 0
n = int(input())
for i in range(n):
    for j in range(i + 1):
        print(p+1, end=' ')
        p+=1
    print()

print("-" * 30)

# Численный треугольник 4

n = int(input())
for i in range(1, n + 1):
    for j in range(1, 2 * i):
        print(min(j, 2 * i - j), end='')
    print()

print("-" * 30)

# Делители-1 🌶️

a , b = int(input()), int(input())
total_maximum = 0
digit = 0

for i in range(a, b + 1):
    maximum = 0
    for j in range(1, i + 1):
        if i % j == 0:
            maximum += j
        if maximum >= total_maximum:
            total_maximum = maximum
            digit = j
print(digit, total_maximum)

print("-" * 30)

# Делители-2

n = int(input())
for i in range(1, n + 1):
    print(i, end = '')
    for j in range(1, i+1):
        if i % j == 0:
            print('+', end = '')
    print()

print("-" * 30)

# Цифровой корень

n = int(input())
while n // 10 > 0:
    n = n // 10 + n % 10
print(n)

print("-" * 30)

# Сумма факториалов

import math
summa = 0
num = int(input())
for i in range(1, num + 1):
    summa += math.factorial(i)
print(summa)

print("-" * 30)

# Простые числа

a, b, = int(input()), int(input())
for i in range(a, b + 1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)

print("-" * 30)

