print("Введите целое число от 3 до 20: ")
first = int(input())
result = ''
list_ = []
for i in range(1, 20):
    for j in range(2, 20):
        if first % (i + j) == 0 and i != j and ([i, j] and [j, i]) not in list_:
            list_.append([i, j])
            result = result + str(i) + str(j)
        else: continue
print(f'Пароль: {result}')