'''
write a pogram that reads the length of base and height of right andle triangle and print the area.
every numberis given on a seperate line
'''

length = int(input("enter the length "))
height = int(input("enter the height "))

right = (length + height) // 2  # // is division

print(f"the area of right angle triangle is {right}")