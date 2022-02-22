print("1")
print([i for i in range(1, int(input()) + 1)])

print("2")
n = int(input())
s = ''
for i in range(n):
    s += chr(97 + i)
print(list(s))