# greeting = "Good morning, "
# name = "Kunal"

# STRING Concatination
# c = greeting + name
# print(c)


#  String Slicing
# name = "Kunal"
# print(name[0])
# print(name[0:3])        # here element at index 3 will not be included
# print(name[:4])         # is same as name[0:4]
# print(name[0:])         # is same as name[0:5] i.e. length of string
# print(name[-4:-1])      # is same as name[1:4]


# Slicing with Skip values
name = "Amazing"
d = name[1:4:2]             # gets value from 1 to 4(excluded) with skips of 2
print(d)