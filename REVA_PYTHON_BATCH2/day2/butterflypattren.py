rows = int(input("Enter number of rows: "))

# Upper half
for i in range(1, rows + 1):
    # Left stars
    print("*" * i, end="")
    # Middle spaces
    print(" " * (2 * (rows - i)), end="")
    # Right stars
    print("*" * i)

# Lower half
for i in range(rows, 0, -1):
    # Left stars
    print("*" * i, end="")
    # Middle spaces
    print(" " * (2 * (rows - i)), end="")
    # Right stars
    print("*" * i)