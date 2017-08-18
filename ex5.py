# my_name = 'Zed A. Shaw'
# my_age = 35 # not a lie
# my_height = 74 # inches
# my_weight = 200 # lbs 
# my_eyes = 'Blue'
# my_teeth = 'White'
# my_hair = 'Brown'

# print "Let's talk about %s." % my_name
# print "He's %d inches tall." % my_height
# print "He's %d pounds heavy." % my_weight
# print "Actually that's not too heavy."
# print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
# print "His teeth are usually %s depending on the coffee." % my_teeth
# print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

### Study Drill 1 ###

name = 'Aldo Bocanegra'
age = 25 # not a lie
height = 72 # inches
metric_height = height * 0.0254
rounded_mheight = round(metric_height, 1)
weight = 200 # lbs
metric_weight = weight * 0.453592
rounded_mweight = round(metric_weight)
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + 	weight)
print " "
print "The metric height is %r meters and the metric weight is %d. kg" % (rounded_mheight, metric_weight)