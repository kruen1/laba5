import random

def generate_sorted_evens(length, min_val=0, max_val=100):

    evens = []
    while len(evens) < length:
        num = random.randint(min_val, max_val)
        if num % 2 == 0:  # Проверка на чётность
            evens.append(num)
    evens.sort()  # Сортировка массива
    return evens

random_evens = generate_sorted_evens(10)
print(f"Случайный массив чётных чисел (отсортированный): {random_evens}")