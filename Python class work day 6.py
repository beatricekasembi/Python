Python 3.8.0a1 (tags/v3.8.0a1:e75eeb00b5, Feb  3 2019, 20:47:39) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> customer = {"name": "Beatrice", "balance" :1000000}
>>> customer 1 = {"name": "Beatrice", "balance" :1000000}
SyntaxError: invalid syntax
>>> customer1 = {"name": "Beatrice", "balance" :1000000}
>>> customer2 = {"name": "James", "balance" : 5000}
>>> customer2 = {"name": "James", "balance" : 5000}
>>> customer3 = {"name": "Michael", "balance" : 3000}
>>> customer4 = {"name": "Alice", "balance" : 50000}
>>> customer5 = {"name": "Stephen", "balance" : 1000}
>>> customers = [customer1,custome2,customer3,customer4,customer5]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    customers = [customer1,custome2,customer3,customer4,customer5]
NameError: name 'custome2' is not defined
>>> customers = [customer1,customer2,customer3,customer4,customer5]
>>> customers
[{'name': 'Beatrice', 'balance': 1000000}, {'name': 'James', 'balance': 5000}, {'name': 'Michael', 'balance': 3000}, {'name': 'Alice', 'balance': 50000}, {'name': 'Stephen', 'balance': 1000}]
>>> for customer in customers:
	sms="Hi {}, your balance is {}".format(customer["name"],customer["balance"])

	
>>> 
>>> sms
'Hi Stephen, your balance is 1000'
>>> print(sms)
Hi Stephen, your balance is 1000
>>> for customer in customers:
	sms="Hi {}, your balance is {}".format(customer["name"],customer["balance"])
	print(sms)

	
Hi Beatrice, your balance is 1000000
Hi James, your balance is 5000
Hi Michael, your balance is 3000
Hi Alice, your balance is 50000
Hi Stephen, your balance is 1000
>>> 
for customer in customers:
	loan=customer["balance"]/2.9
	print(loan)

	
344827.5862068966
1724.1379310344828
1034.4827586206898
17241.37931034483
344.82758620689657
>>> for customer in customers:
	sms="Hi {},kindly save with us to increase higher chances of loan. Your loan limit is {}".format(customer["name"],customer["loan"])
	print(sms)

	
Traceback (most recent call last):
  File "<pyshell#23>", line 2, in <module>
    sms="Hi {},kindly save with us to increase higher chances of loan. Your loan limit is {}".format(customer["name"],customer["loan"])
KeyError: 'loan'
>>> loan = customer ["balance"]/2.9
>>> for customer in customers:
	sms="Hi {},kindly save with us to increase higher chances of loan. Your loan limit is {}".format(customer["name"],customer["loan"])
	print(sms)

	
Traceback (most recent call last):
  File "<pyshell#26>", line 2, in <module>
    sms="Hi {},kindly save with us to increase higher chances of loan. Your loan limit is {}".format(customer["name"],customer["loan"])
KeyError: 'loan'
>>> for loan in customers:
	sms="Hi {},kindly save with us to increase higher chances of loan. Your loan limit is {}".format(customer["name"],customer["loan"])
	print(sms)

	
Traceback (most recent call last):
  File "<pyshell#28>", line 2, in <module>
    sms="Hi {},kindly save with us to increase higher chances of loan. Your loan limit is {}".format(customer["name"],customer["loan"])
KeyError: 'loan'
>>> for customer in customers:
	loan = customer["balance"]/2.9
	sms="Hi {},kindly save with us to increase higher chances of loan. Your loan limit is {}".format(customer["name"],customer["balance"][loan])
	print(sms)

	
Traceback (most recent call last):
  File "<pyshell#30>", line 3, in <module>
    sms="Hi {},kindly save with us to increase higher chances of loan. Your loan limit is {}".format(customer["name"],customer["balance"][loan])
TypeError: 'int' object is not subscriptable
>>> for customer in customers:
	loan = customer["balance"]/2.9
	sms="Hi {},kindly save with us to increase higher chances of getting a loan. Your balance is {}. You qualify for a loan upto {}".format(customer["name"],customer["balance"],loan)
	print(sms)

	
