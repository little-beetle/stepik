# До КОНЦА 1

a = input()
while (a!='КОНЕЦ'):
    print(a)
    a = input()

print("-" * 30)

# До КОНЦА 2

a = input()
while (a.upper() != 'КОНЕЦ'):
    print(a)
    a = input()

print("-" * 30)

# Количество членов

a, k = input(), 0
while a not in ('стоп', 'хватит', 'достаточно'):
    k += 1
    a = input()
print(k)

print("-" * 30)

# Пока делимся

n = int(input())
while not n % 7:
    print(n)
    n = int(input())

print("-" * 30)

# Сумма чисел

num = int(input())
count = 0
while num >= 0:
    count += num
    num = int(input())
print(count)

print("-" * 30)

# Количество пятерок

n, k = int(input()), 0
while 1 <= n <= 5:
    k += n == 5
    n = int(input())
print(k)

print("-" * 30)

# Ведьмаку заплатите чеканной монетой

n = int(input())
print(n // 25 + n % 25 // 10 + n % 25 % 10 // 5 + n % 5)