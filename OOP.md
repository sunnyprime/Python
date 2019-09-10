# Object Oriented Programming
## Class and Objects
```
class computer:
  def config(self):
    print("i5,16gb,1TB")
    
com1 = computer()
com2 = computer()
com1.config()
com2.config()

```
#### Output
```
>>i5,16gb,1TB
>>i5,16gb,1TB
```

### The __init__ method
The **__init__()** function is called automatically every time the class is being used to create a new object.

```
class computer():
  def __init__(self,cpu,ram):
    self.cpu = cpu
    self.ram = ram
    
  def config(self):
    print("config is", self.cpu,self.ram)
    
com1 = computer("i5",16)
com2 = computer("i7",32)
com1.config()
com2.config()
```

#### Output
```
config is i5 16
config is i7 32
```
