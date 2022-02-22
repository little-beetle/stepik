print(1)
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
if 5 in numbers and 17 in numbers:
    print('YES')
else:
    print('NO')
del numbers[0]
del numbers[-1]
print(numbers)

print(2)
n = int(input())
l = []
for i in range(n):
    s = input()
    l.append(s)
print(l)

print(3)
l = []
for i in range(ord('z') - ord('a') + 1):
    l.append(chr(ord('a') + i) * (i + 1))
print(l)

print(4)
ls = [int(input()) ** 3 for i in range(int(input()))]
print(ls)

print(5)
n = int(input())
print([i for i in range(1, n // 2 + 1) if n % i == 0] + [n])

print(6)
n, a = int(input()), int(input())
lst = []
for _ in range(n-1):
    b = int(input())
    lst.append(a + b)
    a = b
print(lst)

print(7)
n=int(input())
b=[]
for i in range(n):
    a=int(input())
    b.append(a)
del b[1::2]
print(b)

print(8)
n = int(input())
li = []
for _ in range(n):
    li.append(input())
index = int(input())
res = ''
for s in li:
    if len(s) >= index:
        res += s[index - 1]

print(res)

print(9)
n = int(input())
sp = []
for _ in range(n):
    sp.extend(input())
print(sp)