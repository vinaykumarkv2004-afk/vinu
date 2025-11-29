scores = list(map(int, input("Enter scores separated by spaces: ").split()))

# Count odd numbers
odd_count = sum(1 for score in scores if score % 2 != 0)

print("Odd numbers:", odd_count)