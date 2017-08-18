#Exercise 10: What was that?

#You can use \ as a escape sequence

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grasss
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print '''
Hey there
Does this work 
Maybe
'''

#try this out

while True:
	for i in ["/", "-", "|", "\\"]:
		print "%s\r" % i,
