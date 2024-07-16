class Teacher():
    def teach(self):
        print("Учитель учит...")

class School():
    def __init__(self, new_teacher):
        self.teacher = new_teacher

    def start_lessone(self):
        self.teacher.teach()


my_teacher = Teacher()
new_school = School(my_teacher)
new_school.start_lessone()
# Агрегация в программировании класс учитель связан с классом школа, но не жестко.