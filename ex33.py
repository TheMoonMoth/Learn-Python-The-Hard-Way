numberset = []
ding = int(raw_input("Type a number here:"))

def number_counter(i):
    while i < ding:
        print "\nAt the top, i is %d \n" % i
        numberset.append(i)
        i = i + 1
        print "Numberset now contains: ", numberset, "\n"
        print "At the bottom of the set, i is %d \n" % i

        if i == 7:
            print "It's a magic number.\n"
        elif i == 6:
            print "Not the best number.\n"
        else:
            print "\'i\' is too small now.\n"


number_counter(0)
print "The numbers: "

for num in numberset:
    print num
