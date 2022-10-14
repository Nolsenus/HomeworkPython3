def decimal_to_binary(num):
    result = 0
    power = 1
    while num > 0:
        result += (num % 2) * power
        num //= 2
        power *= 10
    return result


def main():
    try:
        number = int(input('Введите целое неотрицательное число: '))
        if number < 0:
            print('Вы ввели отрицательное число.')
        else:
            print(f'{number} -> {decimal_to_binary(number)}')
    except ValueError:
        print('Вы ввели не целое число.')


if __name__ == '__main__':
    main()
