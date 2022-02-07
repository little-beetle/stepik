# Python is awesome

for _ in range(10):
    print("Python is awesome!")

print("-" * 30)

# Повторяй за мной 1

text = input()
num = int(input())
for _ in range(num):
    print(text)

print("-" * 30)

# Последовательность символов

for _ in range(6):
    print("AAA")

for _ in range(5):
    print("BBBB")

print("E")

for _ in range(9):
    print("TTTTT")

print("G")

print("-" * 30)

# Звездный прямоугольник

for _ in range(int(input())):
    print("*" * 19)

print("-" * 30)

# Повторяй за мной 2

text = input()

for i in range(10):
    print(f"{i} {text}")

print("-" * 30)

# Квадрат числа

for i in range(int(input()) + 1):
    print(f"Квадрат числа {i} равен {i ** 2}")

print("-" * 30)

# Звездный треугольник

for i in range(int(input()), 0, -1):
    print("*" * i)

print("-" * 30)

# Популяция

m, p, n = float(input()), float(input()), int(input())
[print(i + 1, m * (1 + p / 100) ** (i)) for i in range(n)]

print("-" * 30)

