print("1")
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(59)

print("2")
print(71)

print("3")
print(primes[:6])

print("4")
numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]

print(min(numbers) + max(numbers))

print("5")
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
average = sum(evens)/len(evens)
print(average)

print("6")
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[rainbow.index('Green')] = 'Зеленый'
rainbow[rainbow.index('Violet')] = 'Фиолетовый'
print(rainbow)

print("7")
languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
print(languages[::-1])

print("8")
numbers1 = [1, 2, 3] * 2
numbers2 = [6] * 9
numbers3 = [7, 8, 9, 10, 11, 12, 13]

print(numbers1 + numbers2 + numbers3)
