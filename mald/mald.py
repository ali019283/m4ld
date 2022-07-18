a = ["a","b","c","d","e","f"]
b = 3 
c = 4 
d = [["a", 2 ,2], 
["b", 3 ,4 ,3], 
["c", 1 , 3], 
["d", 3, 1], 
["e", 2 , 4], 
["f", 2 ,2]]

import random

# lis(list) = list
# bign(int) = how big the group will be
def ran_gp(lis, bign):
    random.shuffle(lis)
    ag = []
    ag.append(lis[0:bign])
    return ag

# lse(int) = to what element will the list be deleted to, e.g if the lse is 2, the list will be deleted to the index 2
# nde(list) = a list of elements that should NOT be removed, they wont be removed even if they are in the range of lse
def plist(lis, lse, nde):
    for i in range(lse):
        for e in range(len(nde)+1):
            # TODO: remove try
            try:
                if lis[i] == nde[e]:
                    break
                else:
                    continue
            except IndexError:
                lis.pop(i)
    return lis


# bigl(int) = how many lines to print
# ls(list) = 2d array to store information about the elements
def mald(lis, bign, bigl, ls):
    rs = [] 
    for i in range(bigl):
        olis = lis.copy()
        for x in range(len(ls)):
            if ls[x][1] == 0:
                olis.remove(ls[x][0])
                continue
            for y in ls[x][2:]:
                if y == i+1:
                    olis.remove(ls[x][0])
                    break
                else:
                    continue
        rnmlis = ran_gp(olis, bign)
        rs.append(rnmlis)
        for k in rnmlis[0]:
            for l in range(len(ls)):
                for m in ls[l]:
                    if ls[l][0] == k:
                        ls[l][1] = ls[l][1]-1
                    else:
                        continue
    return rs
mald (a,b,c,d)
            
    

    

    
