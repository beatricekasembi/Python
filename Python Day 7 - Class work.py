Python 3.8.0a1 (tags/v3.8.0a1:e75eeb00b5, Feb  3 2019, 20:47:39) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def hello():
	print("hello Akirachix")

	
>>> hello()
hello Akirachix
>>> def hello(This is my program):
	print("hello Akirachix")
	
SyntaxError: invalid syntax
>>> def hello(name):
	print("hello {}".format(name))

	
>>> hello("James")
hello James
>>> hello("Beatrice")
hello Beatrice
>>> hello("Michael")
hello Michael
>>> hello("Alice")
hello Alice
>>> hello("Stephen")
hello Stephen
>>> def sum(a,b):
	answer=a+b
	return answer

>>> sum(a,b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    sum(a,b)
NameError: name 'a' is not defined
>>> sum
<function sum at 0x0000007CE5262940>
>>> sum(10,50)

	return answer
SyntaxError: multiple statements found while compiling a single statement
>>> sum(1000,1000)
2000
>>> sum(50,40)
90
>>> sum(5000000,4000000)
9000000
>>> def sum(a,b):
	answer=a/b
	return answer

>>> sum(500,5)
100.0
>>> sum(4800000,92)
52173.913043478264
>>> def sum(a,b):
	answer=a//b
	return answer

>>> sum(4800000,92)
52173
>>> sum(1000000,52)
19230
>>> def sum(a,b):
	answer=a%b
	return answer

>>> sum(500000,5)
0
>>> sum(4700,4)
0
>>> sum(33,10)
3
>>> def sum(a,b):
	answer=a-b
	return answer

>>> sum(52,7)
45
>>> sum(100,9)
91
>>> 
def sum(a,b):
	answer=a*b
	return answer

>>> sum(50,70)
3500
>>> sum(900,730)
657000
>>> def sum(a,b):
	answer=a**b
	return answer

>>> sum(7,3)
343
>>> sum(2,3)
8
>>> sum(2,3,3)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    sum(2,3,3)
TypeError: sum() takes 2 positional arguments but 3 were given
>>> def sum(a,b):
	answer=a*b
	return answer

>>> sum(2,3,5)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    sum(2,3,5)
TypeError: sum() takes 2 positional arguments but 3 were given
>>> def sum(a,b,c):
	answer=a*b
	return answer

>>> sum(2,5,7)
10
>>> def sum(a,b,c):
	answer=a*b*c
	return answer

>>> sum(4,5,6)
120
>>> def hello(name,year):
	print("hello {}".format(name,year))

	
>>> hello("Beatrice","year")
hello Beatrice
>>> def hello(name,year):
	print("hello {},you are {} years old.".format(name,year))

	
>>> hello("Beatrice","year")
hello Beatrice,you are year years old.
>>> def hello(name,year):
	print("hello {},you are {} years old.".format(name,year))

	
>>> hello("Beatrice","22")
hello Beatrice,you are 22 years old.
>>> def hello(name,year):
	for year in range(1996,2019)
	print("hello {},you are {} years old.".format(name,year))
	
SyntaxError: invalid syntax
>>> def hello(name,year):
	for year in range(1996,2019):
	print("hello {},you are {} years old.".format(name,year))
	
SyntaxError: expected an indented block
>>> def hello(name,year):
	for year in range(1996,2019):
		print("hello {},you are {} years old.".format(name,year))

		
>>> hello("Beatrice","year")
hello Beatrice,you are 1996 years old.
hello Beatrice,you are 1997 years old.
hello Beatrice,you are 1998 years old.
hello Beatrice,you are 1999 years old.
hello Beatrice,you are 2000 years old.
hello Beatrice,you are 2001 years old.
hello Beatrice,you are 2002 years old.
hello Beatrice,you are 2003 years old.
hello Beatrice,you are 2004 years old.
hello Beatrice,you are 2005 years old.
hello Beatrice,you are 2006 years old.
hello Beatrice,you are 2007 years old.
hello Beatrice,you are 2008 years old.
hello Beatrice,you are 2009 years old.
hello Beatrice,you are 2010 years old.
hello Beatrice,you are 2011 years old.
hello Beatrice,you are 2012 years old.
hello Beatrice,you are 2013 years old.
hello Beatrice,you are 2014 years old.
hello Beatrice,you are 2015 years old.
hello Beatrice,you are 2016 years old.
hello Beatrice,you are 2017 years old.
hello Beatrice,you are 2018 years old.
>>> def hello(name,year=a-b):
		print("hello {},you are {} years old.".format(name,year))

		
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    def hello(name,year=a-b):
NameError: name 'a' is not defined
>>> def hello(name,age):
	age=(2019-year)
	print("hello {},you are {} years old.".format(name,age))

	
>>> hello("Beatrice","age")
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    hello("Beatrice","age")
  File "<pyshell#75>", line 2, in hello
    age=(2019-year)
NameError: name 'year' is not defined
>>> def hello(name,age):
	year=1996
	age=(2019-year)
	print("hello {},you are {} years old.".format(name,age))

	
>>> hello("Beatrice","age")
hello Beatrice,you are 23 years old.
>>> hello("James","age")
hello James,you are 23 years old.
>>> def hello(name,age):
	year range(1996,2019)
	age=(2019-year)
	print("hello {},you are {} years old.".format(name,age))
	
SyntaxError: invalid syntax
>>> 
>>> def hello(name,age):
	year in range(1996,2019)
	age=(2019-year)
	print("hello {},you are {} years old.".format(name,age))

	
>>> hello("Beatrice","age")
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    hello("Beatrice","age")
  File "<pyshell#84>", line 2, in hello
    year in range(1996,2019)
NameError: name 'year' is not defined
>>> def hello(name,age):
	for year in range(1996,2019)
	age=(2019-year)
	print("hello {},you are {} years old.".format(name,age))
	
SyntaxError: invalid syntax
>>> def hello(name,age):
	for year in range(1996,2019):
	age=(2019-year)
	print("hello {},you are {} years old.".format(name,age))
	
SyntaxError: expected an indented block
>>> def hello(name,age):
	for year in range(1996,2019):
		age=(2019-year)
			print("hello {},you are {} years old.".format(name,age))
			
SyntaxError: unexpected indent
>>> def hello(name,age):
	for year in range(1996,2019):
		age=(2019-year)
		print("hello {},you are {} years old.".format(name,age))

		
>>> hello("Beatrice","age")
hello Beatrice,you are 23 years old.
hello Beatrice,you are 22 years old.
hello Beatrice,you are 21 years old.
hello Beatrice,you are 20 years old.
hello Beatrice,you are 19 years old.
hello Beatrice,you are 18 years old.
hello Beatrice,you are 17 years old.
hello Beatrice,you are 16 years old.
hello Beatrice,you are 15 years old.
hello Beatrice,you are 14 years old.
hello Beatrice,you are 13 years old.
hello Beatrice,you are 12 years old.
hello Beatrice,you are 11 years old.
hello Beatrice,you are 10 years old.
hello Beatrice,you are 9 years old.
hello Beatrice,you are 8 years old.
hello Beatrice,you are 7 years old.
hello Beatrice,you are 6 years old.
hello Beatrice,you are 5 years old.
hello Beatrice,you are 4 years old.
hello Beatrice,you are 3 years old.
hello Beatrice,you are 2 years old.
hello Beatrice,you are 1 years old.
>>> def age(name,age):
	age=(2019-year)
	print("hello {},you are {} years old.".format(name,age))

	
>>> age("Beatrice",1993)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    age("Beatrice",1993)
  File "<pyshell#93>", line 2, in age
    age=(2019-year)
NameError: name 'year' is not defined
>>> hello("Beatrice","age")
hello Beatrice,you are 23 years old.
hello Beatrice,you are 22 years old.
hello Beatrice,you are 21 years old.
hello Beatrice,you are 20 years old.
hello Beatrice,you are 19 years old.
hello Beatrice,you are 18 years old.
hello Beatrice,you are 17 years old.
hello Beatrice,you are 16 years old.
hello Beatrice,you are 15 years old.
hello Beatrice,you are 14 years old.
hello Beatrice,you are 13 years old.
hello Beatrice,you are 12 years old.
hello Beatrice,you are 11 years old.
hello Beatrice,you are 10 years old.
hello Beatrice,you are 9 years old.
hello Beatrice,you are 8 years old.
hello Beatrice,you are 7 years old.
hello Beatrice,you are 6 years old.
hello Beatrice,you are 5 years old.
hello Beatrice,you are 4 years old.
hello Beatrice,you are 3 years old.
hello Beatrice,you are 2 years old.
hello Beatrice,you are 1 years old.
>>> def age(name,year):
	x=(2019-year)
	print("hello {},you are {} years old.".format(name,x))

	
>>> age("beatrice",2001)
hello beatrice,you are 18 years old.
>>> def squares(numbers):
	for number in numbers:
		print(number*number)

		
>>> x=[1,2,3,4,5]
>>> y=[100,200,300,400]
>>> squares(x)
1
4
9
16
25
>>> squares(y)
10000
40000
90000
160000
>>> z=['a','b','c','d','e']
>>> squares(z)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    squares(z)
  File "<pyshell#102>", line 3, in squares
    print(number*number)
TypeError: can't multiply sequence by non-int of type 'str'
>>> def squares(strings):
	for string in strings:
		print(string*string)

		
>>> z=['a','b','c','d','e']
>>> z
['a', 'b', 'c', 'd', 'e']
>>> squares(z)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    squares(z)
  File "<pyshell#110>", line 3, in squares
    print(string*string)
TypeError: can't multiply sequence by non-int of type 'str'
>>> def squares(numbers):
	a=[]
	for number in numbers:
		s=number*number
		a.append(s)

		
>>> return a
SyntaxError: 'return' outside function
>>> def squares(numbers):
	a=[]
	for number in numbers:
		s=number*number
		a.append(s)
		return a

	
>>> a
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a=[2,3,4,5,6,7,8,9]
>>> a
[2, 3, 4, 5, 6, 7, 8, 9]
>>> def squares(numbers):
	a=[]
	for number in numbers:
		s=number*number
		a.append(s)
		return a

	
>>> squares
<function squares at 0x0000007CE5C6F540>
>>> a=[]
>>> def squares(numbers):
	x=[]
	for number in numbers:
		s=number*number
		x.append(s)
		return a

	
>>> squares()
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    squares()
TypeError: squares() missing 1 required positional argument: 'numbers'
>>> squares(numbers)
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    squares(numbers)
NameError: name 'numbers' is not defined
>>> def squares(numbers):
	a=[]
	for number in numbers:
		s=number*number
		a.append(s)

		
>>> def squares(numbers):
	a=[]
	for number in numbers:
		s=number*number
		a.append(s)
	return a

>>> squares(numbers)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    squares(numbers)
NameError: name 'numbers' is not defined
>>> squares(x)
[1, 4, 9, 16, 25]
>>> squares(y)
[10000, 40000, 90000, 160000]
>>> 
def tens(numbers):
	a=[]
	for number in numbers:
		s=number*10
		a.append(s)
	return a

>>> squares(x)
[1, 4, 9, 16, 25]
>>> tens(x)
[10, 20, 30, 40, 50]
>>> tens(y)
[1000, 2000, 3000, 4000]
>>> 
