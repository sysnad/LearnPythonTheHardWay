#Exercise 15: Reading Files
###
'''
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here. 
'''
###

#basically asks for module argv to be fetch from sys
from sys import argv

#Allow us to consider two arguments in our program
script, filename = argv

#We are defining txt as the argument filename being opened
txt = open(filename)

#This line inform us that it has fetched our file
print "Here's your file %r:" % filename
#This line prints the file
print txt.read()

#Now we would run the test again
print "Type the filename again:"
#We would named the file again after the prompt sign
file_again = raw_input("> ")

#This would open the file agains similar to line 17
txt_again = open(file_again)

#It would go straight to the file.
print txt_again.read()




