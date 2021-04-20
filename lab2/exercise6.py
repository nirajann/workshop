"""
weight converter :
input the weight of a person in either kg or lbs
if the person provides his/her
weight in kg then convert it into lbs
else convert it into kg
"""

weight_1 = float(input("enter your weight in kg or lbs "))
kg_lbs = input("kg or lbs ")

if kg_lbs == "kg":
    kg = weight_1 * 2.205
    print(f"you are {kg} kg")
elif kg_lbs == "lbs":
    lbs = weight_1 // 2.206
    print(f"your are {lbs} lbs")

