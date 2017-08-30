cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capactiy = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


#basic number of cars available.
print "There are", cars, "cars available."

#how many drivers there are.
print "There are only", drivers, "drivers available."

#how many cars wont be driven.
print "There will be", cars_not_driven, "empty cars today."

#active cars * space per car.MAXIMUM CAPACITY
print "We can transport", carpool_capactiy, "people today."

#People without cars.
print "We have", passengers, "the carpool today."

#people/active cars = DISTRIBUTION
print "We need to put about", average_passengers_per_car, "in each car."
