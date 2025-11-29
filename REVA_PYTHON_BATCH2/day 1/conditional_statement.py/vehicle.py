vehicle_type = input("Enter type of vehicle (TW/FW): ")
number = int(input("Enter number of vehicles: "))

if vehicle_type.upper() == "TW":
    wheels = number * 2
elif vehicle_type.upper() == "FW":
    wheels = number * 4
else:
    print("INVALID INPUT")
    exit()

print("Total =", wheels)

if vehicle_type.upper() == "TW":
    print("Explanation:")
    print(f"{number} TW = {wheels} wheels")
elif vehicle_type.upper() == "FW":
    print("Explanation:")
    print(f"{number} FW = {wheels} wheels")