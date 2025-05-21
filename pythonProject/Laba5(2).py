import random


def calculate_stats(numbers):
    # Сумма положительных элементов
    sum_positives = sum(num for num in numbers if num > 0)

    min_val = min(numbers)
    max_val = max(numbers)
    # Находим индексы минимального и максимального элементов
    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))

    # Определяем границы для среза
    start = min(min_index, max_index)
    end = max(min_index, max_index)

    # Вычисляем произведение между min и max
    product = 1
    for num in numbers[start + 1:end]:
        product *= num

    between_elements = numbers[start + 1:end]

    print("             ===ИТОГОВЫЙ РЕЗУЛЬТАТ===")
    print("-" * 50)
    print(f"Исходный массив: {numbers}")
    print(f"Сумма положительных элементов: {sum_positives}")
    print(f"Минимальный элемент: {min_val} (на позиции {min_index})")
    print(f"Максимальный элемент: {max_val} (на позиции {max_index})")
    print(f"Элементы между ними: {between_elements}")
    print(f"Произведение этих элементов: {product}")
    print("-" * 50)

    return (sum_positives, product)


numbers = [random.randint(-10, 10) for _ in range(15)]
calculate_stats(numbers)