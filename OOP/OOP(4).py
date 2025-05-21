class Soda():
    def __init__(self, supplements):
        self.supplements = supplements

    def show_my_drink(self):
        if self.supplements:
            return f"Газировка и {self.supplements}"
        return "Обычная газировка"


supp = ["ЛИМОН", "ЛЁД", "ТРУБОЧКА"]

cola = Soda(supp[0])
print(cola.show_my_drink())

col = Soda(supp[1])
print(col.show_my_drink())

pepsi = Soda('')
print(pepsi.show_my_drink())