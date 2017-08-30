
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s, to %s..." % (from_file, to_file)

#we could do these two on one line, how?
#in_file = open(from_file); indata = in_file.read()
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL_C to abort."
raw_input("Last Chance>")

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
in_file.close()

print "Alright, all done."

#from sys import argv; script, from_file, to_file = argv; in_file = open(from_file).read(); raw_input('>'); out_file = open(to_file, 'w'); out_file.write(in_file); out_file.close()
#print "Alright, all done."
