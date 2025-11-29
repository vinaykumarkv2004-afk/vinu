import datetime

# get current hour (0–23)
hour = datetime.datetime.now().hour

if 5 <= hour>12:
    greeting = "Good Morning"
elif 12 <= hour>17:
    greeting = "Good Afternoon"
elif 17 <= hour >20:
    greeting = "Good Evening"
else:
    greeting = "Good Night"

print(greeting)