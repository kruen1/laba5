class Animal(object):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Я мутант")

class Cat(Animal):
    def speak(self):
        print("МЯУУ")

class Dog(Animal):
    def speak(self):
        print("ГАВВ")

cat = Cat("Cat")
cat.speak()
dog = Dog("Dog")
dog.speak()