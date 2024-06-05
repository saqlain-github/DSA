def calling(name,init,next):
    new_init = (int(ord(init[0])-96),int(init[1]))
    new_next = (int(ord(next[0]) - 96),int(next[1]))
    if name == "Horse":
        return horse(new_init,new_next)
    elif name == "knight":
        return knight(new_init,new_next)

def knight(init,next):
    if(init[0] - next[0] == (init[1] - next[1]) or init[0] - next[0] == -(init[1] - next[1])):
        return "t"
    return "f"

def horse(init,next):
    if(init[0] == next[0]+1 or init[0] == next[0]-1):
        if(init[1] == next[1]+2 or init[1] == next[1]-2):
            return "t"
    elif(init[0] == next[0] + 2 or init[0] == next[0] - 2):
        if(init[1] == next[1] + 1 or init[1] == next[1] - 1):
            return "t"
    return "f"

temp = "a,b,c,d,e,f,g,h"
alpha = temp.split(",")
for j in range(1, 9):
    for i in alpha:
        print(calling("knight", "d4", i+str(j)), end=" ")
    print("", end="\n")