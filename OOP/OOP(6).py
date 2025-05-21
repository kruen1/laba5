class Nikola():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        if name == "Николай":
            self.name = f"Привет! Я {self.name} и мне {self.age}"
        else:
            self.name = f"Я не {name}, а Николай! Мне {self.age}"


user1 = Nikola("Николай", 34)
print(user1.name)

user2 = Nikola("Олег", 35)
print(user2.name)