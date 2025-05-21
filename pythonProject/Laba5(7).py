try:
    def point_belonging(x, y, r):
        coordinate_point = x ** 2 + y ** 2
        radius = r ** 2

        if coordinate_point > radius:
            return "❌ Точка не принадлежит окружности."
        elif coordinate_point == radius:
            return "⭕️ Точка лежит на окружности."
        else:
            return "✅ Точка принадлежит окружности."


    print("Введите координаты точки и радиус в формате -> X Y R (через пробел):")
    x, y, r = map(int, input().split())

    result = point_belonging(x, y, r)
    print(result)

except ValueError:
    print("Ошибка! Введите три числа через пробел.")