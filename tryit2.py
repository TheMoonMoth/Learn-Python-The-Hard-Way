def addition(sum, new_value):
    total = sum + new_value
    print "The sum is %s." % total

print "What number would you like to start with?"
sum = int(raw_input(">"))

print "What would you like to add to that?"
new_value = int(raw_input(">"))

addition(sum, new_value)

#SUCCESS

def smokebowls(nugs, pipes, friends, munchies):
    print "%s buddies just showed up with %s marijuanas." % (friends, nugs)
    print "%s of these guys brought a pipe." % (friends/2)

smokebowls(6, 4, 2, 0)


def user_update(health, shield, stamina):
    print "Your health levels is: %s" % health
    print "Shield Quality: %s" % shield
    print "Stamina Remaining: %s" % stamina

enemy_fire = 15
defense = 8
shield = enemy_fire + defense

user_update(100, 100 - shield, 100)
