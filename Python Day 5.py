Python 3.8.0a1 (tags/v3.8.0a1:e75eeb00b5, Feb  3 2019, 20:47:39) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=(1,2,3)
>>> b=('a','b','c','d')
>>> a.append(5)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a.append(5)
AttributeError: 'tuple' object has no attribute 'append'
>>> a.append (5)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.append (5)
AttributeError: 'tuple' object has no attribute 'append'
>>> b.remove ('c')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    b.remove ('c')
AttributeError: 'tuple' object has no attribute 'remove'
>>> a.pop ()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.pop ()
AttributeError: 'tuple' object has no attribute 'pop'
>>> a.reverse ()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.reverse ()
AttributeError: 'tuple' object has no attribute 'reverse'
>>> b.sort ()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    b.sort ()
AttributeError: 'tuple' object has no attribute 'sort'
>>> b.pop ()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    b.pop ()
AttributeError: 'tuple' object has no attribute 'pop'
>>> for x in a;
SyntaxError: invalid syntax
>>> for x in a :
	print(x)

	
1
2
3
>>> c=list(a)
>>> c
[1, 2, 3]
>>> d=[x for x in a]
>>> d
[1, 2, 3]
>>> d=[for x in a]
SyntaxError: invalid syntax
>>> for x in x:
	print(y)

	
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    for x in x:
TypeError: 'int' object is not iterable
>>> a
(1, 2, 3)
>>> f=a+b
>>> f
(1, 2, 3, 'a', 'b', 'c', 'd')
>>> a*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> a
(1, 2, 3)
>>> "b" in b
True
>>> "e" in b
False
>>> 5 in a
False
>>> 1 in a
True
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> c=a+b
>>> c
[1, 2, 3, 4, 5, 6]
>>> x=[1,2,3,4,5]
>>> y=(x)
>>> y
[1, 2, 3, 4, 5]
>>> y=(x for x in x)
>>> y
<generator object <genexpr> at 0x0000009954A44970>
>>> a=[1,2,3,4,1,4,2,5,3,7]
>>> b set(a)
SyntaxError: invalid syntax
>>> b=set(a)
>>> b
{1, 2, 3, 4, 5, 7}
>>> c={"a","b","c","a","b","d","c"}
>>> c
{'a', 'c', 'd', 'b'}
>>> d={"a","A","B","b"}
>>> d
{'A', 'a', 'B', 'b'}
>>> d={"a","A","B","b","a","B"}
>>> D
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    D
NameError: name 'D' is not defined
>>> d={"a","A","B","b","a","B"}
>>> d
{'A', 'a', 'B', 'b'}
>>> s1{1,2,3,4}
SyntaxError: invalid syntax
>>> s1={1,2,3,4}
>>> s2={3,4,5,6}
>>> s2.add(7)
>>> s2
{3, 4, 5, 6, 7}
>>> s1.add(5,6)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    s1.add(5,6)
TypeError: add() takes exactly one argument (2 given)
>>> s2.remove(7)
>>> s2
{3, 4, 5, 6}
>>> s1.discard(4)
>>> s1
{1, 2, 3}
>>> s2.remove(7)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    s2.remove(7)
KeyError: 7
>>> s1.discard(4)
>>> s1
{1, 2, 3}
>>> s1.difference(s2)
{1, 2}
>>> s2.difference(s1)
{4, 5, 6}
>>> s1.intersection(s2)
{3}
>>> s1
{1, 2, 3}
>>> s2
{3, 4, 5, 6}
>>> s2.union(s1)
{1, 2, 3, 4, 5, 6}
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6}
>>> s1.update(7,8,9)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    s1.update(7,8,9)
TypeError: 'int' object is not iterable
>>> s1.update({10,11,12,13})
>>> s1
{1, 2, 3, 10, 11, 12, 13}
>>> dictionary
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    dictionary
NameError: name 'dictionary' is not defined
>>> s1.discard
<built-in method discard of set object at 0x0000009954A14DC0>
>>> codes={"kenya":254,"uganda";256,"tanzania";255}
SyntaxError: invalid syntax
>>> codes={"kenya":254,"uganda":256,"tanzania":255}
>>> codes["kenya"]
254
>>> codes["uganda"]
256
>>> codes["tanzania"]
255
>>> codes["kenya"]=250
>>> codes["uganda"]=280
>>> codes
{'kenya': 250, 'uganda': 280, 'tanzania': 255}
>>> codes["tanzania"]=270
>>> codes
{'kenya': 250, 'uganda': 280, 'tanzania': 270}
>>> codes["rwanda"]=252
>>> codes
{'kenya': 250, 'uganda': 280, 'tanzania': 270, 'rwanda': 252}
>>> codes.pop("rwanda")
252
>>> codes
{'kenya': 250, 'uganda': 280, 'tanzania': 270}
>>> codes.keys()
dict_keys(['kenya', 'uganda', 'tanzania'])
>>> codes.values()
dict_values([250, 280, 270])
>>> for key in codes.keys():
	print(key)

	
