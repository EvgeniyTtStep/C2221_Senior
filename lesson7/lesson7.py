print("========= Ітератори ========")

car_list = ["tesla", "toyota", 'nissan']

iterator = iter(car_list)

try:
    print("Next: ", next(iterator))
    print("Next: ", next(iterator))
    print("Next: ", next(iterator))
    print("Next: ", next(iterator))
except StopIteration as e:
    print(e)

print("==============")

for car in iterator:
    print(car)

print("========= Генератори ========")
# генератори  – спеціальні об’єкти, які схожі на ітератор і функцію одночасно.

print("========= Замикання ========")


def helper(work):
    work_memory = work

    def helper(work):
        return f"Memory work: {work_memory}, global work {work}"

    return helper


helper = helper("homework")
print(helper("classwork"))
print(helper("my work"))

print("========= Декоратори ========")

def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as e:
            print(f"Problem: {e}")
        else:
            print(f"No problem, result {result}")
    return checker

@checker
def calc(exp):
    return eval(exp)


# calculate = checker(calc)

calc("9*2")
