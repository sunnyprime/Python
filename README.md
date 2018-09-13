# Python
Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, 
Python has a design philosophy that emphasizes code readability, notably using significant whitespace


###Sample Code:-
#### Output

```
>>> name="prime"
>>> print("Welcome ",name)
Welcome  prime

>>>print(type(name))          #Give the class of type name
<class 'str'>
```

#### Input
```
>>> f=float(input('Enter the float value:'))      #Float input
>>>m=int(input('Enter the integer:'))             # Integer Input
>>> msg=str(input("Enter the name"))              #String input
```

#### String
```
>>> a="This is prime"
>>> a[0:6]
'This i'
>>> a[:5]
'This '
>>> a[5:]
'is prime'
```

#### List
```
>>> list=['Phy','Chem',1999,2000]
>>> list
['Phy', 'Chem', 1999, 2000]
>>> list[2]
1999
>>> list[2] = 2000                                #Update list
>>> list
['Phy', 'Chem', 2000, 2000]
>>> del list[2]                                   #delete list
>>> list
['Phy', 'Chem', 2000]
```

#### Tuple
> Tupple are immutable(Cannot be deleted or edited).But we can add two tupples.

```
>>> tup1=('phy','chem','bio',1997,2000)
>>> tup1
('phy', 'chem', 'bio', 1997, 2000)
>>> tup2=('Prime','India')
>>> tup2
('Prime', 'India')
>>> tup3=tup1+tup2
>>> tup3
('phy', 'chem', 'bio', 1997, 2000, 'Prime', 'India')
```
