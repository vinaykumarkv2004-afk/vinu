rainfall = int(input("Enter rainfall in mm: "))

if rainfall == 0:
    print("No Rain")
elif 1 <= rainfall <= 10:
    print("Light Rain")
elif 11 <= rainfall <= 15:
    print("Moderate Rain")
elif rainfall > 15:
    print("Heavy Rain")
else:
    print("Invalid input")
    