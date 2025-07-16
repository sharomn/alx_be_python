raws = 5

for i in range(1, raws + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()





rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
