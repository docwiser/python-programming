car = {"brand": "Ford", "name": "Mustang", "year": 1960, "color": "Black"}
print(f"the current car implementation is like this: {car}")
print(f"the name of the car is {car['name']}")
print("Looping through the car...")
for x in car:
 print(f"{x} is {car[x]}")
print("Changing the color of the car...")
car["color"] = "Blue"
print(f"the color of the car is now {car['color']}")
print("Removing the year from the car...")
del car["year"]
print(car)