started = False

# creating a continuous loop
while True:
    instruction = input('>').lower()

    # checking if the user needs help
    if instruction == "help":
        print('''
        start - to start the car
        stop - to  stop the car
        quit -  to exit the program
        ''')
    # intruction when the user wants to start the car
    elif instruction == "start":
        if started:
            print('The Car already started')
        else:
            started = True
            print('Car Started...Ready to go.')

    # instruction when the user wants to stop the car
    elif instruction == "stop":
        if not started:
            print('The Car already stopped.')
        else:
            started = False
            print('Car stopped')

    # instruction when the user wants to quit
    elif instruction == "quit":
        break

    # in case the user writes an invalid  command, it will show this message
    else:
        print("Invalid command.")
