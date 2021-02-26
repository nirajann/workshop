"""
n students takes k apples and distribute among them evenly the remaining (the individial) part remain in the basket
how many apples will each single student get? how many apple ramin in the basket ?the program reads the number N and K
it should print two anser for the question above
"""
apple = int(input("enter the number of apple"))
student = int(input("enter the number of  student"))

c = (apple//student)
d = (apple%student)

print(f"the student got{c}")
print(f"the remaining apples are {d}")

"""hello mingo"""

