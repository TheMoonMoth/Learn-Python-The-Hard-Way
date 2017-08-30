people = int(50)
cats = int(15)
dogs = int(30)


if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"


if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."


if people == dogs:
    print "People are dogs."


aliens = 10


raw_input("\nThe aliens have arrived. Ready?")

def people_v_alien(people, aliens):
    if aliens > people:
        print "The aliens have taken control of the humans minds."
    elif aliens < people:
        print "The humans have protected Earth with the help of our furry friends."
    elif aliens == people:
        print "The humans and aliens have come together in peace."

def dog_v_alien(aliens, dogs):
    if aliens < dogs:
        print "Dogs lick the aliens to death."
    elif aliens > dogs:
        print "The dogs play along and get the alien bacon."
    elif aliens == dogs and (dogs > people):
        print "The dogs demand partnership in the enslavment of humanity."

def cats_v_all(cats, dogs, people, aliens):
    if aliens == cats:
        print "Cats seize the alien technology and enslave humans and aliens alike."
    elif aliens > cats:
        print "Aliens incinerate the cats, knowing of their insidious intentions."
    elif cats > people + dogs + aliens:
        print "Cats enact operation \"Control the Universe\""
    elif aliens < cats:
        print "The cats win. And live peacefully on Earth."


print "\nThere are %d people and %d aliens. So:" % (people, aliens)
people_v_alien(people, aliens)

print "\nThere are %d aliens and %d dogs, so:" % (aliens, dogs)
dog_v_alien(aliens, dogs)

print "\nThere are %d cats though... " % cats
cats_v_all(cats, dogs, people, aliens)
