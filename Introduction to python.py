Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

#Introduction to Python

print("Hi Everyone")
Hi Everyone


#Language Tokens

x=10
y=20
print(x+y)
30
print(x<y)
True


#String Handling

name="Jessica"
print(name)
Jessica
print(name.upper())
JESSICA
print(name.lower())
jessica
print(name.replace("J","R"))
Ressica


#Native Datatype
>>> 
>>> fruits=["apple","grapes","watermelon"]
>>> print(fruits[3])
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(fruits[3])
IndexError: list index out of range
>>> 
>>> 
>>> #List
>>> 
>>> 
>>> #List
>>> 
>>> fruits=["apple","mango","orange"]
>>> print(fruits[2])
orange
>>> 
>>> print(fruits)
['apple', 'mango', 'orange']
>>> 
>>> 
>>> 
>>> #Tuple
>>> 
>>> my_tuple=("Python","GenAI")
>>> print(my_tuple)
('Python', 'GenAI')
>>> 
>>> 
>>> 
>>> #Indexing
>>> 
>>> name="jessica"
>>> name[2]
's'
>>> name[0]
'j'
>>> print(name[-1])
a
>>> 
>>> 
>>> #Slicing
>>> 
>>> name="Rachelle"
>>> print(name[0:4])
Rach
print(name[:4])
Rach
name[1:3:1]
'ac'
name[::-1]
'ellehcaR'




















#Ranging

for i in range(5)
SyntaxError: expected ':'
print
<built-in function print>


#Ranging

for i in range(5):
    print(i)

    
0
1
2
3
4

for i in range(1,11,2):
    print(i)

    
1
3
5
7
9

for i in range(2,11,2):
    print(i)

    
2
4
6
8
10
