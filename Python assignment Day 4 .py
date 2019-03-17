Python 3.8.0a1 (tags/v3.8.0a1:e75eeb00b5, Feb  3 2019, 20:47:39) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> c=[7,8,9]
>>> d=a+b+c
>>> d
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> e=(x*x for x in d)
>>> e
<generator object <genexpr> at 0x000000482D7D6970>
>>> e=[x*x for x in d]
>>> e
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>>nested=[[1,2,3],[4,5,6],[7,8,9]
           for x in l;
           for z in x;
           m.append(z)







