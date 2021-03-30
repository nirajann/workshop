"""
price of house is 1m
if buyer has good credit
they need to put down 10% otherwise
they need to put down 20%
print the down payment
"""

buyer_credit = True
price = 1000000

if buyer_credit:
     print(F"you need to pay {(price * 10)/100}")
else:
    print(F"you need to pay {(price * 20)/100}")
