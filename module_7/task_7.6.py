# Наименьший делитель

n, div = int(input()), 2
while n % div:
    div += 1
print(div)

print("-" * 30)

# Следуй правилам

n = int(input())
for i in range(1, n + 1):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i)
