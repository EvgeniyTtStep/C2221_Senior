import requests
import inspect
import sys

#help()

def my_function():
    pass

class Human:
    pass

rq = requests
mf = my_function
jack = Human

print(requests.__name__)
print(rq.__name__)

print(my_function.__name__)
print(mf.__name__)

print(Human.__name__)
print(jack.__name__)

print(__name__)

auto_list = ["bmw", "mercedes", "zaz"]

auto_list.append("tesla")

print(type(auto_list))
print("=========== dir =============")
for methods in dir(auto_list):
    print(methods)


print("=========== dir =============")

for methods in dir():
    print(methods)

print("=========== attr =============")
data = "hello"
print(hasattr(data, "reverse"))
print(hasattr(data, "index"))

print(getattr(data, "index"))

print("=========== issubclass =============")
class Worker(Human):
    pass

print(issubclass(Worker, Human))

print("=========== isinstance =============")

bob = Worker()

print(isinstance(bob, Human))

print("=========== inspect =============")

print(inspect.isclass(bob))
print(inspect.isclass(Human))

print(inspect.ismodule(rq))
print(inspect.ismodule(requests))

print(inspect.isfunction(my_function()))
print(inspect.isfunction(my_function))

print(inspect.getmodule(requests))

print("=========== inspect sig =============")

class Student:
    def __init__(self, age, height, name="Stuart"):
        self.age = age
        self.height = height
        self.name = name


sig = inspect.signature(Student)

for param in sig.parameters.values():
    print(param.name," : ", param.default)


print("=========== sys =============")

print(sys.executable)
print(sys.version)
print(sys.platform)
print(sys.argv)

#print(sys.modules.items())

#for module_name, module_path in sys.modules.items():
#   print(module_name, module_path)

print("=========== builtins =============")

for item in dir(__builtins__):
    print(item)
