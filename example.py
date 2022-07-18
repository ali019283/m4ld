import m4ld

# elements
lis = ["a","b","c","d","e","f"]

# how big will the each group will be
bign = 3

# how many lines to print
bigl = 4

# element name, how many times will it be used max, which turns it should NOT be on
ls = [
["a", 3, 2],
["b", 3 ,4 ,3],
["c", 2 , 3],
["d", 1, 1],
["e", 1 , 4],
["f", 3 ,2]]

x = mald(lis, bign, bigl, ls)

print(x)

# Output:
# [[['b', 'f', 'a']], [['b', 'd', 'c']], [['a', 'e', 'f']], [['f', 'a', 'c']]]
 

