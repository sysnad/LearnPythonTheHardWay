#### Variables and Names Exercise 4 ####
#cars gives us the number of available vehicles
cars = 100
#space_in_a_car tell us the amount of passengers each car can carry
#note that this is on floating point to account for 1/2 or 1/4 capacity (without seatbelts)
space_in_a_car = 4.0
#The people available for driving, its important because our cars are not automated and need a person to drive thus accounting for non-used cars
drivers = 30
#passengers tell us the amount of non-driving people
passengers = 90
#cars_not_driven makes use of the fact that cars are not automated and need a driver
cars_not_driven = cars - drivers
#the figure and ground of cars_not_driven
cars_driven = drivers
#This would tell us how much capacity we have when we account the vehicles in use.
carpool_capacity = cars_driven * space_in_a_car
#This can only show us an average of teh passengers in each car since we don't know for sure
average_passengers_per_car = passengers / cars_driven
#prints the number of cars in total
print "There are", cars, "cars available."
print " "
#print the amount of vehicles in use
print "There are only", drivers, "drivers available."
print " " 
#prints the amount of cars not driven
print "There will be", cars_not_driven, "empty cars today."
print " "
#print the amount of seats available 
print "We can transport", carpool_capacity, "people today."
print" "
#prints the amount of non-drivers people in each vehicles
print "We have", passengers, "to carpool today."
print " "
# Tell us the average estimate on the amount of people in each car
print "We need to put about", average_passengers_per_car, "in each car."