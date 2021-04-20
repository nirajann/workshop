"""
cargame:
   >help
   start - to start the car
   stop - to stop the car
   quit - to quite
   >asd
   i dont understand this
   >start
   car started.... ready to go!!
   >stop
   car stopped...
   >quit
   you have quit the game

"""

command = ""
started = False
stopped = False


while command != "quit":
    command = input(">")
    if command == "quit":
        print("the game had ended")
        break
    elif command == "start":
        if started:
            print("the car has already sgtarted")
        else:
           started = True
           print("car has started")
    elif command == "stop":
        if stopped:
            print("the car has already sgtarted")
        else:
           stopped = True
           print("car has stoppped...")
    elif command == "help":
        print("""start - to start the car
        stop - to stop the car
        quit - to exit""")
    else:
        print("i dont understand this")



