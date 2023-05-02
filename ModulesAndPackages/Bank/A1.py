import services
from config import data

global total
total = 0
print("Welcome to the Bank!!")
print("press 1 tp create a bank acc")
t = int(input())
if t == 1:
    data.total = 0
    print("Account created successfully")
    while True:
        print("Please opt for the services you want to perform")

        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Done with transactions")

        n = int(input("Enter your choice: "))

        if n == 1:
            i = int(input("Enter amt : "))
            services.addMoney(i)
        elif n == 2:
            i = int(input("Enter amt : "))
            services.withdrawMoney(i)
        elif n == 3:
            services.getBalance()
        elif n == 4:
            break
        else:
            print("Enter a valid choice")
else:
    print("Thank you")
