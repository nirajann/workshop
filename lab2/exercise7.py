"""
game finding a secret number within 3 attempts using while loop
"""


secret_number = 3
i = 1

while i < 4:
    given = int(input("enter the secret number"))
    i+=1

    if given == secret_number:
        print("congrats you are correct")

    else:
        print("sorry! try again")