kenya
uganda
tanzania
>>> for value in codes.values():
	print(value)

	
250
280
270
>>> m=dict()
>>> m
{}
>>> m["a"]=10
>>> m["b"]=20
>>> m
{'a': 10, 'b': 20}
>>> m=["c"]=30
SyntaxError: cannot assign to literal
>>> m["c"]=30
>>> m
{'a': 10, 'b': 20, 'c': 30}
>>> range=[0,10]
>>> m=range[0,10]
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    m=range[0,10]
TypeError: list indices must be integers or slices, not tuple
>>> m=range(0,10)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    m=range(0,10)
TypeError: 'list' object is not callable
>>> m=range(10)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    m=range(10)
TypeError: 'list' object is not callable
>>> m="range"(10)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    m="range"(10)
TypeError: 'str' object is not callable
>>> g=range(10)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    g=range(10)
TypeError: 'list' object is not callable
>>> h=range[0,10]
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    h=range[0,10]
TypeError: list indices must be integers or slices, not tuple
>>> number=[0,1,2,3,4,5,6,7,8,9,10]
>>> n=range(10)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    n=range(10)
TypeError: 'list' object is not callable
>>> number
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> n=range(0,10)
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    n=range(0,10)
TypeError: 'list' object is not callable
>>> n= range(0,10)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    n= range(0,10)
TypeError: 'list' object is not callable
>>> n=range(0,10);
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    n=range(0,10);
TypeError: 'list' object is not callable
>>> n=range(0,10):
	
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> b=range(0,10)
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    b=range(0,10)
TypeError: 'list' object is not callable
>>> n=range(0,10)
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    n=range(0,10)
TypeError: 'list' object is not callable
>>> e=[x*x for number]
SyntaxError: invalid syntax
>>> >>> v = dict()
>>> v[2]=2*2
>>> v
{2: 4}
>>> for x in v:
	x*x

	
4
>>> 
>>> v[f]=x*x
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    v[f]=x*x
TypeError: unhashable type: 'list'
>>> v[f]=[x*x]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    v[f]=[x*x]
TypeError: unhashable type: 'list'
>>> z = dict()
>>> for p in range(10):
	m[p]=p*p

	
Traceback (most recent call last):
  File "<pyshell#43>", line 2, in <module>
    m[p]=p*p
NameError: name 'm' is not defined
>>> for p in range(10):
	m[p]= p*p
	print(z)

	
Traceback (most recent call last):
  File "<pyshell#46>", line 2, in <module>
    m[p]= p*p
NameError: name 'm' is not defined
>>> z
{}
>>> for p in range(10):
	z[p]=p*p

	
>>> print(z)
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> for z in fruits:
	a[x]=len of (z)
	
SyntaxError: invalid syntax
>>> for z in fruits:
	a[x]=len of(z)
	
SyntaxError: invalid syntax
>>> for z in fruits:
	a[z]=len of(z)
	
SyntaxError: invalid syntax
>>> 
>>> for z in fruits:
	a[z]=len(z)

	
>>> print(a)
{'mango': 5, 'pineapple': 9, 'peas': 4, 'apple': 5, 'kiwi': 4, 'banana': 6, 'orange': 6, 'melon': 5, 'lemon': 5, 'grapes': 6}
