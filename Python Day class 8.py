Python 3.8.0a1 (tags/v3.8.0a1:e75eeb00b5, Feb  3 2019, 20:47:39) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> first = "Beatrice"
>>> def initial (a):
	a=[]
	for x in a:
		print[0]

		
>>> a
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> def initial (a):
	a=[]
	for x in first:
		print[0]

		
>>> a
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> "Beatrice"[0]
'B'
>>> second = "Kasembi"
>>> "Kasembi"[0]
'K'
>>> def initial (a):
	a=(first,second)
	for x in a:
		print(first[0],second[0])

		
>>> a
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> def initials(first,second)
SyntaxError: invalid syntax
>>> def initials(first,second):
	a=first[0]
	b=second[0]
	ans=a+b
	return ans

>>> ans
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    ans
NameError: name 'ans' is not defined
>>> initials
<function initials at 0x0000000BAF2330C0>
>>> initials(first,second)
'BK'
>>> 
