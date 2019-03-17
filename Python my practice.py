Python 3.8.0a1 (tags/v3.8.0a1:e75eeb00b5, Feb  3 2019, 20:47:39) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Twinkle, twinkle, little star, \n \t How i wonder what you are! \n \t up above the world so high, \n Like a diamond in the sky. \n Twinkle, twinkle, little star,\n \t How i wonder what you are.")
Twinkle, twinkle, little star, 
 	 How i wonder what you are! 
 	 up above the world so high, 
 Like a diamond in the sky. 
 Twinkle, twinkle, little star,
 	 How i wonder what you are.
>>> import sys
>>> print("python version")
python version
>>> print(sys.version)
3.8.0a1 (tags/v3.8.0a1:e75eeb00b5, Feb  3 2019, 20:47:39) [MSC v.1916 64 bit (AMD64)]
>>> pprint("Version info.")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    pprint("Version info.")
NameError: name 'pprint' is not defined
>>> print("Version info.")
Version info.
>>> print(sys.version_info)
sys.version_info(major=3, minor=8, micro=0, releaselevel='alpha', serial=1)
>>> print("2014-07-05 14:34:14")
2014-07-05 14:34:14
>>> r=1.1
>>> area=3
>>> area=3.8013271108436504
>>> r
1.1
>>> area
3.8013271108436504
>>> from math import pi
>>> r= float(input ("input the radius of the circle:"))
input the radius of the circle: 1.1
>>> print ("The area of the circle with radius " + str (r) + " is: " + str(pi * r**2))
The area of the circle with radius 1.1 is: 3.8013271108436504
>>> import datetime
>>> now = datetime.datetime.now()
>>> print ("Current date and time : ")
Current date and time : 
>>> print (now.strftime("%Y-%m-%d %H:%M:%S"))
2019-03-14 11:45:26
>>> first name="Beatrice"
SyntaxError: invalid syntax
>>> first="Beatrice"
>>> last="Kasembi"
>>> names="first"+"last"
>>> names
'firstlast'
>>> first
'Beatrice'
>>> last
'Kasembi'
>>> names=("first"+"last")
>>> names
'firstlast'
>>> print .reverse .formart(first,last)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print .reverse .formart(first,last)
AttributeError: 'builtin_function_or_method' object has no attribute 'reverse'
>>> print () .format(first,last)

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print () .format(first,last)
AttributeError: 'NoneType' object has no attribute 'format'
>>> fname = input("input your First Name : ")
input your First Name : Beatrice
>>> lname = input("inpute your Last Name : ")
inpute your Last Name : Kasembi
>>> print("Hello " + lname + " "+ fname)
Hello Kasembi Beatrice
>>> print("Hello" .format(last,first))
Hello
>>> print("Hello".format(last,first))
Hello
>>> print("Hello {} {}".format(last,first))
Hello Kasembi Beatrice
>>> 
