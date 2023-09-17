command = ''
started = False
while True:
    command = input(">").lower()
    if command == 'start':
        if started:
            print("Car Already On")
        else:
            started = True
            print('Car Started')
        command1 = input("Enter path ").lower()
        if command1 == 'w':
            print("Car accelerating")
        elif command1 == 's':
            print("Car deaccelerating")
        else:
            print('No defined path')
    elif command == 'stop':
        if not started:
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
        break
    else:
        print("Invalid Input")