# Количество слов

s = input()
print(s.count(' ') + 1)

print("-" * 30)

# Минутка генетики

s = input().lower()
print("Аденин:", s.count("а"))
print("Гуанин:", s.count("г"))
print("Цитозин:", s.count("ц"))
print("Тимин:", s.count("т"))

print("-" * 30)
# Очень странные дела

n = int(input())
a = 0
for i in range(n):
    s = input()
    if s.count('11') >= 3:
        a += 1
print(a)

print("-" * 30)
# Количество цифр

s = input()
count = 0
for i in range(len(s)):
    if s[i].isdigit():
        count += 1
print(count)

print("-" * 30)

s = input()
if s.endswith('.com') == True or s.endswith('.ru') == True:
    print('YES')
else:
    print('NO')

print("-" * 30)
# Самый частотный символ

s=input()
c=0
a=0
for i in s:
    if s.count(i)>=c:
        c=s.count(i)
        a=i
print(a)

print("-" * 30)
# Первое и последнее вхождение

s = input()
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))
else:
    print('NO')

print("-" * 30)
# Удаление фрагмента