Python 3.8.0a1 (tags/v3.8.0a1:e75eeb00b5, Feb  3 2019, 20:47:39) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=1
>>> b=2
>>> c=3
>>> d=8
>>> a
1
>>> name="Beatrice"
>>> balance="1,000,000"
>>> code="ABC456"
>>> print("{} confirmed. \n Hi {}, your balance is {} \n Thank you".format(code,name,Balance))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print("{} confirmed. \n Hi {}, your balance is {} \n Thank you".format(code,name,Balance))
NameError: name 'Balance' is not defined
>>> print("{} confirmed. \n Hi {}, your balance is {} \n Thank you".format(code,name,Balance))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print("{} confirmed. \n Hi {}, your balance is {} \n Thank you".format(code,name,Balance))
NameError: name 'Balance' is not defined
>>> print("{} confirmed. \n Hi {}, your balance is {} \n Thank you".format(code,name,balance))
ABC456 confirmed. 
 Hi Beatrice, your balance is 1,000,000 
 Thank you
>>> print("{} confirmed!\n Hi {}, yor blance is {}\n. Thank you.".format(code,name,balance))
ABC456 confirmed!
 Hi Beatrice, yor blance is 1,000,000
. Thank you.
>>> a=[[1,2,3] [4,5,6] [7,8,9]]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a=[[1,2,3] [4,5,6] [7,8,9]]
TypeError: list indices must be integers or slices, not tuple
>>> A = [[1,2,3] [4,5,6] [7,8,9]]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    A = [[1,2,3] [4,5,6] [7,8,9]]
TypeError: list indices must be integers or slices, not tuple
>>> A = [[1,2,3],[4,5,6],[7,8,9]]
>>> f = 1
>>> print(A)
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> for i in range(0,3):
	f *= 10
	for j in range(0,3):
		A[i][j] *= f
    print (A)
    
SyntaxError: unindent does not match any outer indentation level
>>> for i in range(0,3):
	f *= 10
	for j in range(0,3):
		A[i][j] *= f

>>> print (A)
[[10, 20, 30], [400, 500, 600], [7000, 8000, 9000]]
>>> fruit = ["Mango,Banana,Orange,Melon,Avocado"]
>>> for fruit in fruits:
	print (fruit)

	
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    for fruit in fruits:
NameError: name 'fruits' is not defined
>>> for fruit in fruit:
	print (fruit)

	
Mango,Banana,Orange,Melon,Avocado
>>> fruit = ["Mango","Banana","Orange","Melon","Avocado"]
>>> for fruit in fruit:
	print (fruit)

	
Mango
Banana
Orange
Melon
Avocado
>>> fruit = ['Mango','Banana','Orange','Melon','Avocado']
>>> for fruit in fruit:
	print (fruit)

	
Mango
Banana
Orange
Melon
Avocado
>>> numbers = [1,2,3,4,5,6,7,8,9]
>>> for number in numbers:
	print (numbers)

	
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> for number in numbers:
	print (number)

	
1
2
3
4
5
6
7
8
9
>>> fruit [2]
'o'
>>> fruit [1]
'v'
>>> for fruit in fruit:
	print (fruit)

	
A
v
o
c
a
d
o
>>> fruit [0:]
'o'
>>> fruit = ['Mango','Banana','Orange','Melon','Avocado']
>>> for fruits in fruit:
	print (fruit)

	
