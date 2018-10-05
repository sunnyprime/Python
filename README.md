# Python
>Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991,Python has a design philosophy that emphasizes code readability, notably using significant whitespace


### Sample Code only:-

| CODE | PROPERTY |
| :---: | :---: |
| from module import function| from the module imported the function |
| import os | imort the directory |
| os.listdir() | show list of os directory |
| dir(os) | shows the directory of os |
| os.__dir__ | shows the directory of files
| help(glob2) | show the help of package |

### Method:-

| METHOD | METHOD'S FUNCTION | EXAMPLE |
| :---: | :--- | :---: |
| .lower() | Convert all string to lower | >>> First_name.lower() |
| .isalpha() | sure that it only contains letters | if len(original) > 0 and original.isalpha(): |




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

First_name="Sunny"
Last_name="Prime"
print(First_name +" "+ Last_name)
'Sunny Prime'
```

#### List[]
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

#### Tuple()
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
#### Dictonary{}
```
>>> dict={'Name':'Prime','Age':7,'Class':'First'}
>>> dict
{'Name': 'Prime', 'Age': 7, 'Class': 'First'}
>>> dict['Name']
'Prime'
>>> dict['Age']
7
```
#### Set{}
> In set Repation has been ignored.

```
>>> set={1,2,3,"Prime"}
>>> set
{1, 2, 3, 'Prime'}


>>> set={1,1,2,3,2,5,6,8,6,}
>>> set
{1, 2, 3, 5, 6, 8}
```

#### Condition

```
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#######
a and b are equal
```

#### While_Loop

```
i = 0
while i < 6:
  i += 1 
  if i == 3:
    continue
  print(i)

#####

1
2
4
5
6
```

#### For_loop

```
for x in range(6):
  print(x) 
  
####
0
1
2
3
4
5
```
#### Function
```
def my_function():
  print("Hello from a function")

my_function()

#####
Hello from a function
```

#### Lambda function

```
x = lambda a: a + 10
print(x(5))

####
15
```

#### Function Calling Function

```
def fun_one(n):
  return n * 5

def fun_two(m):
  return fun_one(m) + 7
```

#### Date Time
```
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

```


