def arrayCheck(nums):
    # CODE GOES HERE
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True

    return False
l1=[1, 1, 2, 3, 1]
l2=[1, 1, 2, 4, 1]
l3=[1, 1, 2, 1, 2, 3]
print(arrayCheck(l1))
print(arrayCheck(l2))
print(arrayCheck(l3))
# =======================================

def stringBits(mystring):
  # CODE GOES HERE
    result = ""

    for i in range(len(mystring)):
        if i%2 == 0:
            result = result + mystring[i]
    return result

print(stringBits('Hello'))
print(stringBits('Hi'))
print(stringBits('Heeololeo'))

# ==============================================
def end_other(a, b):
    a = a.lower()
    b = b.lower()

    return a[-(len(b)):] == b or a== b[-len(a):]

print(end_other('Hiabc', 'abc'))
# ====================================

def doubleChar(str):
    result = ''
    for char in str:
        result += char*2
    return result
print(doubleChar('The'))
