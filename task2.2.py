def process_input(data):
    try:
        if isinstance(data, set):
            return sum(data)
        elif isinstance(data, list):
            negatives = [x for x in data if x < 0]
            if len(negatives) >= 2:
                return negatives[0] * negatives[1]
            else:
                return "Недостаточно отрицательных элементов в списке."

        elif isinstance(data, int):
            return sum(int(digit) for digit in str(abs(data)))

        elif isinstance(data, str):
            words = data.split()
            longest_word = max(words, key=len)
            return longest_word

        else:
            return "Неизвестный тип данных."

    except TypeError:
        return "Не удалось обработать входные данные."

try:
    user_input = eval(input("Введите данные (может быть множество, список, число или строка): "))
    result = process_input(user_input)
    print("Результат обработки:", result)

except Exception as e:
    print("Произошла ошибка:", str(e))
