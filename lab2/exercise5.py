"""
if name is less than 3 character long - name must be atleast 3 character long
otherwise if its more than 50 characters - name must be maximum of 50 characters
otherwise - name looks good!
"""

name = input("enter your name")
count = len(name)

if count <= 3:
    print("name must be more than 3 characters")
elif 50 <= count:
    print("name must be maximum of 50 characters")
else:
    print("looks awesome")
