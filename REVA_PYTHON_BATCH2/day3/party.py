def classify_party(day, attendees):
    # Valid days
    valid_days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

    # Check for invalid day or negative attendees
    if day not in valid_days or attendees < 0:
        return "Invalid Input"

    # Weekdays: Monday – Thursday
    weekdays = ["MON", "TUE", "WED", "THU"]

    # Weekend: Friday, Saturday, Sunday
    weekend = ["FRI", "SAT", "SUN"]

    # Check success criteria
    if day in weekdays:
        if 700 <= attendees <= 1000:
            return "Successful"
        else:
            return "Unsuccessful"

    elif day in weekend:
        if attendees >= 1500:
            return "Successful"
        else:
            return "Unsuccessful"
        
        
        
day = input("enter the day").strip().upper()
attendees = int(input("ener the number of ateendees"))

result=classify_party(day, attendees)
print(result)
