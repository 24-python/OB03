class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass


class Bird(Animal):
    def __init__(self, name, age, fly):
        super().__init__(name, age)
        self.fly = fly  # Летает

    def make_sound(self):
        return "Чирик"


class Mammal(Animal):
    def __init__(self, name, age, runs):
        super().__init__(name, age)
        self.runs = runs  # Бегает

    def make_sound(self):
        return "Ррррррр"


class Reptile(Animal):
    def __init__(self, name, age, crawls):
        super().__init__(name, age)
        self.crawls = crawls  # Ползает

    def make_sound(self):
        return "Шшшшшшш"


#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных
# и вызывает метод `make_sound()` для каждого животного.

def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} издает звук: {animal.make_sound()}")


# Создадим несколько объектов различных животных
bird = Bird("Воробей", 2, True)
mammal = Mammal("Лев", 5, True)
reptile = Reptile("Змея", 3, True)

# Список животных
animals = [bird, mammal, reptile]

# Вызовем функцию, чтобы продемонстрировать полиморфизм
animal_sound(animals)
