def calculate_structure_sum(*list_):
    global sum
    for i in range(0, len(list_)):
        if isinstance(list_[i], list) is True:
            calculate_structure_sum(*list_[i])
        elif isinstance(list_[i], tuple) is True:
            calculate_structure_sum(*list_[i])
        elif isinstance(list_[i], set) is True:
            calculate_structure_sum(*list_[i])
        elif isinstance(list_[i], dict) is True:
            for j in range(0, len(list(list_[i]))):
                sum += len((list(list_[i]))[j])
                sum += list(list_[i].values())[j]
        elif isinstance(list_[i], str) is True:
            sum += len(list_[i])
        else:
            sum += list_[i]
            continue
    return (sum)

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
sum = 0
result = calculate_structure_sum(data_structure)
print(result)