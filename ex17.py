#Exersice 17: More Files
'''
Now let's do a few more things with files. We're going to actually write a Python script to copy one file to another. It'll be very short but will give you some ideas about other things you can do with files.
'''

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# We could do these two on one line too, how?

input = open(from_file)
indata = input.read()

print " The input file is %d bytes long" % len(indata)

print "does the output file exists? %r" % exists(to_file)

print "Ready, hit return to continue, CTRL-C to abort."

raw_input()

output = open(to_file, 'w')
output.write(indata)

print "Alright, all done."

output.close()
input.close()

