# Ревью кода - 7 🌶️

n = int(input())
s = 0
while n > 0:
    if n % 2 == 0:
        s += n % 10
    n //= 10
print(s)

print("-" * 30)

# Ревью кода - 8 🌶️

n = 8 # n = 7, по условию чисел 8
count = 0
maximum = -10**6 - 1 # maximum = 1000, все случаи, когда все числа меньше 1000, обрабатываются неверно
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0: # x // 4 == 0, по условию нужно найти числа, дел. на 4 без остатка
        count += 1
        if x > maximum: # if x < maximum, если число больше максимума, оно его заменяет, не если меньше максимума
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

# Ревью кода - 9

count = 0
maximum = -1
for i in range(4):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

print("-" * 30)

# Звездная рамка

n = int(input())
for i in range(1, n + 1):
    if i == 1 or i == n:
        print('*' * 19)
    else:
        print('*' + ' ' * 17 + '*')

print("-" * 30)

# Третья цифра

n = int(input())
while n > 999:
    n //= 10
print(n % 10)

print("-" * 30)

# Все вместе 2

n = int(input())
count3 = 0
countLast = 0
countChet = 0
sumBig5 = 0
multyBig7 = 1
count05 = 0
last = n % 10
while n > 0:
    x = n % 10
    if x == 3:
        count3 += 1
    if x == last:
        countLast += 1
    if x % 2 == 0:
        countChet += 1
    if x > 5:
        sumBig5 += x
    if x > 7:
        multyBig7 *= x
    if x == 0 or x == 5:
        count05 += 1
    n //= 10
print(count3)
print(countLast)
print(countChet)
print(sumBig5)
print(multyBig7)
print(count05)

print("-" * 30)

# Числа Рамануджана 🌶️

b = 1729
x = 0
ss = [b]
while x != 33:
    for x in range(1, 34):
        for y in range(1, 34):
            for z in range(1,34):
                for t in range(1, 34):
                    for r in range(1, 34):
                        if (x**3 + y**3) == (z**3+t**3):
                            if x != y and x != z and x != t and y != z and y != t and z != t:
                                a = (x ** 3 + y ** 3)
                                if a != b:
                                    if a not in ss:
                                        ss.append(a)
                                        ss.sort()
                                        b = a
                                        print(ss)