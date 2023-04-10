li = []

for i in range(1, 11):
    li.append(i)

t = iter(li)

for i in range(len(li)+1):
    try:
        print(t.__next__())
    except StopIteration:
        print("Error handled successfully")
