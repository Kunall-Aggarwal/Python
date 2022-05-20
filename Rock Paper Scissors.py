import random

def conclusion(a, b):
    if(a == b):
        return None
    elif(a == 's'):
        if(b == 'r'):
            return True
        elif( b == 'p'):
            return False
    elif(a == 'r'):
        if(b == 's'):
            return False
        elif( b == 'p'):
            return True
    elif(a == 'p'):
        if(b == 'r'):
            return True
        elif( b == 's'):
            return False


n = random.randint(1,3)

if( n == 1):
    comp = 'r'
elif( n == 2):
    comp = 'p'
else:
    comp = 's'

res = input("Your turn: Rock(r), Paper(p) or Scissors(s) ")

if(res == "r" or res == "s" or res == "p"):
    a = conclusion(comp, res)
    dic = {
        "r" : "Rock",
        "p" : "Paper",
        "s" : "Scissors"
    }
    print(f"Comupter chose {dic.get(comp)}")
    print(f"You chose {dic.get(res)}")
    if(a is None):
        print("It was a TIE")
    elif(a is True):
        print("WINNER")
    else:
        print("LOOSER")
else:
    print("Invalid Input")