import decimal
import random


def random_list(size):
    result = []
    for i in range(size):
        result.append(decimal.Decimal(random.randrange(100, 999)) / 100)
    return result


def diff_after_point(array):
    if len(array) < 2:
        return 0
    min_ap = 1
    max_ap = 0
    for i in array:
        if i % 1 > max_ap:
            max_ap = i % 1
        else:
            if i % 1 < min_ap:
                min_ap = i % 1
    return max_ap - min_ap


def main():
    try:
        size = int(input('Введите целое положительное число - размер массива: '))
        if size < 1:
            print('Вы ввели не положительное число.')
        else:
            array = random_list(size)
            print(f'{array} -> {diff_after_point(array)}')
    except ValueError:
        print('Вы ввели не целое число.')


if __name__ == '__main__':
    main()
