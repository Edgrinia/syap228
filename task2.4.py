def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
        return None
    finally:
        print("Блок finally выполнен независимо от того, было ли исключение или нет.")


try:
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))

    result = divide(a, b)
    if result is not None:
        print("Результат деления:", result)

except ValueError:
    print("Ошибка вводи числа.")

except Exception as e:
    print("Произошла ошибка:", str(e))
