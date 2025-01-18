
class Student:
    student_count = 0
    def __init__(self, height, age, phone=111):
        self.height = height
        self.age = age
        self.phone = phone
        print("I am student constructor")
        Student.student_count +=1

    def grow(self, height):
        self.height += height

    def __del__(self):
        print("Жалко цього добряка")



angelina = Student(165, 14) #1
glib = Student(172, 13, 777) #2
jack = Student(180, 12, 555) #3

jack.grow(5)
glib.grow(10)

print("Height = ", angelina.height, angelina.phone, angelina.student_count)
print("Height = ", glib.height, glib.phone, glib.student_count)
print("Height = ", jack.height, jack.phone, jack.student_count)