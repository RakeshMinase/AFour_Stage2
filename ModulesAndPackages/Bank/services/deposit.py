from config import data


def addMoney(x):
    data.total = data.total + x
    print(f"Rs {x} added to the account")
    print("-------------------")
    print()
