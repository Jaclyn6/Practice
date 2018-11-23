Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> asdyasdf
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    asdyasdf
NameError: name 'asdyasdf' is not defined
>>> 
>>> 
>>> a
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a
NameError: name 'a' is not defined
a
>>> 
>>> 
>>> a="""안녕하세요 파이썬
좋아요 """
>>> a
'안녕하세요 파이썬\n좋아요 '
>>> 
>>> 
>>> '안' in a
True
>>> a[:4]
'안녕하세'
>>> a[2:]
'하세요 파이썬\n좋아요 '
>>> len(a)
14
>>> 
>>> a.startswith('안녕')
True
>>> a.rfind('녕')
1
>>> a.count('요')
2
>>> '1234'.isnumeric()
True
>>> 
>>> 
>>> b='apple,loopy,superbee'
>>> c= a.split(',')
>>> type(c)
<class 'list'>
>>> 
>>> 
>>> c
['안녕하세요 파이썬\n좋아요 ']
>>> 
>>> 
>>> c=b.split(',')
>>> 
>>> 
>>> c
['apple', 'loopy', 'superbee']
>>> d="안녕 내이름은 {0}고 나이는 {1}이야."
>>> 
>>> 
>>> d.format("",14)
'안녕 내이름은 고 나이는 14이야.'
>>> d
'안녕 내이름은 {0}고 나이는 {1}이야.'
>>> print("hi" + math.e)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print("hi" + math.e)
NameError: name 'math' is not defined
>>> print("hi" + str(math.e))
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print("hi" + str(math.e))
NameError: name 'math' is not defined
>>> import math
>>> print("hi" + math.e)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print("hi" + math.e)
TypeError: can only concatenate str (not "float") to str
>>> print("hi"+str(math.e))
hi2.718281828459045
>>> a=[1,2,3,4,5]
>>> b=[5,6,7,8]
>>> a+b
[1, 2, 3, 4, 5, 5, 6, 7, 8]
>>> a.append(4)
>>> a
[1, 2, 3, 4, 5, 4]
>>> a.insert(2,10)
>>> a
[1, 2, 10, 3, 4, 5, 4]
>>> 
