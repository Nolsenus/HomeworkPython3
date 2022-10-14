import random


def random_list(size):
    result = []
    for i in range(size):
        result.append(random.randint(1, 9))
    return result


def sum_of_odd_indexes(array):
    result = 0
    for i in range(1, len(array), 2):
        result += array[i]
    return result


def main():
    try:
        size = int(input('Введите целое положительное число - размер списка: '))
        if size < 1:
            print('Вы ввели не положительное число.')
        else:
            array = random_list(size)
            print(f'{array} -> {sum_of_odd_indexes(array)}')
    except ValueError:
        print('Вы ввели не целое число.')


if __name__ == '__main__':
    main()