Hi Beatrice,kindly save with us to increase higher chances of getting a loan. Your balance is 1000000. You qualify for a loan upto 344827.5862068966
Hi James,kindly save with us to increase higher chances of getting a loan. Your balance is 5000. You qualify for a loan upto 1724.1379310344828
Hi Michael,kindly save with us to increase higher chances of getting a loan. Your balance is 3000. You qualify for a loan upto 1034.4827586206898
Hi Alice,kindly save with us to increase higher chances of getting a loan. Your balance is 50000. You qualify for a loan upto 17241.37931034483
Hi Stephen,kindly save with us to increase higher chances of getting a loan. Your balance is 1000. You qualify for a loan upto 344.82758620689657
>>> for x in range (0,10):
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
>>> if x%3==0:
	print(x)

	
9
>>> for x in range (0,10):
	if x%3==0
	
SyntaxError: invalid syntax
>>> for x in range (0,10):
	if x%3==0:
		print(x)

		
0
3
6
9
>>> for x in range (0,10):
	if x!=%==0:
		print(x)
		
SyntaxError: invalid syntax
>>> 
>>> for x in range (0,10):
	if x%3!=0:
		print(x)

		
1
2
4
5
7
8
>>> 
for x in range (0,10):
	if x%3!=0:
		print("{} is divisible by 3".format(x)

		      else:
		      
SyntaxError: invalid syntax
>>> for x in range (0,10):
	if x%3!=0:
		print("{} is divisible by 3".format(x)

	else:
		      
SyntaxError: invalid syntax
>>> for x in range (0,10):
	if x%3!=0:
		print("{} is divisible by 3".format(x)
	else:print
		      
SyntaxError: invalid syntax
>>> for x in range (0,10):
	if x%3!=0:
		print("{} is divisible by 3".format(x)
	else:
		      
SyntaxError: invalid syntax
>>> for x in range (0,10):
	if x%3!=0:
		print("{} is divisible by 3".format(x))
	else:
		print("{} is not divisible by 3".format(x))

		
0 is not divisible by 3
1 is divisible by 3
2 is divisible by 3
3 is not divisible by 3
4 is divisible by 3
5 is divisible by 3
6 is not divisible by 3
7 is divisible by 3
8 is divisible by 3
9 is not divisible by 3
>>> 
for x in range (0,10):
	if x%3==0:
		print("{} is divisible by 3".format(x))
	else:
		print("{} is not divisible by 3".format(x))

		
0 is divisible by 3
1 is not divisible by 3
2 is not divisible by 3
3 is divisible by 3
4 is not divisible by 3
5 is not divisible by 3
6 is divisible by 3
7 is not divisible by 3
8 is not divisible by 3
9 is divisible by 3
>>> 
for x in range (0,20):
	if x%3==0:
		print("{} is divisible by 3".format(x))
	elif x%5==0
		print("{} is divisible by 5".format(x))
	else:
		print("{} is not divisible by 3 or 5".format(x))
		
SyntaxError: invalid syntax
>>> 
>>> for x in range (0,20):
	if x%3==0:
		print("{} is divisible by 3".format(x))
	elif x%5==0:
		print("{} is divisible by 5".format(x))
	else:
		print("{} is not divisible by 3 or 5".format(x))

		
0 is divisible by 3
1 is not divisible by 3 or 5
2 is not divisible by 3 or 5
3 is divisible by 3
4 is not divisible by 3 or 5
5 is divisible by 5
6 is divisible by 3
7 is not divisible by 3 or 5
8 is not divisible by 3 or 5
9 is divisible by 3
10 is divisible by 5
11 is not divisible by 3 or 5
12 is divisible by 3
13 is not divisible by 3 or 5
14 is not divisible by 3 or 5
15 is divisible by 3
16 is not divisible by 3 or 5
17 is not divisible by 3 or 5
18 is divisible by 3
19 is not divisible by 3 or 5
>>> 
for x in range (0,20):
	if x%3==0:
		print("{} is divisible by 2".format(x))
	elif x%5==0:
		print("{} is divisible by 6".format(x))
	else:
		print("{} is not divisible by 3 or 5".format(x))

		
0 is divisible by 2
1 is not divisible by 3 or 5
2 is not divisible by 3 or 5
3 is divisible by 2
4 is not divisible by 3 or 5
5 is divisible by 6
6 is divisible by 2
7 is not divisible by 3 or 5
8 is not divisible by 3 or 5
9 is divisible by 2
10 is divisible by 6
11 is not divisible by 3 or 5
12 is divisible by 2
13 is not divisible by 3 or 5
14 is not divisible by 3 or 5
15 is divisible by 2
16 is not divisible by 3 or 5
17 is not divisible by 3 or 5
18 is divisible by 2
19 is not divisible by 3 or 5
>>> for x in range (0,20):
	if x%3==0:
		print("{} is divisible by 2".format(x))
	elif x%5==0:
		print("{} is divisible by 6".format(x))
	else:
		print("{} is not divisible by 2 or 6".format(x))

		
0 is divisible by 2
1 is not divisible by 2 or 6
2 is not divisible by 2 or 6
3 is divisible by 2
4 is not divisible by 2 or 6
5 is divisible by 6
6 is divisible by 2
7 is not divisible by 2 or 6
8 is not divisible by 2 or 6
9 is divisible by 2
10 is divisible by 6
11 is not divisible by 2 or 6
12 is divisible by 2
13 is not divisible by 2 or 6
14 is not divisible by 2 or 6
15 is divisible by 2
16 is not divisible by 2 or 6
17 is not divisible by 2 or 6
18 is divisible by 2
19 is not divisible by 2 or 6
>>> 
for x in range (0,100):
	if x%3==0:
		print("{} is divisible by 7".format(x))
	
	else:
		print("{} is not divisible by 7".format(x))

		
0 is divisible by 7
1 is not divisible by 7
2 is not divisible by 7
3 is divisible by 7
4 is not divisible by 7
5 is not divisible by 7
6 is divisible by 7
7 is not divisible by 7
8 is not divisible by 7
9 is divisible by 7
10 is not divisible by 7
11 is not divisible by 7
12 is divisible by 7
13 is not divisible by 7
14 is not divisible by 7
15 is divisible by 7
16 is not divisible by 7
17 is not divisible by 7
18 is divisible by 7
19 is not divisible by 7
20 is not divisible by 7
21 is divisible by 7
22 is not divisible by 7
23 is not divisible by 7
24 is divisible by 7
25 is not divisible by 7
26 is not divisible by 7
27 is divisible by 7
28 is not divisible by 7
29 is not divisible by 7
30 is divisible by 7
31 is not divisible by 7
32 is not divisible by 7
33 is divisible by 7
34 is not divisible by 7
35 is not divisible by 7
36 is divisible by 7
37 is not divisible by 7
38 is not divisible by 7
39 is divisible by 7
40 is not divisible by 7
41 is not divisible by 7
42 is divisible by 7
43 is not divisible by 7
44 is not divisible by 7
45 is divisible by 7
46 is not divisible by 7
47 is not divisible by 7
48 is divisible by 7
49 is not divisible by 7
50 is not divisible by 7
51 is divisible by 7
52 is not divisible by 7
53 is not divisible by 7
54 is divisible by 7
55 is not divisible by 7
56 is not divisible by 7
57 is divisible by 7
58 is not divisible by 7
59 is not divisible by 7
60 is divisible by 7
61 is not divisible by 7
62 is not divisible by 7
63 is divisible by 7
64 is not divisible by 7
65 is not divisible by 7
66 is divisible by 7
67 is not divisible by 7
68 is not divisible by 7
69 is divisible by 7
70 is not divisible by 7
71 is not divisible by 7
72 is divisible by 7
73 is not divisible by 7
74 is not divisible by 7
75 is divisible by 7
76 is not divisible by 7
77 is not divisible by 7
78 is divisible by 7
79 is not divisible by 7
80 is not divisible by 7
81 is divisible by 7
82 is not divisible by 7
83 is not divisible by 7
84 is divisible by 7
85 is not divisible by 7
86 is not divisible by 7
87 is divisible by 7
88 is not divisible by 7
89 is not divisible by 7
90 is divisible by 7
91 is not divisible by 7
92 is not divisible by 7
93 is divisible by 7
94 is not divisible by 7
95 is not divisible by 7
96 is divisible by 7
97 is not divisible by 7
98 is not divisible by 7
99 is divisible by 7
>>> for x in range (0,100):
	if x%7==0:
		print("{} is divisible by 7".format(x))
	else:
		print("{} is not divisible by 7".format(x))

		
0 is divisible by 7
1 is not divisible by 7
2 is not divisible by 7
3 is not divisible by 7
4 is not divisible by 7
5 is not divisible by 7
6 is not divisible by 7
7 is divisible by 7
8 is not divisible by 7
9 is not divisible by 7
10 is not divisible by 7
11 is not divisible by 7
12 is not divisible by 7
13 is not divisible by 7
14 is divisible by 7
15 is not divisible by 7
16 is not divisible by 7
17 is not divisible by 7
18 is not divisible by 7
19 is not divisible by 7
20 is not divisible by 7
21 is divisible by 7
22 is not divisible by 7
23 is not divisible by 7
24 is not divisible by 7
25 is not divisible by 7
26 is not divisible by 7
27 is not divisible by 7
28 is divisible by 7
29 is not divisible by 7
30 is not divisible by 7
31 is not divisible by 7
32 is not divisible by 7
33 is not divisible by 7
34 is not divisible by 7
35 is divisible by 7
36 is not divisible by 7
37 is not divisible by 7
38 is not divisible by 7
39 is not divisible by 7
40 is not divisible by 7
41 is not divisible by 7
42 is divisible by 7
43 is not divisible by 7
44 is not divisible by 7
45 is not divisible by 7
46 is not divisible by 7
47 is not divisible by 7
48 is not divisible by 7
49 is divisible by 7
50 is not divisible by 7
51 is not divisible by 7
52 is not divisible by 7
53 is not divisible by 7
54 is not divisible by 7
55 is not divisible by 7
56 is divisible by 7
57 is not divisible by 7
58 is not divisible by 7
59 is not divisible by 7
60 is not divisible by 7
61 is not divisible by 7
62 is not divisible by 7
63 is divisible by 7
64 is not divisible by 7
65 is not divisible by 7
66 is not divisible by 7
67 is not divisible by 7
68 is not divisible by 7
69 is not divisible by 7
70 is divisible by 7
71 is not divisible by 7
72 is not divisible by 7
73 is not divisible by 7
74 is not divisible by 7
75 is not divisible by 7
76 is not divisible by 7
77 is divisible by 7
78 is not divisible by 7
79 is not divisible by 7
80 is not divisible by 7
81 is not divisible by 7
82 is not divisible by 7
83 is not divisible by 7
84 is divisible by 7
85 is not divisible by 7
86 is not divisible by 7
87 is not divisible by 7
88 is not divisible by 7
89 is not divisible by 7
90 is not divisible by 7
91 is divisible by 7
92 is not divisible by 7
93 is not divisible by 7
94 is not divisible by 7
95 is not divisible by 7
96 is not divisible by 7
97 is not divisible by 7
98 is divisible by 7
99 is not divisible by 7
>>> for x in range (0,100):
	if x%7==0:
		print("{} is divisible by 7".format(x))

		
0 is divisible by 7
7 is divisible by 7
14 is divisible by 7
21 is divisible by 7
28 is divisible by 7
35 is divisible by 7
42 is divisible by 7
49 is divisible by 7
56 is divisible by 7
63 is divisible by 7
70 is divisible by 7
77 is divisible by 7
84 is divisible by 7
91 is divisible by 7
98 is divisible by 7
>>> 
for x in range (0,20):
	if x%3==0: and x%5==0:
		
SyntaxError: invalid syntax
>>> for x in range (0,20):
	if x%3==0:and x%5==0:
		
SyntaxError: invalid syntax
>>> for x in range (0,20):
	if x%3==0 and x%5==0:
		print(x)

		
0
15
>>> for x in range (0,20):
	if x%3==0 or x%5==0:
		print(x)

		
0
3
5
6
9
10
12
15
18
>>> true and true
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    true and true
NameError: name 'true' is not defined
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> False or False
False
>>> True or False
True
>>> True or True
True
>>> 
for x in range (900,950):
	if x%5==0:
		print("{} fizz".format(x))
	elif x%3==0:
		print("{} buzz".format(x))	
	elif x%5==0 and x%3==0:
		print("{} fizzbuzz".format(x))
	else:
		print("{} number".format(x))

		
900 fizz
901 number
902 number
903 buzz
904 number
905 fizz
906 buzz
907 number
908 number
909 buzz
910 fizz
911 number
912 buzz
913 number
914 number
915 fizz
916 number
917 number
918 buzz
919 number
920 fizz
921 buzz
922 number
923 number
924 buzz
925 fizz
926 number
927 buzz
928 number
929 number
930 fizz
931 number
932 number
933 buzz
934 number
935 fizz
936 buzz
937 number
938 number
939 buzz
940 fizz
941 number
942 buzz
943 number
944 number
945 fizz
946 number
947 number
948 buzz
949 number
>>> for x in range (900,950):
	if x%5==0 and x%3==0:
		print("{} fizzbuzz"
	elif x%5==0:
		print("{} fizz"
	elif x%3==0:
		print("{} buzz"
	else:
		print(x)
		      
SyntaxError: invalid syntax
>>> for x in range (900,950):
	if x%5==0 and x%3==0:
		print("{} fizzbuzz"
	if x%5==0:
		print("{} fizz"
	elif x%3==0:
		print("{} buzz"
	else:
		print(x)
		      
SyntaxError: invalid syntax
>>> for x in range (900,950):
	if x%5==0 and x%3==0:
		print("{} fizzbuzz"
	if x%5==0
		print("{} fizz"
	elif x%3==0:
		print("{} buzz"
	else:
		print(x)
		      
SyntaxError: invalid syntax
>>> for x in range (900,950):
	if x%5==0 and x%3==0:
		print("{} fizzbuzz"
	if x%5==0:
		print("{} fizz"
	elif x%3==0:
		print("{} buzz"
	else:
		print(x)
		      
SyntaxError: invalid syntax
>>> for x in range (900,950):
	if x%5==0 and x%3==0:
		print("{} fizzbuzz".format(x))
	if x%5==0:
		print("{} fizz".format(x))
	elif x%3==0:
		print("{} buzz".format(x))
	else:
		print(x)

		
900 fizzbuzz
900 fizz
901
902
903 buzz
904
905 fizz
906 buzz
907
908
909 buzz
910 fizz
911
912 buzz
913
914
915 fizzbuzz
915 fizz
916
917
918 buzz
919
920 fizz
921 buzz
922
923
924 buzz
925 fizz
926
927 buzz
928
929
930 fizzbuzz
930 fizz
931
932
933 buzz
934
935 fizz
936 buzz
937
938
939 buzz
940 fizz
941
942 buzz
943
944
945 fizzbuzz
945 fizz
946
947
948 buzz
949
>>> for x in range (900,950):
	if x%5==0 and x%3==0:
		print("fizzbuzz")
	if x%5==0:
		print("fizz")
	elif x%3==0:
		print("buzz")
	else:
		print(x)

		
fizzbuzz
fizz
901
902
buzz
904
fizz
buzz
907
908
buzz
fizz
911
buzz
913
914
fizzbuzz
fizz
916
917
buzz
919
fizz
buzz
922
923
buzz
fizz
926
buzz
928
929
fizzbuzz
fizz
931
932
buzz
934
fizz
buzz
937
938
buzz
fizz
941
buzz
943
944
fizzbuzz
fizz
946
947
buzz
949
>>> for x in range (900,950):
	if x%5==0 and x%3==0:
		print("fizzbuzz")
	elif x%5==0:
		print("fizz")
	elif x%3==0:
		print("buzz")
	else:
		print(x)

		
fizzbuzz
901
902
buzz
904
fizz
buzz
907
908
buzz
fizz
911
buzz
913
914
fizzbuzz
916
917
buzz
919
fizz
buzz
922
923
buzz
fizz
926
buzz
928
929
fizzbuzz
931
932
buzz
934
fizz
buzz
937
938
buzz
fizz
941
buzz
943
944
fizzbuzz
946
947
buzz
949
>>> 
