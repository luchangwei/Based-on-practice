
from functools import reduce
"""
'123.456'
digists = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,}
def da(i):
    return digists[i]
def vl(s):
    return list(map(da,s))
def fn(x,y):
    return 10*x + y
def str2float():
    return reduce(fn,vl(s))
s = '123456'
print(type(str2float()))

digists = {'0':float(0),'1':float(1),'2':float(2),'3':float(3),'4':float(4),'5':float(5),'6':float(6),}
def da(i):
    return digists[i]
def vl(s):
    return list(map(da,s))
def fn(x,y):
    return 10*x + y
def str2float():
    return reduce(fn,vl(s))
s = '123456'
print((str2float()))



"""




##   return list(map(da,positive))
#def fn(x,y):
 #   return 10*x + y
#def str2float():
#    return reduce(fn,vl(positive))
 #   print(reduce(fn,vl(positive)))

digists = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, }
def da(i):
    return digists[i]

def fn(x, y):
    return 10 * x + y


def str2float(s):
    split_1 = s.split(".")
    positive = split_1[0]
    negative = split_1[1]




    return reduce(fn, list(map(da, positive))) + reduce(fn, list(map(da, negative)))/pow(10,len(negative))


    #return str1float(positive) + str1float(negative)/pow(10,len(negative))
print(str2float("123.456"))