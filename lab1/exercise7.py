"""
you live 4 miles from university .  the bus driver drives at 25mph but spends 2 minute at each of the ten stops on the
way .how long will the bus journey takes ? .alternatively , you could run to university. you jog the first mile  at 7 mph
then run the next 2 at 15mph before jogging the last at 7mph again . will this be quicker or slower than bus ?
"""

uni_miles = 4
driver_speed = (4 / 25) * 60
bus_stop = 2 * 10

bus_time =  (driver_speed  + bus_stop)

print(f"driver takes {bus_time} minute to reach university")

first_mile = (1 / 7) * 60
second_mile =  (2 / 15) * 60
third_mile =  (1 / 7) * 60

jog_time = first_mile + second_mile + third_mile

print(f"jogging takes {jog_time} minute to reach university")

if bus_time > jog_time :
    print("taking bus is slower than running")
else:
    print("taking bus is faster than running")

