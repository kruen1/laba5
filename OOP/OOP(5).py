class KgToPounds():
    def __init__(self, kg = 1):
        self.__kg = kg

    def converter(self):
        pounds = self.__kg * 2.2
        return pounds

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, kg_amount):
        try:
            if kg_amount < 0:
                raise ValueError
        except ValueError:
            print("Значение не может быть меньше 0.")
        else:
            self.__kg = kg_amount

test = KgToPounds()
test.kg = 5
print(f"{test.kg} кг -> {test.converter()} фунтов")