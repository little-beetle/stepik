import math

# Количество чисел

a = int(input())
b = int(input())
count = 0
for i in range(a, b + 1):
    if i % 10 == 4 or i % 10 == 9:
        count += 1
print(count)

print("*" * 30)

# Сумма чисел

a = int(input())
s = 0
for i in range(a):
    s += int(input())
print(s)

print("*" * 30)

# Асимптотическое приближение

count = 0
num = int(input())
for i in range(1, num + 1):
    count += 1 / i
print(count - math.log(num))


print("*" * 30)

# Сумма чисел

num = int(input())
count = 0
for i in range(1, num + 1):
    if (i ** 2) % 10 == 2 or (i ** 2) % 10 == 5 or (i ** 2) % 10 == 8:
        count += i

print(count)

print("*" * 30)

# Факториал

print(math.factorial(int(input())))

print("*" * 30)

# Без нулей

p = 1
for _ in range(10):
    n = int(input())
    p *= n + (n == 0)
print(p)

print("*" * 30)

# Сумма делителей

n = int(input())
s = 0
r = int(math.sqrt(n))
for i in range(1, r + 1):
    if n % i == 0:
        s += i
        s += n // i
if n / r == r:
    s -= r

print(s)

print("*" * 30)

# Знакочередующаяся сумма

n = int(input())

if (n % 2 == 0):
    print(-n // 2)
else:
    print(n // 2 + 1)

print("*" * 30)

# Наибольшие числа 🌶️🌶️

n = int(input())

max1, max2 = -1, -1

for _ in range(n):
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num

print(max1)
print(max2)

print("*" * 30)

# Only even numbers 🌶️

flag = 'YES'
for _ in range(10):
    a = int(input())
    if a % 2 != 0:
        flag = 'NO'
print(flag)

print("*" * 30)

# Последовательность Фибоначчи 🌶️

n = int(input())
a, b = 1, 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b

print("*" * 30)

