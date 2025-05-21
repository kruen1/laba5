def array_converter(array_numbers):
    new_array_numbers = []
    for i in array_numbers:
        if i > 0:
            new_array_numbers.append(i)
        else:
            i = i + (i * (-2))
            new_array_numbers.append(i)
    return new_array_numbers
array = [1, -5, 0, 3, -4]
result = array_converter(array)
print(result)