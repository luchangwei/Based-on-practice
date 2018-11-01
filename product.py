
from functools import reduce


def prod(L):
    def oo(x,y):
        return x * y
    a = reduce(oo,L)

    return a
print(prod([3,5,7,9]))
