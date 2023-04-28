class ListOperations:
    def __init__(self) -> None:
        print("You are inside List Operations")
        self.li = []
        print(f"Created an empty list named li -> {self.li}")

    def Append(self, i):
        self.li.append(i)
        print(f"Element {i} added to the list")

    def Delete(self):
        print("Choose from the options below:")
        print("1. Delete all elemnents from the list")
        print("2. Delete a particular element from the list")
        print("3. Delete element at given index from the list")
        n = int(input())
        if n == 1:
            self.li.clear()
            print("All elements deleted from the list")
        elif n == 2:
            t = int(input("Enter the element you want to delete:   "))
            try:
                self.li.remove(t)
            except ValueError:
                print("Element not found")
        elif n == 3:
            t = int(
                input("Enter the index at which you want to delete the element:   ")
            )
            try:
                self.li.pop(t)
            except IndexError:
                print("Index out of bound")
        else:
            print("Choice invalid!")

    def Display(self):
        print(f"List is: {self.li}")


li = ListOperations()
li.Append(2)
li.Append(12)
li.Append(5)
li.Append(10)
li.Append(11)
li.Append(20)
li.Display()
li.Delete()
li.Display()
li.Delete()
li.Display()
li.Delete()
li.Display()
