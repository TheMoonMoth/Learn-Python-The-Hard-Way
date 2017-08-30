#argv=MODULE
from sys import argv

#unpackable variables from the module
script, first, second, third, fourth, fifth = argv

script = raw_input("What do you want to call this script? ")

print "This script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "You fourth variable is:", fourth
print "Your fifth variable is:", fifth

data = raw_input("Leave data here: ")
first = raw_input("The winner came in...? ")

print "What do you get when you cross %s and %s?" % (second, third),
answer = raw_input()

print "No, a frog!"
