try:
    number = int(input("Введите натуральное число: "))

    if number < 0:
        print("Вы ввели отрицательное число. Пожалуйста, введите натуральное число.")
    else:
        maxnumber = 0

        while number > 0:
            lastnumber = number % 10
            if lastnumber > maxnumber:
                maxnumber = lastnumber
            number = number // 10

        print("Максимальная цифра в числе:", maxnumber)

except ValueError:
    print("Ошибка: Введено не число.")






