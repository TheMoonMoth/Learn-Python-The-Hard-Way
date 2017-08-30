lists = "Shopping To-Do Pokedex 4 5 6 7 8 9 10"

print "Add a new list, one at a time."

all = lists.split(' ')

print all

while len(all) != 10:
    add_some = raw_input("> ")
    print "Adding your addition now..."
    all.append(add_some)
    print "There are now %d lists." % len(all)

print "Here are the lists: ", all

#CARDINAL numbers, not(ORDINAL)
print all[1]
print all[-3]
print all
print all.pop(-1)
print all.pop(0)
print all.pop(0)
print all.pop(0)
print ' '.join(all)
print '#'.join(all[0:11])
