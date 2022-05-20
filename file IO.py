f = open('sample.txt')                  # by default read
f = open('sample.txt', 'r')                 # read
f = open('sample.txt', 'w')                 # write
f = open('sample.txt', 'a')                 # append
f = open('sample.txt', '+')                 # update

data = f.read()

f.write("fehk aiwefuh awefaj ")

f.close()                               # must to write



# ALTERNATIVE: with statement
with open('sample.txt', 'r') as f:               # no read to write f.close() when using this
    f.read()
with open('sample.txt', 'w') as f:               # no read to write f.close() when using this
    f.write("ifhh aifu aifhjka")