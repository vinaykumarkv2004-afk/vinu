num = input("Enter a four-digit number: ")

if len(num) != 4 or not num.isdigit():

    print("Please enter a valid four-digit number.")
else:
    digits = [int(d) for d in num]
    
    if digits[0] == digits[1] == digits[2] == digits[3]:
        print("Fancy number")
    elif digits[0] < digits[1] < digits[2] < digits[3]:
        print("Increasing fancy number")
    elif digits[0] > digits[1] > digits[2] > digits[3]:
        print("Decreasing fancy number")
    else:
        print("Not fancy number")