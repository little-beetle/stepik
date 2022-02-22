print("1")
s = 'Python rocks!'
print(len(s))

print("2")
s = 'Python rocks!'
print(s[3])

print("3")
s = 'Python rocks!'
print(s[1:5])

print("4")
print('Python rocks!')

print("5")
s = 'Python rocks!'
print(s.upper())

print("6")
print('Pyth@n r@cks!')

print("7")
s = list(input())
del s[0::3]
print(*s, sep='')

print("8")
print(input().replace('1', 'one'))

print("9")
print(input().replace('@', ''))

print("10")
s = input()
if s.count('f')==1:
    print(-1)
elif s.count('f')==0:
    print(-2)
else:
    s = s.replace('f', 'k' , 1)
    print(s.find('f'))

print("11")
s = input()
print(s[:s.find('h')] + s[s.rfind('h'):s.find('h'):-1] + s[s.rfind('h'):])