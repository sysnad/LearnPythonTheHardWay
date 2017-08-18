# Exercise 16: Reading and Writing
#We are getting access to argv in the sys library
from sys import argv

#there are two arguments needed in our script
script, filename = argv

#This wo uld erase the last test.txt
print "We're going to erase %r." % filename
print "If you do want that, hit RETURN."
print "If you don't want that, hit ctrl-c (^C)."

#gets the input that we want like enter
raw_input("?")

#Now we'll open our target file
print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
text = line1,"\n", line2, '\n',line3, '\n'
print "I'm going to write these to the file."

target.write(str(text))
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print "And finally, we close it."
target.close()