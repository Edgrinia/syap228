print("Введите элементы первого кортежа, разделяя их пробелами:")
input_str = input()
tuple1 = tuple(input_str.split())

print("Введите элементы второго кортежа, разделяя их пробелами:")
input_str = input()
tuple2 = tuple(input_str.split())

tuple3 = tuple1 + tuple2
print("Третий кортеж, объединяя элементы из первого и второго кортежей:", tuple3)
