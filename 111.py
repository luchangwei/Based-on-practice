""""
 1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \

a = [1]
b = []
a[0] = b[0]
a[-1] = b[-1]
a[0] + a[1] = b[1]
a[1] + a[2] = b[2]


n = 1
while n < max:

1   5   10  10  5   1




from enum import Enum
Month = Enum('Month',('Jan','Feb','Mar','Jun'))
#s = Month.Jan
#print(s)
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
print(Month.Jan)
"""
from enum import Enum,unique
@unique
class Gender(Enum):
    Male = 0
    Female = 1
class Student():
    def __init__(self,name,gender):
        if type(gender) == Gender:
            self.gender = gender
        else:
            raise TypeError("输入有误！！！")
s = Student('bob','Male')
