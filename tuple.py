tup = (1,2,34)          #cannot make changes in tuples

t = ()        # Empty tuple
t = (1)       # wrong way to declare a single tuple
t = (1,)      # the right way

tup[0] = 34     # will throw error as changes cannot be made

print(tup.count(1))
print(tup.index(1))         # returns the first index at which the element occurs


