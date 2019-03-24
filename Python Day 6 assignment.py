Python 3.8.0a1 (tags/v3.8.0a1:e75eeb00b5, Feb  3 2019, 20:47:39) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for x in range (0,100)
SyntaxError: invalid syntax
>>> for x in range (0,100):
	if x%9==0:
		print(x)

		
0
9
18
27
36
45
54
63
72
81
90
99
>>> for x in range (0,100):
	if x%11==0:
		print(x)

		
0
11
22
33
44
55
66
77
88
99
>>> for x in range (0,100):
	if x%11==0:
		x.extend(x%9==0)

		
Traceback (most recent call last):
  File "<pyshell#10>", line 3, in <module>
    x.extend(x%9==0)
AttributeError: 'int' object has no attribute 'extend'
>>> 9
9
>>> a=()
>>> for in range (0,100):
	
SyntaxError: invalid syntax
>>> for x in range (0,100):
	if x%9==0:
		a.append(x)

		
Traceback (most recent call last):
  File "<pyshell#17>", line 3, in <module>
    a.append(x)
AttributeError: 'tuple' object has no attribute 'append'
>>> a=[]
>>> if x%9==0:
	a.append(x)

	
>>> a
[0]
>>> a=[]
>>> for x in range(0,100):
	if x%9==0:
		a.append(x)

		
>>> a
[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]
>>> b=[]
>>> for x in range(0,100):
	if x%11==0:
		a.append(x)

		
>>> b
[]
>>> for x in range(0,100):
	if x%11==0:
		b.append(x)

		
>>> b
[0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> c=a+b
>>> c
[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> c.sort()
>>> 
>>> c
[0, 0, 0, 9, 11, 11, 18, 22, 22, 27, 33, 33, 36, 44, 44, 45, 54, 55, 55, 63, 66, 66, 72, 77, 77, 81, 88, 88, 90, 99, 99, 99]
>>> a=[]
>>> b=[]
>>> for x in range(0,100):
	if x%11==0:
		a.append(x)
	elif x%9==0:
		b.append(x)

		
>>> a
[0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> b
[9, 18, 27, 36, 45, 54, 63, 72, 81, 90]
>>> c=a+b
>>> c
[0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90]
>>> c.sort()
>>> c
[0, 9, 11, 18, 22, 27, 33, 36, 44, 45, 54, 55, 63, 66, 72, 77, 81, 88, 90, 99]
>>> student1={"name":"Beatrice","Yob"=1996
	  
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> student1 = {"name": "Beatrice", "yob" :1996}
>>> student2 = {"name": "Stephen", "yob" : 1973}
>>> student3 = {"name": "James", "yob" : 1995}
>>> student4 = {"name": "Michael", "yob" : 2000}
>>> student5 = {"name": "Alice", "yob" : 1975}
>>> students=[student1,student2,student3,student4,student5]
SyntaxError: multiple statements found while compiling a single statement
>>> student1 = {"name":"beatrice","yob" :1996}
>>> student2 = {"name":"James","yob" :1997}
>>> student3 = {"name":"Michael","yob" :1994}
>>> student4 = {"name":"Alice","yob" :1974}
>>> student5 = {"name":"Stephen","yob" :1972}
>>> students = [student1,student2,student3,student4,student5]
>>> year = 365 days
SyntaxError: invalid syntax
>>> student1 = {"name": "Beatrice", "yob" :1996}
>>> student2 = {"name": "Stephen", "yob" : 1973}
>>> student3 = {"name": "James", "yob" : 1995}
>>> student4 = {"name": "Michael", "yob" : 2000}
>>> student5 = {"name": "Alice", "yob" : 1975}
>>> 
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> 
>>> 
>>> student1 = {"name":"beatrice","yob" :1996}
>>> student2 = {"name":"James","yob" :1997}
>>> student3 = {"name":"Michael","yob" :1994}
>>> student4 = {"name":"Alice","yob" :1974}
>>> student5 = {"name":"Stephen","yob" :1972}
>>> 
>>> 
>>> students = [student1,student2,student3,student4,student5]
>>> students
[{'name': 'beatrice', 'yob': 1996}, {'name': 'James', 'yob': 1997}, {'name': 'Michael', 'yob': 1994}, {'name': 'Alice', 'yob': 1974}, {'name': 'Stephen', 'yob': 1972}]
>>> for student in students:
	age=(2019-student["yob"])*365
	message="Hi {}, you are {} days old".format(student["name"],age)

	
>>> print(message)
Hi Stephen, you are 17155 days old
>>> for student in students:
	age=(2019-student["yob"])*365
	message="Hi {}, you are {} days old".format(student["name"],age)
	print(message)

	
Hi beatrice, you are 8395 days old
Hi James, you are 8030 days old
Hi Michael, you are 9125 days old
Hi Alice, you are 16425 days old
Hi Stephen, you are 17155 days old
>>> for x in range(2019,2119)
SyntaxError: invalid syntax
>>> for x in range(2019,2119):
	if x%4==0:
		print(x)

		
2020
2024
2028
2032
2036
2040
2044
2048
2052
2056
2060
2064
2068
2072
2076
2080
2084
2088
2092
2096
2100
2104
2108
2112
2116
>>> 
