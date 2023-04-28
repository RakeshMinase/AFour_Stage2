class StringOperations:
    def __init__(self) -> None:
        print("You are inside StringOperations")
        self.s = str()

    def get_string(self):
        self.s = str(input("Enter a string\n"))
        return self.s

    def print_string(self):
        print(f"The string is {self.s}")

    def print_string_in_uppercase(self, s):
        print(f"The string {s} in uppercase is {s.upper()}")


str_obj = StringOperations()
temp = str_obj.get_string()
str_obj.print_string()
str_obj.print_string_in_uppercase(temp)
