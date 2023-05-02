import services

print("You are in Python modules and packages")
print("1. Math")
print("2. Sorting")

c = int(input("Enter the choice of services"))


if c == 1:
    print("1. Roots")
    print("2. Fibonacci series")
    a = int(input("Enter choice from below options"))

    if a == 1:
        n = int(input("Enter a number"))
        services.cuberoot(n)
        services.sqroot(n)
    elif a == 2:
        n = int(input("Enter a number"))
        print(f"{n}th fibonacci term is {services.Fibonacci(n)}")
elif c == 2:
    print("Enter elements of the list")
    li = [int(x) for x in input().split()]
    print("O/P for merge sort is ")
    services.mergeSort(li, 0, len(li)-1)
    print(li)
    print("O/P for insertion sort is ")
    services.insertionSort(li)
    print(li)
else:
    print("Enter a valid choice")
