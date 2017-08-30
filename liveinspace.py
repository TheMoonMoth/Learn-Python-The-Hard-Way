from sys import exit

def outside():
    print "You stumble through the storm and run into a ship!"
    print "There is a door but it's locked."

    door = False

    while True:
        print "What will you do? \n1 = Look around \n2 = Walk around \n3 = Open door"
        choice = raw_input('> ')

        if "1" in choice:
            print "You see a large button next to the door."
            print "1 = Press button \n2 = Look around \n3 = Bash door in"

            button = raw_input('> ')

            if "1" in button:
                door = True
                "The door unlocks and hisses open."
                first_floor()
            elif "3" in button:
                door = True
                print "The door unlocked!"
            else:
                print "The button won't respond to that."
                dead("A rock flys out of the storm and punctures your suit.")


        elif "2" in choice:
            dead("You walked away from your only hope of survival.")
        elif "3" in choice:
            if door == True:
                print "The door hisses open."
                first_floor()
            else:
                print "The door does nothing."
                dead("While you fumble with the door, the storm kills you.")
        else:
            print "You can't do that."
            dead("A gust of wind blows you a mile in the air. You fall to your death.")

def first_floor():
    print "You made it to the 1st floor."
    print "You see the ships power supply. But it's covered in blue moss."

    blue_moss()
    second_floor()

def blue_moss():
    print "Choose a tool to deal with the moss: \n1 = flashlight \n2 = knife \n3 = cream cheese"
    power = False

    while power == False:
        tool = raw_input('Which tool will you use?')
        if "1" in tool:
            print "The moss gets scared by the light and erupts into flames."
            print "The defense mechanism sets the power supply on fire."
            dead("The ship explodes.")
        elif "2" in tool:
            print "The moss feeds on metal."
            print "It eats the knife and starts on your suit."
            dead('The moss has eaten you alive.')
        elif "3" in tool:
            print "The moss loves cheese."
            print "It takes the cream cheese and disappearshon
             into the storm."
            print "You safely restore the ships power!"
            power = True
        else:
            print "You only have 3 tools, dingus."
            dead("The moss attacks while you fiddle with %s") % tool

def dead(why):
    print why, "Smooth move, space cadet."
    exit(0)

outside()
