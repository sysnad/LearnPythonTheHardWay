#We're using a formatter that creates the output of raw data if we were to used %s 
#we it would represent them as strings

formatter = "%r %r %r %r"
# formatter = "%s %s %s %s"

#the following prints out integers as they appeaer
print formatter % (1, 2, 3, 4)

#now we print out strings as they appear including the quotation
print formatter % ("one", "two", "three", "four")

#we are using 
print formatter % (True, False, False, True)

print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
	"I had this thing.", 
	"That you could type up right. ",
	"But it didn't sing.", #we don't want to interpret the didn't as the closing quote so we use double quotes..
	"So I said goodnight."
)
