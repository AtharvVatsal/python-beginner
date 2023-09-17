command = ''
started = False     #car always stopped
while True:         #Directly starts while loop
    command = input(">").lower()
    if command == 'start':
        if started:
            print("Car Already On")
        else:
            started = True
            print('Car Started')
        command1 = input("Enter pathway ").lower()
            if command1 == 'w':
            print("Car accelerating")
            elif command1 == 's':
            print("Car deaccelerating")
             else:
            print('No defined path')
    elif command == 'stop':
        if not started:                 #started -> false
            print("Car Already Stoped")
        else:
            print("Car stoped")
    elif command == 'help':
        print(""" 
start: To start car
w: Accelerate
s: Deaccelerate
stop: Stop Car
quit: To Quit""")
    elif command == 'quit':
        break                       #break while loop and exits program
    else:
        print("Invalid Input")