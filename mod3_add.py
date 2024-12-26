def calculate_structure_sum(data_structure) :
    structure_sum = 0
    for structure_object in data_structure :
        if isinstance(structure_object, int) :
            structure_sum = structure_sum + float(structure_object)
        elif isinstance(structure_object, float) :
            structure_sum = structure_sum + structure_object
        elif isinstance(structure_object, str) :
            structure_sum = structure_sum + float(len(structure_object))
        elif isinstance(structure_object, bool) :
            structure_sum = structure_sum + float(int(structure_object))
        elif isinstance(structure_object, tuple) :
            structure_sum = structure_sum + calculate_structure_sum(structure_object)
        elif isinstance(structure_object, list) :
            structure_sum = structure_sum + calculate_structure_sum(structure_object)
        elif isinstance(structure_object, set) :
            structure_sum = structure_sum + calculate_structure_sum(structure_object)
        elif isinstance(structure_object, dict) :
            structure_sum = structure_sum + calculate_structure_sum(structure_object.keys()) + calculate_structure_sum(structure_object.values())
    return  structure_sum

data_structure_1 = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure_1)
print(result)
