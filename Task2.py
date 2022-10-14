import random


def random_list(size):
    result = []
    for i in range(size):
        result.append(random.randint(1, 9))
    return result


def mult_pairs(array):
    result = []
    for i in range(len(array) // 2 + len(array) % 2):
        result.append(array[i] * array[len(array) - 1 - i])
    return result


def main():
    try:
        size = int(input('Введите целое положительное число - размер массива: '))
        if size < 1:
            print('Размер массива должен быть положительным, вы ввели не положительное число.')
        else:
            array = random_list(size)
            print(f'{array} -> {mult_pairs(array)}')
    except ValueError:
        print('Размер массива должен быть целым числом, вы ввели не целое число.')


if __name__ == '__main__':
    main()
