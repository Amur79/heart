def task1(x, y):
    """ Вычислить гипотенузу прямоугольного треугольника. Катеты вводит пользователь. """
    # x = float(input("Введите катет 1: "))  # просим пользователя ввести катеты
    # y = float(input("Введите катет 2: "))
    q = x ** 2 + y ** 2  # вычисляем квадрат гипотенузы по суммам квадратов катетов

    return(q ** .5)  # вычисляем квадратный корень и выводим результат


def task2():
    """Вычисление корней квадратного уравнения """
    a = float(input("Введите a: "))  # Запрашиваем коэффициенты
    b = float(input("Введите b: "))
    c = float(input("Введите c: "))

    D = b ** 2 - 4 * a * c  # Вычисляем дискриминант квадратного уравнения

    if D < 0:    # Если D < 0, то корней нет
        print("Дискриминант < 0")
        print("Корней нет")

    elif D == 0:  # Если D = 0, то корень 1
        x = (-b + D ** .5) / (2 * a)

        print("Дискриминант = ", D)
        print("Корень один: ", x)

    else:  # Если D > 0, то 2 корня
        x1 = (-b + D ** .5) / (2 * a)
        x2 = (-b - D ** .5) / (2 * a)

        print("Дискриминант > 0", D)
        print("Есть 2 корня: ")
        print("Корень 1 =  ", x1)
        print("Корень 2 =  ", x2)


def task3():
    """Вывод таблицы умножения """
    M = int(input("Введите число M: "))  # Запрашиваем у пользователя значения

    a = int(input("Введите диапазон a: "))
    b = int(input("Введите диапазон b: "))

    if a <= 0 and b <= 0:     # Выполняем проверки
        print("Ошибка! a и b должны быть > 0!")

    elif b <= a:
        print("Неверный диапазон! b должно быть больше a!")

    else:
        print("Результат:")

        for a in range(a - 1, b):  # Выводим результат циклом
            a += 1
            print(M, "x", a, "=", M * a)


def task4():
    """Проверка является ли число n простым """
    n = int(input("Введите число n: "))

    for a in range(2, n):
        if (n % a) == 0:
            print("Число ", n, "не простое")
            break
        elif (n // a) == 1:
            print("Число ", n, " простое!")
            break


def task5():
    """Вывод простых чисел в диапазоне d """
    d = int(input("Введите диапазон: "))

    print("1")
    print("2")

    for n in range(2, d + 1):
        for a in range(2, n):
            if (n % a) == 0:
                break
        else:
            print(n)



def task6():
    """Високосный год """
    frm = int(input("Введите год от: "))
    to = int(input("Введите год до: "))

    if frm >= to or frm == 0:
        print("Неверный диапазон!")
        exit()

    for year in range(frm, to + 1):
        if year % 4 == 0:
            print(year)
            year += 1


def task7():
    """Площадь, периметр и диагональ квадрата """
    sd = int(input("Введите сторону квадрата: "))
    print("Периметр - ", 4 * sd)
    print("Площадь - ", sd ** 2)
    print("Диагональ - ", (2 * sd ** 2) ** .5)


def task8():
    """Простейший калькулятор на Python """
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
    c = input("Введите операцию: ")
    if c == "+":
        print(a + b)

    elif c == "-":
        print(a - b)

    elif c == "*":
        print(a * b)

    elif c == "/":
        print(a / b)

    else:
        print("Неизвестная операция!")


def task9():
    """Времена года """
    m = int(input("Введите номер месяца: "))

    if m == 12 or m == 1 or m == 2:
        print("Это зима")

    elif m == 3 or m == 4 or m == 5:
        print("Это весна")

    elif m == 6 or m == 7 or m == 8:
        print("Это лето")

    elif m == 9 or m == 10 or m == 11:
        print("Это осень")

    elif m == 0 or m > 12:
        print("Нет такого месяца!")


def task10():
    """Простой калькулятор банковского вклада """
    sum = float(input("Введите сумму вклада: "))
    years = int(input("На сколько лет: "))

    for i in range(years):
        sum = sum * 1.1

    print(sum)


def task11():
    import random
    """Заполнение списка случайными числами и сортировка """
    n1 = int(input("Введите нижний диапазон: "))
    n2 = int(input("Введите верхний диапазон: "))
    k = int(input("Введите количество элементов: "))

    sp = []

    for i in range(k):
        sp.append(random.randrange(n1, n2))

    print("Вывод списка: ")
    print(sp)

    sp.sort()
    print("Элементы отсортированы по возрастанию: ")
    print(sp)

    sp.sort(reverse=True)
    print("Элементы отсортированы по убыванию: ")
    print(sp)


def task12():
    """Сортировка пузырьком на Python """
    lst = [4, 23, 6, 2, 12, 100, 9]

    j = 0

    print(lst)
    print("Сортировка...")
    for j in range(len(lst)):

        for i in range(len(lst) - 1):

            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]  # меняем местами

            i += 1

    print(lst)


def task13():
    """Самое длинное слово в предложении """
    s = input("Введите ваш текст: ")

    w = max(s.split(), key=len)

    print("Самое длинное слово в предложении: ", w)