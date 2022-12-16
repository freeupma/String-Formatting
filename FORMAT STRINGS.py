# replace with string-positional

first_name= "Janet"
last_name= "Cheserem"

print("My name is {}.".format(first_name))
print("My name is {} {}.".format(first_name,last_name))

# replace with string using index
#can be useful when order varies

print("My name is {0} {1}.".format(first_name,last_name))
print("My name is {1}, {0}. First name {0}". format(first_name,last_name))

# alignment:Align Left, Right, Middle
#{:<} align Left(default is align left)
#{:>n} align Right with n padding spaces
#{:^n}align Middle with n padding spaces

# align left; these both do the same thing
cases=[5,60,778]
for case in cases:
    print("Number of cases:{}".format(case))
for case in cases:
    print("Number of cases:{:<}".format(case))

# align right with 5 total spaces; 5 spaces including 5 or 60 or 778
for case in cases:
    print("Number of cases:{:>5}".format(case))
    
# align center with 5 total spaces
for case in cases:
    print("Number of cases:{:^5}".format(case))
    

#{}Integer variable
#{}Integer with padding of 5
#{}Floating point variable



# integer with commas
print("Distance to the moon is {:,d}".format(238900))

radius= 4.78
print("radius is {:f} inches.".format(radius))

# round to 1 decimal place, float
print("radius is {:.1f} inches.".format(radius))

# padding=6 (pads with leading 0's), round to 1 decimal
print("radius is {:06.1f} inches.".format(radius))

# padding =5 decimal places
print("radius is {:.5f} inches".format(radius))

# positive & negative signs
a,b,c = 15, -9, 33
print("A is {:+d}. B is {:+d}. C is {:-d}.".format(a,b,c))

#{+3d} shows pos or neg sign, padding=3
#{: d} prints neg or a leading space if poitive
print("A is {:+3d}. B is {:+4d}. B is {: d}".format(a,b,c))

#NAMED PLACEHOLDERS
#or use a dictionary, and ** unpacks the dictionary
jobs = {"name":"Janet", "job":"data_analyst"}
print("{name} is a {job}".format(**jobs))

#passing in a list is clean and easy
scores= [78,96,83,86]
print("Score 2 is {s[1]}".format(s=scores))








