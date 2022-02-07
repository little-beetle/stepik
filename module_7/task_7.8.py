# Таблица-1

n = int(input())
for i in range(n):
    print(n, n, n)

print("-" * 30)

# Таблица-2

for i in range(1, int(input()) + 1):
    for _ in range(5):
        print(i, "", end='')
    print()

print("-" * 30)

# Таблица-3

num = int(input())
for i in range(1, num + 1):
    for  j in range(1, 10):
        print(f"{i} + {j} = {j + i}")
    print()

print("-" * 30)

# Звездный треугольник 🌶️🌶️

n = int(input())
for i in range(1, n + 1):
    print('*' * min(i, n - i + 1))

print("-" * 30)

# Численный треугольник 1

num = int(input())
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(i, end = "")
    print()

