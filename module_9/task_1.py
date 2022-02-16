print("Step 5")

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(",")

print("Step 6")

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print("w")

print("Step 7")

s = input()
for c in range(0, len(s), 2):
    print(s[c])


print("Step 8")

s = input()
for c in range(1, len(s) + 1):
    print(s[-c])

print("Step 9")

name = input()
surname = input()
last_name = input()

print(f"{surname[0]}{name[0]}{last_name[0]}")

print("Step 10")

a = input()
s = 0
for i in a:
    s += int(i)
print(s)

print("Step 11")

s = input()
flag = False
for i in s:
    if i.isdigit() == True:
        flag = True

if flag:
    print("Цифра")
else:
    print("Цифр нет")

print("Step 12")

a = input()
star = 0
plus = 0
for i in a:
    if i == '*':
        star += 1
    elif i == '+':
        plus += 1
print('Символ + встречается', plus, 'раз')
print('Символ * встречается', star, 'раз')

print("Step 13")

s, count = input(), 0
for i in range(1, len(s)):
    count += s[i] == s[i-1]
print(count)

print("Step 14")

s = input().lower()
print('Количество гласных букв равно', sum(1 for _ in s if _ in 'ауоыиэяюёе'))
print('Количество согласных букв равно', sum(1 for _ in s if _ in 'бвгджзйклмнпрстфхцчшщ'))

print("Step 15")

n = int(input())  # число
d = ''            # строка
while n > 0:
    d = str(n % 2) + d
    n //= 2
print(d)


