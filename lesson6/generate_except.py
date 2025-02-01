def checker(var1):
    if type(var1)!=str:
        raise TypeError(f"I need a str TYPE ok?")
    else:
        return var1


num1 = "Hello ok"

checker(num1)