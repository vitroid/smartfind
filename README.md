
A smarter find() function.

* Can search multiple values.
* Can search with a condition.
* Always returns multiple matches.

    In [1]: from smartfind import sfind
    
    In [2]: C = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0]
    
    In [3]: tuple(sfind(C, (1,)))
    Out[3]: (1, 3)

    In [4]:  tuple(sfind(C, lambda x:x==1))
    Out[4]: (1, 3)
    
    In [5]: list(sfind(C, lambda x:x in (1,3)))
    Out[5]: [0, 1, 3, 9, 15, 17, 24, 25, 27]
    
    In [6]: list(sfind(C, (1,3)))
    Out[6]: [0, 1, 3, 9, 15, 17, 24, 25, 27]
    
    In [7]: list(sfind(C, (1,3), fromend=True))
    Out[7]: [-5, -7, -8, -15, -17, -23, -29, -31, -32]


