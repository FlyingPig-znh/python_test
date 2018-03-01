#char to int
from functools import reduce
def chartoint(char):
    def fn(x, y):
        return x * 10 + y
    def char2int(s):
        return {'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7':\
         7,'8': 8,'9': 9}[s]
    return reduce (fn,map(char2int, char))
    #same as
    #return reduce (lambda x, y :x * 10 + y,map(char2int, char ))
#test
print(chartoint ('36524'))

#规范输入字符首字母大写
def normalize(name):
    return name.capitalize()
#test
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#浮点字符串转浮点数

def str2float(n):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7':\
         7, '8': 8, '9': 9}[s]
    return reduce(lambda x ,y :  x * 10 + y, map(char2num,n.split('.')[0]))\
     + reduce(lambda x ,y :  x * 10 + y, map(char2num,n.split('.')[1])) / (\
     10 ** len(n.split('.')[1]))

print("str2float('123.456') = ", str2float('123.456'))

#筛选回数
def ispalindrome(n):
    n = str(n)
    return n == n[::-1]
print(list(filter(ispalindrome,range(1000))))     
