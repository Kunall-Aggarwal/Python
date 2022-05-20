st = {1, 3,4,4,4,5,6,6}

s = {}          # wrong way to declare empty set(will be read as empty dictionary)
s = set()       # right way to declare an empty set

#values are not repeated in sets
print(st)

st.add(23)
st.add(478)
st.add("aejfh")         # can store different types


b = (20, 20.0, "20")        # length of set in this case will be 2 becoz, 20 & 20.0 have the same values

b = ([132,414,5435])                                # lists cannot be stored in sets
b = ({132 : 98284, 414:9721, 5435: 2918379})        # dictionary cannot be stored in sets
b = ((132,414,5435))                                # tuples can be stored in sets as tuple cannot be changed

