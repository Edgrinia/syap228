def sum_columns(matrix):
    try:
        m = len(matrix)
        n = len(matrix[0])

        column_sums = [0] * n

        for i in range(m):
            for j in range(n):
                try:
                    element = float(matrix[i][j])
                except ValueError:
                    raise ValueError("Некорректный элемент в матрице: {}".format(matrix[i][j]))

                column_sums[j] += element

        return column_sums

    except Exception as e:
        return str(e)

def input_matrix():
    m = int(input("Введите количество строк в матрице: "))
    n = int(input("Введите количество столбцов в матрице: "))

    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            element = input("Введите элемент [{}][{}]: ".format(i, j))
            row.append(element)
        matrix.append(row)

    return matrix

try:
    matrix = input_matrix()
    print("Матрица:")
    for row in matrix:
        print(row)

    column_sums = sum_columns(matrix)
    print("Суммы каждого столбца:", column_sums)

except Exception as e:
    print("Произошла ошибка:", str(e))
