import random

# Створення двовимірного масиву 3x3
matrix = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]

print("Масив:")
for row in matrix:
    print(row)

# Сума всіх елементів
total_sum = sum(sum(row) for row in matrix)
print("\nСума всіх елементів:", total_sum)

# Пошук max, min та їх індексів
max_value = matrix[0][0]
min_value = matrix[0][0]
max_index = (0, 0)
min_index = (0, 0)

for i in range(3):
    for j in range(3):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_index = (i, j)
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
            min_index = (i, j)

print("\nМаксимальне значення:", max_value, "Індекс:", max_index)
print("Мінімальне значення:", min_value, "Індекс:", min_index)

# Сортування кожного рядка
sorted_matrix = [sorted(row) for row in matrix]

print("\nВідсортований масив по рядках:")
for row in sorted_matrix:
    print(row)