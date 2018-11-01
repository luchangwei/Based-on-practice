L1  = ['hello','world',18,None]
L2 = [x for x in L1 if isinstance(x,str)]

print(L2)
L3 = (x for x in range(1,10))

print(L3)
def fib(n):
    a = 0
    b = 1
    i = 0
    while i < n :
        yield b
       # b = a + b
       # a = b
        a,b = b,a+b
        i += 1
    return  'done'
a = fib(8)

while True:
    try:
        x = next(a)
        print(x)
    except StopIteration as e:
        print(e)
        break