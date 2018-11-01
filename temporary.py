
'''


list_num = ['0','1335','1654984','wquhwu']
def odd():
    for n in range(1,201):
        n =str(n)
        return n
        print(n)
        list_num.append(n)
def palindrome(n):
   # if len(n) == 1:
     #   return Truea
    if len(n) == 2:
        n[0] == n[1]
    if len(n) == 3:
        n[0] == n[2]
def is_palindrome():

    aa = filter(palindrome(odd()),list_num)
    print(aa)

is_palindrome()



def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x: x % n > 0
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break


list_num = ["122","222","123","134"]
def odd():
    for n in range(1,201):
        n  = str(n)
        list_num.append(n)
def palindrome(n):
    return n == int(str(n)[::-1])
def is_palindrome():

        n = str(222)
        aa = list(filter(palindrome(n),list_num))

        return aa

print(is_palindrome())


def counterA():
    def fla(i):
        def num():
            return i + 1
        return num
    time = []
    for n in range(1,6):
        time.append(fla(n))
    return time
a = counterA()
print(a)







def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    print(fs)
    return fs

f1,f2,f3 = count()


import functools
max2 = functools.partial(max, 10)
#a = [1,2,3,4,5,6,7,8]
print(max2(1,2,3,4,5,6,77))




class Student():
    count = 0
    def __init__(self,name):
        self.name = name
        Student.count += 1

a = Student('bob')
print(a.name)
print(Student.count)
b = Student('Lisa')
print(b.name)
print(b.count)





class Screen():
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height = value
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width = value
    @property
    def resolution(self):
        self.resolution = self.height * self.width
        return self.resolution


s = Screen
s.height = 222
s.width = 213

print(s.height)
print(s.width)
print(s.resolution)

class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width
s = Screen
s.height = 222
s.width = 213

print(s.height)
print(s.width)
print(s.resolution)

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,width):
        self._width = width

    @property
    def height(self):
        return self._height

    @width.setter
    def height(self,height):
        self._height = height

    @property
    def resolution(self):
        return self._width * self._height
s = Screen
s.height = 222
s.width = 213
s.resolution = 12423423
print(s.height)
print(s.width)
print(s.resolution)

class Screen():
    def __init__(self,height,width):
        self.heihght = height
        self.width = width
        self.resolution = height * width
c = Screen(123,456)
print(c.resolution)
'''
