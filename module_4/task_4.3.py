# Зум бросил вызов Флэшу и предложил ему честный поединок в виде гонки вокруг магнетара.
# В случае проигрыша эта нейтронная звезда зарядится и уничтожит мир, поэтому Флэш
# решил не рисковать без причины, и узнать у своего друга Циско Рамона есть ли
# смысл принимать вызов. Циско получил данные, что скорость Зума равна nn, а скорость Флэша равна kk.

# Напишите программу, которая должна вывести ответ Циско на вопрос Флэша.

speed_zoom = int(input())
speed_flesh = int(input())

if speed_flesh > speed_zoom:
    print("YES")
elif speed_flesh < speed_zoom:
    print("NO")
else:
    print("Don't know")

print("-" * 30)

# Напишите программу, которая принимает три положительных числа и определяет вид треугольника,
# длины сторон которого равны введенным числам.

side_1 = int(input())
side_2 = int(input())
side_3 = int(input())

if side_1 == side_2 == side_3:
    print("Равносторонний")
elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
    print("Равнобедренный")
else:
    print("Разносторонний")

print("-" * 30)

# Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

if num_2 > num_1 > num_3 or num_3 > num_1 > num_2:
    print(num_1)
elif num_1 > num_2 > num_3 or num_3 > num_2 > num_1:
    print(num_2)
elif num_1 > num_3 > num_2 or num_2 > num_3 > num_1:
    print(num_3)

print("-" * 30)

# Дан порядковый номер месяца (1, \, 2, \ldots, 12)(1,2,…, 12). Напишите программу, которая выводит
# на экран количество дней в этом месяце. Принять, что год является невисокосным.

m = int(input())
if m == 2:
    print('28')
elif m <= 7:
    print(30 + m % 2)
else:
    print(31 - m % 2)

print("-" * 30)

# Известен вес боксера-любителя (целое число). Известно, что вес таков, что боксер может быть отнесён
# к одной из трех весовых категорий:

# Легкий вес – до 60 кг;
# Первый полусредний вес – до 64 кг;
# Полусредний вес – до 69 кг.
# Напишите программу, определяющую, в какой категории будет выступать данный боксер.

weight = int(input())

if weight < 60:
    print("Легкий вес")
elif weight < 64:
    print("Первый полусредний вес")
elif weight < 69:
    print("Полусредний вес")

print("-" * 30)

# Напишите программу, которая считывает с клавиатуры два целых числа и строку. Если эта строка является обозначением
# одной из четырёх математических операций (+, -, *, /), то выведите результат применения этой операции к введённым
# ранее числам, в противном случае выведите «Неверная операция». Если пользователь захочет поделить на ноль,
# выведите текст «На ноль делить нельзя!».

num_1 = int(input())
num_2 = int(input())
action = input()

if action == "+":
    print(num_1 + num_2)
elif action == "-":
    print(num_1 - num_2)
elif action == "*":
    print(num_1 * num_2)
elif action == "/":
    if num_2 == 0:
        print("На ноль делить нельзя!")
    else:
        print(num_1 / num_2)
else:
    print('Неверная операция')

print("-" * 30)

# Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем смешения других цветов.
# При смешивании двух основных цветов получается вторичный цвет:

# если смешать красный и синий, то получится фиолетовый;
# если смешать красный и желтый, то получится оранжевый;
# если смешать синий и желтый, то получится зеленый.
# Напишите программу, которая считывает названия двух основных цветов для смешивания. Если пользователь вводит
# что-нибудь помимо названий «красный», «синий» или «желтый», то программа должна вывести сообщение об ошибке.
# В противном случае программа должна вывести название вторичного цвета, который получится в результате.

color_1 = input()
color_2 = input()

if color_1 == "красный" and color_2 == "красный":
    print("красный")
elif (color_1 == "красный" and color_2 == "синий") or (color_2 == "красный" and color_1 == "синий"):
    print("фиолетовый")
elif (color_1 == "красный" and color_2 == "желтый") or (color_2 == "красный" and color_1 == "желтый"):
    print("оранжевый")
elif color_1 == "желтый" and color_2 == "желтый":
    print("желтый")
elif color_1 == "синий" and color_2 == "синий":
    print("синий")
elif color_1 == "синий" and color_2 == "желтый" or (color_2 == "синий" and color_1 == "желтый"):
    print("зеленый")
elif color_1 == "желтый" and color_2 == "желтый":
    print("желтый")
else:
    print("ошибка цвета")

print("-" * 30)

# На колесе рулетки карманы пронумерованы от 0 до 36. Ниже приведены цвета карманов:

# карман 0 зеленый;
# для карманов с 1 по 10 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
# для карманов с 11 по 18 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный;
# для карманов с 19 по 28 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
# для карманов с 29 по 36 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный.
# Напишите программу, которая считывает номер кармана и показывает, является ли этот карман зеленым, красным или черным.
# Программа должна вывести сообщение об ошибке, если пользователь вводит число, которое лежит вне диапазона от 0 до 36.

print("-" * 30)

# На колесе рулетки карманы пронумерованы от 0 до 36. Ниже приведены цвета карманов:
#
# карман 0 зеленый;
# для карманов с 1 по 10 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
# для карманов с 11 по 18 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный;
# для карманов с 19 по 28 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
# для карманов с 29 по 36 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный.
# Напишите программу, которая считывает номер кармана и показывает, является ли этот карман зеленым, красным или черным.
# Программа должна вывести сообщение об ошибке, если пользователь вводит число, которое лежит вне диапазона от 0 до 36.

n = int(input())

if n < 0 or n > 36:
    print('ошибка ввода')
elif n == 0:
    print('зеленый')
elif 1 <= n <= 10:
    if n % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 11 <= n <= 18:
    if n % 2 == 0:
        print('красный')
    else:
        print('черный')
elif 19 <= n <= 28:
    if n % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 29 <= n <= 36:
    if n % 2 == 0:
        print('красный')
    else:
        print('черный')

print("-" * 30)

# На числовой прямой даны два отрезка: [a_1; b_1][a_2; b_2]

# Напишите программу, которая находит их пересечение.
#
# Пересечением двух отрезков может быть:
#
# отрезок;
# точка;
# пустое множество.

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a2 < a1:
    if b2 < a1:
        print('пустое множество')
    elif b2 == a1:
        print(b2)
    elif a1 < b2 <= b1:
        print(a1, b2)
    elif b2 > b1:
        print(a1, b1)
elif a2 < b1:
    if b2 <= b1:
        print(a2, b2)
    else:
        print(a2, b1)
elif a2 == a1:
    if b2 <= b1:
        print(a2, b2)
    else:
        print(a2, b1)
elif a2 == b1:
    print(a2)
else:
    print('пустое множество')
