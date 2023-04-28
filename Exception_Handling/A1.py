# TypeError Example
def multiply(a, b):
    try:
        return a * b
    except TypeError as e:
        print(f"Error: {e}")
        return "Error"


print(multiply("b", "a"))


# ValueError Example
try:
    n = int(input("Enter a integer value:  "))
except ValueError as e:
    print(f"Error: {e}")
print("Error handled successfully")


# AttributeError Example
li = [1, 2, 3, 4, 5]
try:
    li.erase()
except AttributeError as e:
    print(f"AttributeError occured: {e}")
print("Error handled successfully")


# ZeroDivisionError Example
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")


a = divide(6, 3)
a = divide(6, 0)


# IndexError example

li = [1, 2, 3, 4, 4, 5]
try:
    print(li[10])
except IndexError as e:
    print(f"Error: {e}")
