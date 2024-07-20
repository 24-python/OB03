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


# Функция для демонстрации полиморфизма
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


# Использование композиции для создания класса Zoo
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(f"Зоопарк: {self.name}\n")
            file.write("Животные в зоопарке:\n")
            for animal in self.animals:
                file.write(f"- {animal.name}, возраст {animal.age}, звук: {animal.make_sound()}\n")
            file.write("Сотрудники зоопарка:\n")
            for employee in self.employees:
                file.write(f"- {employee.name}, должность {employee.position}, зарплата {employee.salary}\n")


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary


class ZooKeeper(Employee):
    def __init__(self, name, position, salary):
        super().__init__(name, position, salary)

    def feed_animal(self):
        pass


class Veterinarian(Employee):
    def __init__(self, name, position, salary):
        super().__init__(name, position, salary)

    def heal_animal(self):
        pass


# Создадим зоопарк и добавим животных и сотрудников
zoo = Zoo("Городской зоопарк")
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zoo_keeper = ZooKeeper("Иван", "Смотритель", 30000)
veterinarian = Veterinarian("Анна", "Ветеринар", 50000)

zoo.add_employee(zoo_keeper)
zoo.add_employee(veterinarian)

# Теперь у нас есть зоопарк с животными и сотрудниками
print(f"Зоопарк: {zoo.name}")
print("Животные в зоопарке:")
for animal in zoo.animals:
    print(f"- {animal.name}, возраст {animal.age}")

print("Сотрудники зоопарка:")
for employee in zoo.employees:
    print(f"- {employee.name}, должность {employee.position}, зарплата {employee.salary}")

# Сохранение информации о зоопарке в файл
zoo.save_to_file('zoo_info.txt')
