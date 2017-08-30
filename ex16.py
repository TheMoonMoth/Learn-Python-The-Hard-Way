#import in the module
from sys import argv

#script name, filename
script, filename = argv

#print lines - statements
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)." #^C = STOPS SCRIPT!
print "If you do want that, hit RETURN."

#unassigned raw_input will wait for ANY user input.
raw_input("?")

#print line -- loading...
print "Opening the file..."
#the acutal loading/opening function -- open()
#!!!!OK! = means target is the variable.
target = open(filename, 'w') #'w' means safe mode. from what?

#print line -- truncating!
print "Truncating the file. Goodbye!"
#actual truncate function!!!! varibalbe.truncate() means the function is
#happening to the variable
target.truncate()

print "Now I'm going to ask you for three lines."

#asking for 3 lines of input
line1 = raw_input("Line 1:")
line2 = raw_input("Line 2:")
line3 = raw_input("Line 3:")

print "I'm going to write these to the file."

#variable.function = write (what i want written) to the variable.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
#function of closing the file or variable.
target.close()
