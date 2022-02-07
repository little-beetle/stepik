# Обратный порядок 1

num = int(input())
while num != 0:
    print(num % 10)
    num //= 10

print("-" * 30)

# Обратный порядок 2

n = int(input())
while n != 0:
    print(n % 10, end = '')
    n = n // 10

print("-" * 30)

# max и min

x = str(input())
print('Максимальная цифра равна', max(x))
print('Минимальная цифра равна', min(x))

print("-" * 30)

# Все вместе

num = int(input())
number = num
num_sum = 0
mult = 1

while num != 0:
    last_digit = num % 10
    num_sum += last_digit
    mult *= last_digit
    num = num // 10

print(num_sum)
print(len(str(number)))
print(mult)
print(num_sum / len(str(number)))
print(last_digit)
print(last_digit + number % 10)

print("-" * 30)

# Вторая цифра

n = int(input())
while n > 99:
    n //= 10
print(n % 10)

print("-" * 30)

# Одинаковые цифры

n = int(input())
m = n % 10
answer = 'YES'
while n != 0:
    if m != n % 10:
        answer = 'NO'
    n = n // 10
print(answer)

print("-" * 30)

# Упорядоченные цифры 🌶️

n,b = int(input()),'YES'
while n // 10 != 0 :
    a = n % 10
    n = n // 10
    if a > n % 10:
        b = 'NO'
print(b)
