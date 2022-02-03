# Напишите программу, которая выводит текст:

print('"Python is a great language!", said Fred. "I don\'t ever remember having this much fun before."')

print("-" * 30)

# Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:
#
# «Hello [введенное имя] [введенная фамилия]! You just delved into Python».

name = input()
surname = input()
print(f"Hello {name} {surname}! You just delved into Python")

print("-" * 30)

# Футбольная команда

name = input()
print(f"Футбольная команда {name} имеет длину {len(name)} символов")

print("-" * 30)

# Три города

name_1 = input()
name_2 = input()
name_3 = input()

print(min(name_1, name_2, name_3, key=len ))
print(max(name_1, name_2, name_3, key=len ))

print("-" * 30)

# Арифметические строки

a, b, c = len(input()), len(input()), len(input())
if a + b + c == (min(a, b, c) + max(a, b, c))/2*3:
    print("YES")
else:
    print("NO")

print("-" * 30)

# Цвет настроения синий

print('YES' if 'синий' in input() else 'NO')

print("-" * 30)

# Отдыхаем ли?

s = input()
print('YES' if 'суббота' in s or 'воскресенье' in s else 'NO')

print("-" * 30)

# Корректный email

email = input()
print('YES' if all(_ in email for _ in ('@', '.')) else 'NO')


