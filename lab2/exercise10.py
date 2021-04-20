number_1 = 3
number_2 = 4
number_3 = 6

if number_1 > number_2:
    if number_3 > number_2:
        print(f"{number_2} is the smallest among three number")
elif number_2 > number_1:
    if number_3 > number_1:
        print(f"{number_1}  is the smallest among three number")
elif number_3 > number_2:
    if number_1 > number_2:
        print(f"{number_2} 3 is the smallest")
