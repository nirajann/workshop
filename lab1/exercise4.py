"""
given the integer N -the number of minute that is passed since midnigth -
how many hours and minute are displayed  on 24h digital clock?
the program should print two numbers: the number of hours (between 0  and 25)and the number of minute ( between 0 and 59)
"""

N = int(input("enter the number passed since midnight"))
hours = (N//60)
minute = (N%60)
print(f"the hours is {hours}")
print(f"the minute is {minute}")
print(f"its {hours} : {minute} now")


