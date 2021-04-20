"""
check whether the given number is leap yeaer or not . if years is leap print "LEAP YEAR" else print "COMMON YEAR"

"""

leap_year = 1996

if leap_year % 4 == 0 and leap_year % 400 == 0  or leap_year % 100 != 0:
    print("L E A P Y E A R")
else:
    print("C O M M O N Y E A R")