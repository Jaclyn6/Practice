Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #tuple lets go!
>>> #tuple is Immutable Type, But It's possible that using like List. But we need to understand tuple is immutable
>>> 
>>> 
>>> a= (1,2,3)
>>> a
(1, 2, 3)
>>> type(a)
<class 'tuple'>
>>> or
SyntaxError: invalid syntax
>>> b= 1,2,3,4
>>> type(b)
<class 'tuple'>
>>> b
(1, 2, 3, 4)
>>> a=(1)
>>> a
1
>>> type(a)
<class 'int'>
>>> a=(1,)
>>> tpye(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tpye(a)
NameError: name 'tpye' is not defined
>>> a
(1,)
>>> type(a)
<class 'tuple'>
>>> a=1,
>>> a
(1,)
>>> type(a)
<class 'tuple'>
>>> a+b
(1, 1, 2, 3, 4)
>>> a
(1,)
>>> b
(1, 2, 3, 4)
>>> b[0]
1
>>> b[0]=7
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    b[0]=7
TypeError: 'tuple' object does not support item assignment
>>> 
>>> #Tuple Packing
>>> a= 1,2,3
>>> a
(1, 2, 3)
>>> #Tuple UnPacking
>>> one, two, three = a
>>> one
1
>>> two
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    wo
NameError: name 'wo' is not defined
t
>>> two
2
>>> three
3
>>> 
>>> 
>>> #Dictionary!!
>>> dic = {}
>>> dic['파이썬']='www.python.org'
>>> dic['네이버']='www.naver.com'
>>> dic['daum']='www.daum.net'
>>> 
>>> dic['파이썬']
'www.python.org'
>>> type(dic)
<class 'dict'>
>>> #dictionary as fast as list for explore
>>> #dictionary use hash mapping
>>> dic
{'파이썬': 'www.python.org', '네이버': 'www.naver.com', 'daum': 'www.daum.net'}
>>> dic.keys()
dict_keys(['파이썬', '네이버', 'daum'])
>>> dic.values()
dict_values(['www.python.org', 'www.naver.com', 'www.daum.net'])
>>> 'www.naver.com' in dic
False
>>> 'www.naver.com' in dic.values()
True
>>> dic
{'파이썬': 'www.python.org', '네이버': 'www.naver.com', 'daum': 'www.daum.net'}
>>> '네이버' in dic
True
>>> 'www.naver.com' in dic
False
>>> 'www.python.org' in dic
False
>>> 'daum' in dic
True
>>> dic.pop()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    dic.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> dic.pop('파이썬')
'www.python.org'
>>> dic
{'네이버': 'www.naver.com', 'daum': 'www.daum.net'}
>>> dic.clear()
>>> dic
{}
>>> 
>>> 
>>> #bool
>>> a= 3>2
>>> a
True
>>> not Ture
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    not Ture
NameError: name 'Ture' is not defined
>>> not True
False
>>> not false
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    not false
NameError: name 'false' is not defined
>>> not False
True
>>> not 0
True
>>> not -1
False
>>> not None
True
>>> None
>>> none
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    none
NameError: name 'none' is not defined
>>> None
>>> a= None
>>> a
>>> not ''
True
>>> not 'a'
False
>>> # empty is False!
>>> bool(None)
False
>>> 
