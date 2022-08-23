#Hometask_13_1
def sum_num(data):
    """
    Суммирует цифры из целого десятичного числа,
    создает список из сум цифр,
    сортирует элементы нового списка
    :param data: список целых чисел
    :return: список отсортированных сумм цифр из data
    """

    new_list = []
    for n in data:
        summ = 0
        while n != 0:
            last = n % 10
            summ += last
            n = n // 10
        new_list.append(summ)
    new_list.sort()
    return new_list

num_list = [int(i) for i in input().split()]
print(sum_num(num_list))

#Hometask_13_2
#def f_x(x):
#    """
#    Фычисляет значение функции
#    :param x: значение аргумента функции
#    :return: значение функции
#    """
#    if x <= -2:
#        y = 1 - (x + 2)**2
#    elif x > -2 and x <= 2:
#        y = -x/2
#    else:
#        y = 1 + (x - 2)**2
#    return y

#print(f_x(float(input("Ведите значение аргумента:"))))

#Hometask_13_3

#def conv_list(data):
#    """
#    принимает на вход список целых чисел, удаляет из него
#    все нечётные значения, а чётные нацело делит на два
#    :param data: список целых чисел
#    :return: список четных целых чисел из data целочисленно деленных на 2
#    """
#    new_list = []
#    for n in data:
#        if n % 2 == 0:
#            new_list.append(n // 2)
#    return new_list

#print(conv_list([int(i) for i in input().split()]))