"""
if temparature is greater than 30
its a hot day otherwise if
it less than 10
its a cold day otherwise
its neither hot nor cold
"""

temparature = int(input("enter your temparature"))

if    30  <= temparature :
    print("it's a hot day")
elif   temparature <= 10:
    print("it's a cold day")
else:
    print("its neither hot neither cold day")