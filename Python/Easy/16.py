l1,l2=[],[]
L=(1,2,3,4)
for i in L:
    l1.append(i)
l1.append(5)
my_tuple = (1, 2, 3)
for i in my_tuple:
    l2.append(i)
l2.append(5)
  # 'tuple' object has no 'append' method
print(tuple(l1))
print(tuple(l2))