"""
WAP which accepts marks of four students  and display total marks , percentage and grade
"""

stu_1 = int(input("enter your marks"))
stu_2 = int(input("enter your marks"))
stu_3 = int(input("enter your marks"))
stu_4 = int(input("enter your marks"))

marks = stu_1 + stu_2 + stu_3 + stu_4
grade = (marks * 100 ) / 400

if 70 <= grade:
    print(f"total marks :{marks}")
    print(f"percentage :{grade}%")
    print("distinction")
elif 60 <= grade <= 70:
    print(f"total marks :{marks}")
    print(f"percentage :{grade}%")
    print("first")
elif 40 <= grade <= 60:
    print(f"total marks :{marks}")
    print(f"percentage :{grade}%")
    print("pass")
elif grade <= 40 :
    print(f"total marks :{marks}")
    print(f"percentage :{grade}%")
    print("fail")