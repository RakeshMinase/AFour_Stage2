class American:
    def __init__(self) -> None:
        print("You are inside parent class American")


class NewYorker(American):
    def __init__(self) -> None:
        # super().__init__()
        print("You are inside child class NewYorker")


NewYork_Citizen = NewYorker()
print("---------")
American_Citizen = American()
