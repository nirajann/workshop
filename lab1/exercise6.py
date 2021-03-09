"""
solve the each of the following problem using python scripts.make sure you use an appropriate variable names and comments.
when there is final answer have python print it to the screen
A person's body mass BMI id defined as:
 BMI : mass in kg /(height in meter)2
"""

mass_in_kg = int(input("enter the mass in kg"))
height_meter = int(input("enter the height in meter"))

height_meter_square = height_meter ** 2

bmi = mass_in_kg // height_meter_square

print(f"the person body mass is {bmi}")