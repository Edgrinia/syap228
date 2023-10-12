my_list = []
n = int(input("Введите количество элементов в списке: "))

for i in range(n):
    while True:
        try:
            element = int(input("Введите элемент: "))
            my_list.append(element)
            break
        except ValueError:
            print("ОШИБКА введите целое число.")

min_even = float('inf')
first_element = None

for element in my_list:
    if element == 0:
        continue

    if element % 2 == 0:
        min_even = min(min_even, element)

    if first_element is None:
        first_element = element

if min_even != float('inf'):
    print("Наименьший четный элемент:", min_even)
else:
    print("Наименьший четный элемент не найден, выводим первый элемент:", first_element)

my_list.sort(key=lambda x: (x != 0, x))

print("Преобразованный список:", my_list)
