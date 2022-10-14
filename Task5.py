import random


def shuffle_matrix(matrix):
    width = len(matrix[0])
    total_amount_of_nums = width * len(matrix)
    for i in range(total_amount_of_nums // 2 - 1 + total_amount_of_nums % 2):
        rand = random.randint(i + 1, total_amount_of_nums - 1 - i)
        temp = matrix[i // width][i % width]
        matrix[i // width][i % width] = matrix[rand // width][rand % width]
        matrix[rand // width][rand % width] = temp

        rand = random.randint(i + 1, total_amount_of_nums - i - 2)
        temp = matrix[(total_amount_of_nums - 1 - i) // width][(total_amount_of_nums - 1 - i) % width]
        matrix[(total_amount_of_nums - 1 - i) // width][(total_amount_of_nums - 1 - i) % width] = \
            matrix[rand // width][rand % width]
        matrix[rand // width][rand % width] = temp

    if total_amount_of_nums % 2 == 0:
        temp = matrix[(total_amount_of_nums // 2 - 1) // width][(total_amount_of_nums // 2 - 1) % width]
        matrix[(total_amount_of_nums // 2 - 1) // width][(total_amount_of_nums // 2 - 1) % width] = \
            matrix[(total_amount_of_nums // 2) // width][(total_amount_of_nums // 2) % width]
        matrix[(total_amount_of_nums // 2) // width][(total_amount_of_nums // 2) % width] = temp


def print_matrix(matrix):
    for i in matrix:
        for j in range(len(i) - 1):
            print(i[j], end=' ')
        print(i[len(i) - 1])


def unique_random_matrix(rows, cols):
    result = [[0 for i in range(cols)] for i in range(rows)]
    used = set({})
    for i in range(rows):
        for j in range(cols):
            rand = random.randint(100, 999)
            while rand in used:
                rand = random.randint(100, 999)
            used.add(rand)
            result[i][j] = rand
    return result


def main():
    try:
        rows = int(input('Введите количество строк матрицы (целое положительное число): '))
        cols = int(input('Введите количетсво столбцов матрицы (целое положительное число): '))
        if rows < 1 or cols < 1:
            print('Размеры матрицы должны быть положительными, вы ввели что-то другое.')
        else:
            matrix = unique_random_matrix(rows, cols)
            print_matrix(matrix)
            print()
            shuffle_matrix(matrix)
            print_matrix(matrix)
    except ValueError:
        print('Размеры матрицы - целые числа, вы ввели что-то другое.')


if __name__ == '__main__':
    main()
