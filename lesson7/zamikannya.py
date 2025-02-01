class Helper:
    def __init__(self, work):
        self.work = work

    def __call__(self, work):
        return f"Self work: {self.work}, global work: {work}"

helper = Helper("Homework")
print(helper("Classwork"))


