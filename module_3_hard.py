def calculate_structure_sum(*args):
    global summ
#    args = list(args)
    for index in args:
        if isinstance(index, int):
            summ += index
        elif isinstance(index, str):
            summ += len(index)
        elif isinstance(index, list):
            calculate_structure_sum(*index)
        elif isinstance(index, set):
            calculate_structure_sum(*index)
        elif isinstance(index, tuple):
            calculate_structure_sum(*index)
        elif isinstance(index, dict):
            index = list(index.items())
            calculate_structure_sum(*index)
    return summ

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
summ = 0
result = calculate_structure_sum(*data_structure)
print(result)