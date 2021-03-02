"""
a school decided to replace the desks in three classroom . each desk sits two students given the number of
students in each class.
print the smallest possible number of desks that can be purchased the program should read three integers the
number of students in each of the three classes a,b and c respectively.
In the first test there is three groups .the first group has 20 students and thus needs 10 desks. the second
group has 21 students , so they can get by with no fewer than 11 desks . 11 desks are also enough for third group
of 22 students.so, we need 32 desks in total .
"""

student_class1 = int(input(" enter the number of first group :"))
student_class2 = int(input(" enter the number of second group :"))
student_class3 = int(input(" enter the number of third group :"))

desk_class1 = (student_class1 // 2)
desk_class2 = (student_class2 // 2)
desk_class3 = (student_class3 // 2)

print(f"the desk for class one is : {desk_class1}")
print(f"the desk for class two is : {desk_class2}")
print(f"the desk for class three is : {desk_class3}")


remain_class1 = (student_class1 % 2)
remain_class2 = (student_class2 % 2)
remain_class3 = (student_class3 % 2)

print(f"the remaining desk for class one is : {remain_class1}")
print(f"the remaining desk for class two is : {remain_class2}")
print(f"the remaining desk for class three is : {remain_class3}")

total_desk =(desk_class1 + desk_class2 + desk_class3 - remain_class1 + remain_class2 + remain_class1 )
print(f"the total number of desk is : {total_desk}")




