tickets = int(input("Enter number of tickets: "))
rate = int(input("Enter rate per ticket: "))
category = input("Enter category (Tatkal/Ordinary): ")
charges = int(input("Enter other charges: "))

discount = 0

if tickets > 10 and category.lower() == "tatkal":
    discount = 0.2 * tickets * rate

total = (tickets * rate + charges) - discount

if discount > 0:
    print("Discount Applied - Maximum Tickets and Tatkal")
else:
    print("No Discount")

print("Total Amount =", int(total))