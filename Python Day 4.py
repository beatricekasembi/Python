Python 3.8.0a1 (tags/v3.8.0a1:e75eeb00b5, Feb  3 2019, 20:47:39) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruits = ['Banana','apple','mango','pineapple','berries','kiwi']
>>> For fruit in fruits:
	
SyntaxError: invalid syntax
>>> for fruit in fruits:
	print (fruits)

	
['Banana', 'apple', 'mango', 'pineapple', 'berries', 'kiwi']
['Banana', 'apple', 'mango', 'pineapple', 'berries', 'kiwi']
['Banana', 'apple', 'mango', 'pineapple', 'berries', 'kiwi']
['Banana', 'apple', 'mango', 'pineapple', 'berries', 'kiwi']
['Banana', 'apple', 'mango', 'pineapple', 'berries', 'kiwi']
['Banana', 'apple', 'mango', 'pineapple', 'berries', 'kiwi']
>>> numbers = [0,1,2,3,4,5,6,7,8,9]
>>> for number in numbers
SyntaxError: invalid syntax
>>> for number in numbers:
	print(number)

	
0
1
2
3
4
5
6
7
8
9
>>> for fruit in fruits:
	print(fruit)

	
Banana
apple
mango
pineapple
berries
kiwi
>>> fruit[0]
'k'
>>> fruits[0]
'Banana'
>>> fruits[4]
'berries'
>>> fruits[0:4]
['Banana', 'apple', 'mango', 'pineapple']
>>> fruits[4:5]
['berries']
>>> fruits[5:6]
['kiwi']
>>> fruits[4:6]
['berries', 'kiwi']
>>> print[4:]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print[4:]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> fruits[4:]
['berries', 'kiwi']
>>> fruits[-2:]
['berries', 'kiwi']
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> c=a+b
>>> c
[1, 2, 3, 4, 5, 6]
>>> d=a*3
>>> d
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> fruits
['Banana', 'apple', 'mango', 'pineapple', 'berries', 'kiwi']
>>> fruits.append("grapes")
>>> fruits
['Banana', 'apple', 'mango', 'pineapple', 'berries', 'kiwi', 'grapes']
>>> fruits.add('peach")
	   
SyntaxError: EOL while scanning string literal
>>> fruits.add("peach")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    fruits.add("peach")
AttributeError: 'list' object has no attribute 'add'
>>> fruits.extend(["guava","blueberries"])
>>> fruits
['Banana', 'apple', 'mango', 'pineapple', 'berries', 'kiwi', 'grapes', 'guava', 'blueberries']
>>> fruits.remove("Banana")
>>> fruits
['apple', 'mango', 'pineapple', 'berries', 'kiwi', 'grapes', 'guava', 'blueberries']
>>> fruits.delete("guava")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    fruits.delete("guava")
AttributeError: 'list' object has no attribute 'delete'
>>> fruits.del("guava")
SyntaxError: invalid syntax
>>> fruits.sort()
>>> fruits
['apple', 'berries', 'blueberries', 'grapes', 'guava', 'kiwi', 'mango', 'pineapple']
>>> fruits.reverse()
>>> fuits
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    fuits
NameError: name 'fuits' is not defined
>>> fruits
['pineapple', 'mango', 'kiwi', 'guava', 'grapes', 'blueberries', 'berries', 'apple']
>>> fruits.pop()
'apple'
>>> fruits
['pineapple', 'mango', 'kiwi', 'guava', 'grapes', 'blueberries', 'berries']
>>> del fruits[0]
>>> fruits
['mango', 'kiwi', 'guava', 'grapes', 'blueberries', 'berries']
>>> fruits.replace(["mango","tomoko"])
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    fruits.replace(["mango","tomoko"])
AttributeError: 'list' object has no attribute 'replace'
>>> fruits.replace("mango","dates")
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    fruits.replace("mango","dates")
AttributeError: 'list' object has no attribute 'replace'
>>> fruits.replace("mango","Banana")
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    fruits.replace("mango","Banana")
AttributeError: 'list' object has no attribute 'replace'
>>> replace fruits("mango","banana")
SyntaxError: invalid syntax
>>> numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> sum(numbers)
45
>>> sum("fruits")
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    sum("fruits")
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> min(numbers)
0
>>> max(numbers)
9
>>> fruits.append("banana")
>>> fruits.append("mango")
>>> fruits.append("kiwi")
>>> fruits.count("mango")
2
>>> n=range(10)
>>> for x in n:
	print(x)

	
0
1
2
3
4
5
6
7
8
9
>>> m=range(10,20)
>>> for x in n:
	print(x)

	
0
1
2
3
4
5
6
7
8
9
>>> for m in n:
	print(m)

	
0
1
2
3
4
5
6
7
8
9
>>> for f in fruits:
	print(f)

	
mango
kiwi
guava
grapes
blueberries
berries
banana
mango
kiwi
>>> a
[1, 2, 3]
>>> e=[x*10 for x in a]
>>> e
[10, 20, 30]
>>> e=[a*10]
>>> e
[[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]]
>>> f=[x*2 for x in a]
>>> f
[2, 4, 6]
>>> e=[10,20,30]
>>> f=[x*2 for x in e]
>>> f
[20, 40, 60]
>>> g=range(25,50)
>>> g
range(25, 50)
>>> h=[x*2 for x in g]
>>> h
[50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> g=[25,50]
>>> g
[25, 50]
>>> h=[x*x for x in g]
>>> h
[625, 2500]
>>> g=range(25,50)
>>> g
range(25, 50)
>>> h=[x*x for x in g]
>>> h
[625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401]
>>> h[]
SyntaxError: invalid syntax
>>> h=[]
>>> for x in g:
	h.append(x)

	
>>> 
>>> h
[25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> 
>>> h=[]
>>> y=x*x
>>> h.append(y)
>>> h=[x*x for x in y]
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    h=[x*x for x in y]
TypeError: 'int' object is not iterable
>>> h=[x*x for x in y]
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    h=[x*x for x in y]
TypeError: 'int' object is not iterable
>>> h.append(y)
>>> 
>>> 
>>> h
[2401, 2401]
>>> h=[]
>>> for x in g:
	y=x*x
	h.append(y)

	
>>> h
[625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401]
>>> x
49
>>> 49*49
2401
>>> x=[100,200,300,400,500]
>>> y=x//x
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    y=x//x
TypeError: unsupported operand type(s) for //: 'list' and 'list'
>>> y="x"//"x"
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    y="x"//"x"
TypeError: unsupported operand type(s) for //: 'str' and 'str'
>>> y=x%x
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    y=x%x
TypeError: unsupported operand type(s) for %: 'list' and 'list'
>>> y=%x/7
SyntaxError: invalid syntax
>>> y=[z%7 for z in x]
>>> 
>>> y
[2, 4, 6, 1, 3]
>>> y=[z%7]
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    y=[z%7]
NameError: name 'z' is not defined
>>> y=[]
>>> for x in y:
	y=(z%7)
	x.append(y)

	
>>> y
[]
>>> for x in y:
	y=(z%7)
	y.append(x)

	
>>> y
[]
>>> for z in yx
y=(z%7)
	y.append(x)
	
SyntaxError: invalid syntax
>>> for z in x:
	y=(z%7)
	y.append(z)

	
Traceback (most recent call last):
  File "<pyshell#145>", line 3, in <module>
    y.append(z)
AttributeError: 'int' object has no attribute 'append'
>>> for x in y:
	y=z%7
	z.append(y)

	
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    for x in y:
TypeError: 'int' object is not iterable
>>> for z in x:
	y=(z%7)
	y.append(z)

	
Traceback (most recent call last):
  File "<pyshell#152>", line 3, in <module>
    y.append(z)
AttributeError: 'int' object has no attribute 'append'
>>> z
100
>>> y
2
>>> for z in x:
	q=z%
	
SyntaxError: invalid syntax
>>> for z in x:
	q=z%7
	y.append(q)

	
Traceback (most recent call last):
  File "<pyshell#159>", line 3, in <module>
    y.append(q)
AttributeError: 'int' object has no attribute 'append'
>>> y
2
>>> a=range(for x in y:
	y=(z%7)
	y.append(x)
	
SyntaxError: invalid syntax
>>> a=range(99,109)
>>> a
range(99, 109)
>>> b[x*x for x in a]
SyntaxError: invalid syntax
>>> b=[x*x for x in a]
>>> b
[9801, 10000, 10201, 10404, 10609, 10816, 11025, 11236, 11449, 11664]
>>> for m in x:
	f=x*x
	b.append(f)

	
Traceback (most recent call last):
  File "<pyshell#170>", line 2, in <module>
    f=x*x
TypeError: can't multiply sequence by non-int of type 'list'
>>> b=[]
>>> for m in x:
	f=x*x
	b.append(f)

	
Traceback (most recent call last):
  File "<pyshell#175>", line 2, in <module>
    f=x*x
TypeError: can't multiply sequence by non-int of type 'list'
>>> for x in a:
	m=x*x
	b.append(m)

	
>>> b
[9801, 10000, 10201, 10404, 10609, 10816, 11025, 11236, 11449, 11664]
>>> nested=[[1,2,3],[4,5,6],[7,8,9]]
>>> nested
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> flat[1,2,3,4,5,6,7,8]
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    flat[1,2,3,4,5,6,7,8]
NameError: name 'flat' is not defined
>>> flat(1,2,3,4,5,6,7,8,9)
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    flat(1,2,3,4,5,6,7,8,9)
NameError: name 'flat' is not defined
>>>
