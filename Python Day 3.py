Python 3.8.0a1 (tags/v3.8.0a1:e75eeb00b5, Feb  3 2019, 20:47:39) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> code
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    code
NameError: name 'code' is not defined
>>> code "ABC123"
SyntaxError: invalid syntax
>>> code="ABC123"
>>> name="Beatrice"
>>> Balance="1000"
>>> print("{} confirmed. \n Hi {}, your balance is {} \n Thank you".format(code,name,Balance))
ABC123 confirmed. 
 Hi Beatrice, your balance is 1000 
 Thank you
>>> Name="Beatrice"
>>> Age="23"
>>> Home="Kasarani"
>>> Hobby="Dancing"
>>> print("I am {},aged {} years old.I come from {} and i love {}".format(Name,Age,Home,Hobby))
I am Beatrice,aged 23 years old.I come from Kasarani and i love Dancing
>>> sms= "{} confirmed. \n Hi {}, your balance is {} \n Thank you".format(code,name,Balance)
>>> sms
'ABC123 confirmed. \n Hi Beatrice, your balance is 1000 \n Thank you'
>>> sms="{} confirmed. \n Hi {}, your balance is {} \n Thank you".format(code,name,Balance))
SyntaxError: unmatched ')'
>>> sms="{} confirmed. \n Hi {}, your balance is {} \n Thank you".format(code,name,Balance)
>>> print sms
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(sms)?
>>> print (sms)
ABC123 confirmed. 
 Hi Beatrice, your balance is 1000 
 Thank you
>>> s="Akirachix"
>>> s[0]
'A'
>>> s[7)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> s[7]
'i'
>>> s[0:2]
'Ak'
>>> s[2:6]
'irac'
>>> s[3:7]
'rach'
>>> s[7:3]
''
>>> s[3:]
'rachix'
>>> s[0:6]
'Akirac'
>>> s[:6]
'Akirac'
>>> s[-9]
'A'
>>> s[-9]==s[0]
True
>>> s[-9:-7]
'Ak'
>>> s=[0:2]==s[-9:-7]
SyntaxError: invalid syntax
>>> s[0:2]==s[-9:-7]
True
>>> s[1:5]==s[-8:-4]
True
>>> s.Akirachix("k")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s.Akirachix("k")
AttributeError: 'str' object has no attribute 'Akirachix'
>>> s.index("k")
1
>>> s.index("x")
8
>>> sms="ABCD123. Confirmed! Hi Beatrice, your balance is 1,000."
>>> sms[0:7]
'ABCD123'
>>> sms[0:20]
'ABCD123. Confirmed! '
>>> sms[:60]
'ABCD123. Confirmed! Hi Beatrice, your balance is 1,000.'
>>> sms[21:28]
'i Beatr'
>>> sms[18:25]
'! Hi Be'
>>> sms[20:30]
'Hi Beatric'
>>> sms[26:33]
'trice, '
>>> sms[23:35]
'Beatrice, yo'
>>> sms[0:20]
'ABCD123. Confirmed! '
>>> sms[0:30]
'ABCD123. Confirmed! Hi Beatric'
>>> sms[21:31]
'i Beatrice'
>>> sms[23:32]
'Beatrice,'
>>> sms[21:32]
'i Beatrice,'
>>> sms[24:31]
'eatrice'
>>> sms[24:30]
'eatric'
>>> sms[21:30]
'i Beatric'
>>> sms[22:31]
' Beatrice'
>>> sms[0:]
'ABCD123. Confirmed! Hi Beatrice, your balance is 1,000.'
>>> sms[51:56]
'000.'
>>> sms[51:57]
'000.'
>>> sms[50:56]
',000.'
>>> sms[49:56]
'1,000.'
>>> sms
'ABCD123. Confirmed! Hi Beatrice, your balance is 1,000.'
>>> sms.upper()
'ABCD123. CONFIRMED! HI BEATRICE, YOUR BALANCE IS 1,000.'
>>> sms.captalize()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    sms.captalize()
AttributeError: 'str' object has no attribute 'captalize'
>>> sms.lower()
'abcd123. confirmed! hi beatrice, your balance is 1,000.'
>>> sms.endswith "0"
SyntaxError: invalid syntax
>>> sms.endswith() "b"
SyntaxError: invalid syntax
>>> sms.isnumeric
<built-in method isnumeric of str object at 0x0000002DC7EC2988>
>>> sms.isalpha
<built-in method isalpha of str object at 0x0000002DC7EC2988>
>>> s.startswith ("A")
True
>>> sms.startswith ("B")
False
>>> sms.capitalize
<built-in method capitalize of str object at 0x0000002DC7EC2988>
>>> sms.endswith (".")
True
>>> sms.replace("1,000","10,000")
'ABCD123. Confirmed! Hi Beatrice, your balance is 10,000.'
>>> sms[0:]
'ABCD123. Confirmed! Hi Beatrice, your balance is 1,000.'
>>> len(sms)
55
>>> len(akirachix)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    len(akirachix)
NameError: name 'akirachix' is not defined
>>> len(s)
9
>>> 
