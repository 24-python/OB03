class Dog:
    def speak(self):
        return "Woff!"
class Cat:
    def speak(self):
        return "Myau!"
def animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_speak(dog)
animal_speak(cat)