#Exercise 18: Names, Variables, Code, Functions

'''
Big title right? I am about to introduce you to the function! dum dumdah! Every programmer will go on and on about functions and all the different ideas about how they work and wha they do, but I will give you the simplest explanation you can use right now.

function do three things:
1.They name pieces of code the way variables name strings and numbers.

2.They take arguments the way your scripts take argv

3.Using #1 and #2 they let you make your own "mini scripts" or "tiny commands".

'''
#this one is like scripts with argv

def print_two(*args):
    arg1,arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok, that *args is actually pointless, we can just do this

def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1,arg2)

#this just takes one arguments
def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothing'."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()