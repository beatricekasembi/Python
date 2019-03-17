Python 3.8.0a1 (tags/v3.8.0a1:e75eeb00b5, Feb  3 2019, 20:47:39) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=2
>>> b=3
>>> c="girl"
>>> d="boy"
>>> a
2
>>> b
3
>>> c
'girl'
>>> d
'boy'
>>> a+b
5
>>> e+f
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    e+f
NameError: name 'e' is not defined
>>> e=a**b
>>> e
8
>>> type(a)
<class 'int'>
>>> type(b)
<class 'int'>
>>> type(c)
<class 'str'>
>>> type(d)
<class 'str'>
>>> type(e)
<class 'int'>
>>> f=10/b
>>> f
3.3333333333333335
>>> type(f)
<class 'float'>
>>> g=10//b
>>> g
3
>>> type(g)
<class 'int'>
>>> str(a)
'2'
>>> h=str(b)
>>> h
'3'
>>> type(h)
<class 'str'>
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    int(d)
ValueError: invalid literal for int() with base 10: 'boy'
>>> i="123"
>>> i
'123'
>>> type(i)
<class 'str'>
>>> j=int(i)
>>> j
123
>>> type(j)
<class 'int'>
>>> 
>>> float(3)
3.0
>>> print("hello akirachix")
hello akirachix
>>> print(hello akirachix.\n 2019")
      
SyntaxError: invalid syntax
>>> print("hello akirachix. \n 2019")
hello akirachix. 
 2019
>>> print("my names are: \n Beatrice \n Kasembi")
my names are: 
 Beatrice 
 Kasembi
>>> print("haha\a")
haha
>>> print("haha \a")
haha 
>>> print("hello \t akirachix")
hello 	 akirachix
>>> print("hello \v akirachix")
hello  akirachix
>>> school="akirachix"
>>> school
'akirachix'
>>> school.upper()
'AKIRACHIX'
>>> school.lower()
'akirachix'
>>> s=" i love akirachix"
>>> s
' i love akirachix'
>>> s.upper()
' I LOVE AKIRACHIX'
>>> s.lower()
' i love akirachix'
>>> s.capitalize()
' i love akirachix'
>>> school.capitalize
<built-in method capitalize of str object at 0x000000E86F29B230>
>>> school.capitalize()
'Akirachix'
>>> school.endswith("x")
True
>>> school.endswith("z")
False
>>> school.startswith("b")
False
>>> school.startswith(:A")
		  
SyntaxError: invalid syntax
>>> school.startswith("A")
False
>>> s.is numeric()
SyntaxError: invalid syntax
>>> s.isnumeric()
False
>>> school.isalpha()
True
>>> school.upper()
'AKIRACHIX'
>>> school.isupper()
False
>>> school.islower()
True
>>> a="AKIRACHIX"
>>> B="akirachix"
>>> a.isupper()
True
>>> B.islower()
True
>>> first="Beatrice"
>>> last="Kasembi"
>>> print(hello{}{}, welcome to {}".format(first,last,school)
      
SyntaxError: invalid syntax
>>> school="akirachix"
>>> print(Hello{}{}, welcome to {}". format(first,last,school))
      
SyntaxError: invalid syntax
>>> print(hello{}{},welcometo{}".format(first,last,school))
      
SyntaxError: invalid syntax
>>> first
'Beatrice'
>>> last
'Kasembi'
>>> school
'akirachix'
>>> print(hello{}{}, welcome to {}". format (first,last,school)
      
SyntaxError: invalid syntax
>>> print("hello{}{},welcome to {}".format(first,last,school))
helloBeatriceKasembi,welcome to akirachix
>>> year="1996"
>>> year
'1996'
>>> print("hello {}{}, you are {} years old")
hello {}{}, you are {} years old
>>> print("hello {}{}, you are {}". format(first,last,year))
hello BeatriceKasembi, you are 1996
>>> age="23"
>>> age
'23'
>>> print("hello {}{}, you are {} years old". formart(first,last,age))
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    print("hello {}{}, you are {} years old". formart(first,last,age))
AttributeError: 'str' object has no attribute 'formart'
>>> print("hello {}{}, you are {} years old". format(first,last,age))
hello BeatriceKasembi, you are 23 years old
>>> c1="Kenya"
>>> c2="Uganda"
>>> c3="Tanzania"
>>> Ke_code="254"
>>> Ug_code="256"
>>> Tz_code="255"
>>> c1
'Kenya'
>>> c2
'Uganda'
>>> c3
'Tanzania'
>>> Ke_code
'254'
>>> Ug_code
'256'
>>> Tz_code
'255'
>>> print("{} code is {}". format(c1,Ke_code))
Kenya code is 254
>>> print(" {} code is {}". format(c2, Ug_code))
 Uganda code is 256
>>> print(" {} code is {}". format(c3,Tz_code))
 Tanzania code is 255
>>> print("The codes of {},{} and {} are {},{} and {} respecively". format(c1,c2c3,Ke_code,Ug_code,Tz_code))
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    print("The codes of {},{} and {} are {},{} and {} respecively". format(c1,c2c3,Ke_code,Ug_code,Tz_code))
NameError: name 'c2c3' is not defined
>>> print("The codes of {},{},{} are {},{},{} respectively". format(c1,c2,c3,Ke_code,Ug_code,Tz_code))
The codes of Kenya,Uganda,Tanzania are 254,256,255 respectively
>>> print("I love my country {} as well as {} "and" {}". format(c1,c2,c3))
 Kenya
>>> print("I love my country {}, as well as {}". format(c1,c2))
I love my country Kenya, as well as Uganda
>>> 
