digit_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# Read number from user
num = input("Enter a number: ")

# Print each digit as word
for digit in num:
    print(digit_words[int(digit)], end=" ")