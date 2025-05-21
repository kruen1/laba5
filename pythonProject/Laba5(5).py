try:
    def calculate_example(a, b):
        return (a + 4*b) * (a - 3 * b) + a * 2
    varA = input("Введите переменную a -> ")
    varB = input("Введите переменную b -> ")
    if "." or "," in varA and varB:
        varA = float(varA.replace(",", "."))
        varB = float(varB.replace(",", "."))
    else:
        varA = int(varA)
        varB = int(varB)
    result = calculate_example(varA, varB)
    print(result)
except ValueError:
    print("\nОшибка!!!\n")
    print("Она может появлять по нескольким причинам:")
    print("    ❌ Вы не ввели одну или две переменные.")
    print("    ❌ Вы ввели буквы вместо цифр.")
    print("    ❌ Вы ввели какие-либо символы, кроме ТОЧКИ или ЗАПЯТОЙ . ")
    print("🔸Для решения проблемы попробуйте ВВЕСТИ нужное вам ЧИСЛО через ЗАПЯТУЮ или ТОЧКУ🔸")