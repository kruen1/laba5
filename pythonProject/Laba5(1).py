import random

numbers = [random.randint(0, 10) for _ in range(15)]
print(numbers)
userStartNumber = int(input("Введите начало диапазона (всего чисел 15) -> "))
userEndNumber = int(input("Введите конец диапазона (всего чисел 15) -> "))

sum = 0
num = 1
for i in range(userStartNumber, userEndNumber):
    sum += numbers[i]
    print(f"Число №{num} -> {numbers[i]}")
    num += 1
print(f"Сумма чисел, в выбранном вами диапазоне -> {sum}")