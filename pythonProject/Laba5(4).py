def transform_string(stroka):
    if stroka.startswith('abc'):
        return 'www' + stroka[3:]
    else:
        return stroka + 'zzz'

input_string = input("Введите строку: ")
result = transform_string(input_string)
print("Результат:", result)