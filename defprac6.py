Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def dicdeftest(**players):
	for k in players.keys():
		print('{0} = {1}'.format(k,players(k]))
		
SyntaxError: invalid syntax
>>> 
>>> def dicdeftest(**players):
	for k in players.keys():
		print('{0} = {1}'.format(k,players[k]))

		
>>> dicdeftest(나는=gk)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    dicdeftest(나는=gk)
NameError: name 'gk' is not defined
>>> dicdeftest(카시야스='gk',유벤투스='찔밥')
카시야스 = gk
유벤투스 = 찔밥
>>> def print_args(argc, *argv):
	for i in range(argc):
		print(argv[i])

		
>>> print_args(3,a,2,3)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print_args(3,a,2,3)
NameError: name 'a' is not defined
>>> print_args(3,24,5,6_
	       
SyntaxError: invalid token
>>> print_args(3,24,5,6)
	       
24
5
6
>>> print_args(argc=3,24,5,6) #일반 매개변수가 가변매개변수 앞에 있을 경우 키워드 매개변수 사용 불가(argc=3)
	       
SyntaxError: positional argument follows keyword argument
>>> def print_args(*argv,argc): #일반 매개변수가 가변매개변수 뒤에 있을 경우
	       for i in range(argc):
		       print(argv[i])

	       
>>> print_args(1,2,3,4,4)
	       
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print_args(1,2,3,4,4)
TypeError: print_args() missing 1 required keyword-only argument: 'argc'
>>> print_args(1,2,3,4,argc=4) #일반 매개변수가 가변 매개변수 뒤에 있을 경우키워드 매개변수를 사용해야 함
	       
1
2
3
4
>>> def scope_test():
	       global a = 1
	       
SyntaxError: invalid syntax
>>> def scope_test():
	       global a
	       a = 1
	       print('a:{0}'.format(a))

	       
>>> a = 0
	       
>>> a
	       
0
>>> scope_test
	       
<function scope_test at 0x020CFBB8>
>>> scopee_test()
	       
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    scopee_test()
NameError: name 'scopee_test' is not defined
>>> scope_test()
	       
a:1
>>> a
	       
1
>>> #global은 함수내에서 전역변수를 참조하게 함
	       
>>> 
	       
>>> def factorial(n):
	       if n == 0:
		       return 1
	       elif n > 0:
		       return factorial(n-1)*n

	       
>>> factorial(5
	      )
	       
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    actorial(5
NameError: name 'actorial' is not defined
>>> factorial(5)
	     
120
>>> factorial(110
	      )
	     
15882455415227429404253703127090772871724410234473563207581748318444567162948183030959960131517678520479243672638179990208521148623422266876757623911219200000000000000000000000000
>>> factorial(35
	      )
	     
10333147966386144929666651337523200000000
>>> p = factorial()
	     
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    p = factorial()
TypeError: factorial() missing 1 required positional argument: 'n'
>>> p = factorial
	     
>>> p(5)
	     
120
>>> dic=[]
	     
>>> type(dic)
	     
<class 'list'>
>>> dic = {}
	     
>>> type(dic)
	     
<class 'dict'>
>>> dic['팩토리얼']=factorial
	     
>>> dic['팩토리얼
	
SyntaxError: EOL while scanning string literal
>>> dic['팩토리얼'](30)
	
265252859812191058636308480000000
>>> a
