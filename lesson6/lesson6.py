# first =  int(input("Enter first"))
# second =  int(input("Enter second"))
#
# if second != 0:
#     print(first/second)
# else:
#     print("Division by zero")
#
#
#
# colors = ["red", "pink", "black"]
#
# index =  int(input("Enter index"))
#
# if index <= len(colors)-1:
#     print(colors[index])
# else:
#     print("Out of colors len")


print(f"NameError = {type(NameError)} - {issubclass(NameError, BaseException)}")



try:
    first =  int(input("Enter first "))
    second =  int(input("Enter second "))
    print(first/second)
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Value error - enter only numbers!!!")
finally:
    print("Finally 1")


colors = ["red", "pink", "black"]

try:
    index =  int(input("Enter index "))
    print(colors[index])
except IndexError:
    print("Out of colors len")
except ValueError:
    print("Value error - enter only numbers!!!")
finally:
    print("Finally 2")



try:
    turtle
except (IndexError, NameError) as error:
    print(error)
finally:
    print("Finally 3")


print("The End")

#Створіть класс Студент по прикладу уроку2.
#Зробіть обробку вийнятків при вводі даних студента