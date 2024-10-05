# Modifying Immutable Objects
my_tuple = (1, 2, 3)
l=list(my_tuple)
l[0] = 5
my_tuple=tuple(l)
print(my_tuple)