'''

someone@gmail.com
bill.gates@microsoft.com
# -*- coding: utf-8 -*-
import re

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


import re
def is_valid_email(addr):
    if re.match(r'\w*@microsoft.com$', addr):
        return True
    elif re.match( r'\w+@gmail.com$', addr):
        return True
    else:
        return False
print(is_valid_email('qwedewd@gmail.com'))
print(is_valid_email('qqeee@microsoft.com'))

import re
def name_of_email(addr):
   if '<' in addr:
        m = re.match(r'^\<(\w+?)\>@(\w+).(\w+)$',addr)
        return m.group(1)
   else:
        m = re.match(r'(\w+?)@(\w+)\.(\w+)$',addr)
        return m.group(1)
print(name_of_email("bob@189.cn"))
print(name_of_email("<bobtripbob>@189.cn"))



dict = {"a":1,"b":3,"c":5,"d":6,"e":3,"f":2}
a = sorted(dict.items(),key = lambda a:a[1],reverse=True )
print(list(a))

import time
print(time.strftime('%y %a %b %d %a %I:%M %p %Y'))

class Fib():
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
            return a
        elif isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b , a + b
            return L

f = Fib().

x = 1
def change(a):
    global x
    x += 1
    print (x)
change(x)


a = [1,3,4,5,7787,8,9,0,]
b = list(enumerate(a))
c= sorted(b,key=lambda x:x[0],reverse=True)
d = []
for aa in c:
    d.append(aa[1])
print(d)

b,a= 1,0
c = 1
while c <=39:

    a,b = b,a + b
    c += 1
print(a)
'''

