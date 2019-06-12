from smartfind import sfind
C = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0]
tuple(sfind(C, (1,)))
tuple(sfind(C, lambda x:x==1))
#Want the first item
next(sfind(C, lambda x:x==1))
#Lookup multiple items
list(sfind(C, lambda x:x in (1,3)))
list(sfind(C, (1,3)))
#Lookup from the bottom
list(sfind(C, (1,3), fromend=True))
for i in range(len(In)-1):
    print("      In [{0}]: {1}".format(i,In[i]))
    if i in Out:
        print("      Out[{0}]: {1}".format(i,Out[i]))
    print()

