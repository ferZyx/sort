import random


def sort_1(sort_1_array):
    not_sorted = True
    j = 0
    while not_sorted:
        not_sorted = False
        for i in range(n - j - 1):
            if sort_1_array[i] > sort_1_array[i + 1]:
                sort_1_array[i], sort_1_array[i + 1] = sort_1_array[i + 1], sort_1_array[i]
                not_sorted = True
        j += 1
    return sort_1_array


if __name__ == '__main__':
    array = []
    n = int(input('Введите размер массива: '))
    for i in range(n):
        array.append(random.randint(1, 20))
    sort_pickem = int(input('Для пузырьковой сортивровки введите 1:'))
    if sort_pickem == 1:
        print(sort_1(array))
