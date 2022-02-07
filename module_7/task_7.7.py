# Ревью кода-1 🌶️🌶️

count = 0
p = 1
for i in range(1, 11):
    x = int(input())
    if x >= 0:
        p = p * x
        count = count + 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')

print("-" * 30)

# Ревью кода-2 🌶️🌶️

mx = -10**6 - 1
s = 0
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
    if x < 0 and x > mx:
        mx = x
if s < 0:
    print(s)
    print(mx)
else:
    print('NO')

print("-" * 30)

# Ревью кода-3

s = 0
for _ in range(7):
    n = int(input())
    if n % 2 == 0:
        s += n
print(s)

print("-" * 30)

# Ревью кода-4 🌶️🌶️

n = int(input())
max_digit = -1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    n = n // 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)

print("-" * 30)

# Ревью кода-5 🌶️

n = int(input())
while n > 9:
    n //= 10
print(n)

print("-" * 30)

# Ревью кода-6

n = int(input())
product = 1
while n > 0:
    digit = n % 10
    product *= digit
    n //= 10
print(product)