['Mango', 'Banana', 'Orange', 'Melon', 'Avocado']
['Mango', 'Banana', 'Orange', 'Melon', 'Avocado']
['Mango', 'Banana', 'Orange', 'Melon', 'Avocado']
['Mango', 'Banana', 'Orange', 'Melon', 'Avocado']
['Mango', 'Banana', 'Orange', 'Melon', 'Avocado']
>>> print [4:]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print [4:]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> print [4"5]
       
SyntaxError: Missing parentheses in call to 'print'. Did you mean print([4"5])?
>>> print [4:5]
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    print [4:5]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> for fruit in fruit:
	print (fruit)

	
Mango
Banana
Orange
Melon
Avocado
>>> fruit [0]
'A'
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> c=a+b
>>> c
[1, 2, 3, 4, 5, 6]
>>> d=a-b
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    d=a-b
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> d=b+a
>>> d
[4, 5, 6, 1, 2, 3]
>>> e=a*8
>>> e
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> fruit
'Avocado'
>>> fruits = ['mango','melon','orange','grapes','avocado']
>>> fruits
['mango', 'melon', 'orange', 'grapes', 'avocado']
>>> fruits.append("banana")
>>> fruits
['mango', 'melon', 'orange', 'grapes', 'avocado', 'banana']
>>> fruits.extend(["blueberries","peas"])
>>> fruits
['mango', 'melon', 'orange', 'grapes', 'avocado', 'banana', 'blueberries', 'peas']
>>> fruits.remove("banana")
>>> fruits
['mango', 'melon', 'orange', 'grapes', 'avocado', 'blueberries', 'peas']
>>> fruits.remove(["peas","blueberries"])
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    fruits.remove(["peas","blueberries"])
ValueError: list.remove(x): x not in list
>>> fruits.remove("peas","blueberries")
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    fruits.remove("peas","blueberries")
TypeError: remove() takes exactly one argument (2 given)
>>> fruits
['mango', 'melon', 'orange', 'grapes', 'avocado', 'blueberries', 'peas']
>>> fruits.sort ()
>>> fruits
['avocado', 'blueberries', 'grapes', 'mango', 'melon', 'orange', 'peas']
>>> fruits.reverse ()
>>> fruits
['peas', 'orange', 'melon', 'mango', 'grapes', 'blueberries', 'avocado']
>>> fruits.pop ()
'avocado'
>>> fruits
['peas', 'orange', 'melon', 'mango', 'grapes', 'blueberries']
>>> del fruits [0]
>>> fruit
'Avocado'
>>> numbers
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> min(numbers)
1
>>> max(numbers)
9
>>> count ()
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    count ()
NameError: name 'count' is not defined
>>> count (numbers)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    count (numbers)
NameError: name 'count' is not defined
>>> count(numbers)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    count(numbers)
NameError: name 'count' is not defined
>>> fruits.count(fruits)
0
>>> fruits
['orange', 'melon', 'mango', 'grapes', 'blueberries']
>>> fruits.append("banana")
>>> fruits.append("peas")
>>> fruits.count(fruits)
0
>>> fruits.append("banana")
>>> fruits.count("banana")
2
>>> n=range(10)
>>> for x in in:
	
SyntaxError: invalid syntax
>>> for x in n:
	print (x)

	
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
>>> kasembi=range(20)
>>> for x in kasembi:
	print (kasembi)

	
range(0, 20)
range(0, 20)
range(0, 20)
range(0, 20)
range(0, 20)
range(0, 20)
range(0, 20)
range(0, 20)
range(0, 20)
range(0, 20)
range(0, 20)
range(0, 20)
range(0, 20)
range(0, 20)
range(0, 20)
range(0, 20)
range(0, 20)
range(0, 20)
range(0, 20)
range(0, 20)
>>> kasembi=range(0,20)
	for x in kasembi:
	print (kasembi)
	
SyntaxError: multiple statements found while compiling a single statement
>>> m=range(10,20)
>>> for x in m:
	print (m)

	
range(10, 20)
range(10, 20)
range(10, 20)
range(10, 20)
range(10, 20)
range(10, 20)
range(10, 20)
range(10, 20)
range(10, 20)
range(10, 20)
>>> for x in m:
	print(m)

	
range(10, 20)
range(10, 20)
range(10, 20)
range(10, 20)
range(10, 20)
range(10, 20)
range(10, 20)
range(10, 20)
range(10, 20)
range(10, 20)
>>> for f in fruits:
	print (f)

	
orange
melon
mango
grapes
blueberries
banana
peas
banana
>>> a
[1, 2, 3]
>>> e=[a*10]
>>> e
[[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]]
>>> e=[a*10 for x in a]
>>> e
[[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]]
>>> e=[x*10 for x in a]
>>> e
[10, 20, 30]
>>> f=[x+10 for x in a]
>>> f
[11, 12, 13]
>>> f=[x//10 for x in a]
>>> f
[0, 0, 0]
>>> f=[10,20,30]
>>> g=[x*x for x in f]
>>> g
[100, 400, 900]
>>> h=range(25,50)
>>> i=[x*x for x in h]
>>> i
[625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401]
>>> j=range(50,100)
>>> k=[x/5 for x in j]
>>> k
[10.0, 10.2, 10.4, 10.6, 10.8, 11.0, 11.2, 11.4, 11.6, 11.8, 12.0, 12.2, 12.4, 12.6, 12.8, 13.0, 13.2, 13.4, 13.6, 13.8, 14.0, 14.2, 14.4, 14.6, 14.8, 15.0, 15.2, 15.4, 15.6, 15.8, 16.0, 16.2, 16.4, 16.6, 16.8, 17.0, 17.2, 17.4, 17.6, 17.8, 18.0, 18.2, 18.4, 18.6, 18.8, 19.0, 19.2, 19.4, 19.6, 19.8]
>>> k=[x/%5 for x in j]
SyntaxError: invalid syntax
>>> i=[]
>>> for x in h:
	h.append (x)

	
Traceback (most recent call last):
  File "<pyshell#146>", line 2, in <module>
    h.append (x)
AttributeError: 'range' object has no attribute 'append'
>>> for x in h:
	i.append(x)

	
>>> i
[25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> h=range(25,50)
>>> l=[x*x for x in h]
>>> l
[625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401]
>>> l[]
SyntaxError: invalid syntax
>>> l []
SyntaxError: invalid syntax
>>> l[]
SyntaxError: invalid syntax
>>> l[]
SyntaxError: invalid syntax
>>> l=[]
>>> for x in h:
	l.append(x)

	
>>> 
>>> l
[25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> flat=[[1,2,3],[4,5,6],[7,8,9]
      a=[1,2,3]
      
SyntaxError: invalid syntax
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> c=[7,8,9]
>>> d=a+b+c
\
>>> d
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> e=[x*x for x in d]
>>> e
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
