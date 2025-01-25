class Human:
    age = 18 #public
    _salary = 2000 #protected
    __password = "1234" #private
    def __init__(self, height):
        self.height = height


class Student(Human):
    def __init__(self, hungry, height):
        super().__init__(height)
        self.hungry = hungry


class Worker(Human):
    def __init__(self, hungry, height):
        super().__init__(height)
        self.hungry = hungry


jack = Student(0, 180)
bob = Worker(100, 185)

print(f"Student Jack: {jack.hungry}, {jack.height}, {jack.age}, {jack._salary}")
print(f"Worker Bob: {bob.hungry}, {bob.height}, {bob.age}, {bob._salary}")

