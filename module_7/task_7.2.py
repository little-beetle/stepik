# Последовательность чисел 1

for i in range(int(input()), int(input()) + 1):
    print(i)

print("-" * 30)

# Последовательность чисел 2 🌶️

n, m = int(input()), int(input())

if n < m:
    for i in range(n, m + 1):
        print(i)
else:
    for i in range(n, m - 1, -1):
        print(i)

print("-" * 30)

# Последовательность чисел 3 🌶️

m, n = int(input()), int(input())

start = ((m - 1) // 2) * 2 + 1

for i in range(start, n - 1, -2):
    print(i)

print("-" * 30)

# Последовательность чисел 4

m, n = int(input()), int(input())
for i in range(m, n + 1):
    if i % 17 == 0 or i % 10 == 9 or i % 15 == 0:
        print(i)

print("-" * 30)


a = int(input())

for i in range(1, 11):
    print(f"{a} x {i} = {i*a}")
