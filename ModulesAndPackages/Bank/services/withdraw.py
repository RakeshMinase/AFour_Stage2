from config import data


def withdrawMoney(x):
    if x <= data.total:
        data.total = data.total - x
        print(f"Rs {x} withdrwan from account")
    else:
        print("Insufficient Balance")
    print("-------------------")
    print()
