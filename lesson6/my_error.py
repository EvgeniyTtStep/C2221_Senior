class MyError(Exception):
    def __str__(self):
        return f"Hello it is my error"


def check_code(num, value):
    if num > value:
        return "Check ok"
    else:
        raise MyError(num)


print(check_code(10, 15))


