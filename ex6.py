
#this line explains how many types of of people there are by using python format d which
#is meant to denote decimal integers
x = "There are %d types of people." % 10

#binary is a string representing the word binary so we're allow to charcterise through
#%s format
binary = "binary"

#since we are not able to call a variable don't we use spacing as do not which represents
#the word don't
do_not = "don't"

#y is the punch line of the joke meaning we're talking about only two types of people when we
#originally claimed 10 people
y = "Those who know %s and those who %s." % (binary, do_not)

#we would now print the joke
print x 

print y

print "I said: %r." % x

print "I also said: '%s'." % y 

#here we have a boolean variable for the hilarity of the joke
hilarious = False
#here we observe that we left a raw data format opened to make use in our future print of the joke evaluation.
joke_evaluation = "Isn't that joke so funny?! %r"


print joke_evaluation % hilarious

w = "This is the left side of ..."

e = "a string with a right side."

#this would sum up the strings w and e allowing to make sense of a joke when combined.
print w + e

