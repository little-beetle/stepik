# Заглавные буквы

name = input()

if name == name.title():
    print("YES")
else:
    print("NO")

print("-" * 30)

# sWAP cASE

print(input().swapcase())

print("-" * 30)

# Хороший оттенок

if "хорош" in input().lower():
    print("YES")
else:
    print("NO")

print("-" * 30)

# Нижний регистр

word = input()
count = 0
for i in range(len(word)):
    if word[i].islower():
        count += 1

print(count)