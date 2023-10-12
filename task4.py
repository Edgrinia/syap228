string = input('Введите строку: ')

char_count = {}

for char in string:
    try:

        if char.isalpha():
            char = char.lower()
            char_count[char] = char_count.get(char, 0) + 1
    except TypeError:
        pass

print(char_count)
