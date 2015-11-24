Python 2.7.10 (default, May 23 2015, 09:44:00) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ls -lha

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    ls -lha
NameError: name 'ls' is not defined
>>> a=1.2
>>> b=2.0
>>> print a.is_integer(), b.is_integer()
False True
>>> import math
>>> print round(a),math.ceil(a),math.floor(a)
1.0 2.0 1.0
>>> a="abcde"
>>> print a[0],a[4]
a e
>>> pront a[-1],a[-5]
SyntaxError: invalid syntax
>>> print a[-1],a[-5]
e a
>>> a="gachon usversity"
>>> print a[0:6],"AND",a[-9:]
gachon AND usversity
>>> print a[:]
gachon usversity
>>> print a[-50:50]
gachon usversity
>>> print a[::2],"AND",a[::-1]
gco sest AND ytisrevsu nohcag
>>> f=open("yesterday","r")

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    f=open("yesterday","r")
IOError: [Errno 2] No such file or directory: 'yesterday'
>>> f=open("yesterday",'r')

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    f=open("yesterday",'r')
IOError: [Errno 2] No such file or directory: 'yesterday'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> f=open("yesterday.txt","r")

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    f=open("yesterday.txt","r")
IOError: [Errno 2] No such file or directory: 'yesterday.txt'
>>> f=open("yesterday.txt",'r')

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    f=open("yesterday.txt",'r')
IOError: [Errno 2] No such file or directory: 'yesterday.txt'
>>> f=open("yesterday.txt",'r')

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    f=open("yesterday.txt",'r')
IOError: [Errno 2] No such file or directory: 'yesterday.txt'
>>> f = open("yesterday.txt",'r')

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    f = open("yesterday.txt",'r')
IOError: [Errno 2] No such file or directory: 'yesterday.txt'
>>> f = open("yesterday.txt",'r')

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    f = open("yesterday.txt",'r')
IOError: [Errno 2] No such file or directory: 'yesterday.txt'
>>> ================================ RESTART ================================
>>> 
red
green

Traceback (most recent call last):
  File "C:/1.txt/d.py", line 4, in <module>
    print lnd(colors)
NameError: name 'lnd' is not defined
>>> 
