fruits = ['Apple','Banana', 'Cheeku', 'Grapes']
for item in fruits:
    print(item)


# RANGE
i = 0
for i in range(1,8):          # prints i starting from 1 till 8(excluded)
    print(i)


for i in range(8):              # prints i starting from 0 till 8(excluded)
for i in range(1,8,2):          # prints i starting from 1 till 8(excluded) with skip counts of 2


# FOR ELSE
for j in range(10):
    print(j)
else:
    print("Ho gaya loop khatam")


# BREAK
for j in range(10):
    print(j)
    if(j == 5):
        break
else:
    print("Ho gaya loop khatam")


# CONTINUE
for j in range(10):
    if(j == 5):
        continue
    print(j)
else:
    print("Ho gaya loop khatam")