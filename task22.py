input_text = input("Введите строку с текстом в скобках: ")
output_text = ""

inside_brackets = False

for char in input_text:
    if char == '(':
        inside_brackets = True
    elif char == ')':
        inside_brackets = False
    elif not inside_brackets:
        try:
            int(char)
        except ValueError:
            output_text += char

print("Результат после удаления текста в скобках и чисел:", output_text)
