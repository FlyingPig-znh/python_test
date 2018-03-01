# -*- coding: utf-8 -*-
print (ord('A'))
print (ord('朱'))
print (chr(66))
print ('zhunenghui'.encode('ascii'))
print ('zhu能辉'.encode('utf_8'))
d={'zhu':45,'neng':54,'hui':36}
print(d['neng'])
d.pop('hui')
print(d)
a=[1,9,4,5,8,4]
a.sort()
print(a)
print(hex(455))
print(bin(0x1c7))

#8-30
def powern(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print (powern(5))
print(powern(6,4))

#函数参数
def play(name,age,**k):
    print("name:",name,"age:",age,"other:",k)
play('zhunenghui',23,high='180',weight=52)

def play2(name,age,*,job,addr):
    print('name:',name,'age:',age,job,addr)
play2('zhu',23,job='student',addr=1521)

def play3(name,age,*job,addr):
    print('name:',name,'age:',age,job,addr)
play3('zhu',23,'student',addr='1521')

#8-31
lis=[x * x for x in range(1,9) if x % 2 == 0]
print(lis)
d={'x':'a','y':'b','z':'c'}
print([key+'='+value for key, value in d.items()])
for k,v in d.items():
    print(k, '=', v)
l=['ZHU','NENG','HUI']
print([s.lower() for s in l])
print(isinstance(l, str))

#9-1
def fib(max):
    n, a, b =0, 0, 1
    while n<max:
        yield b
        a, b =b, a + b
        n=n+1
    return 'over'
g =fib(5)
while True:
    try :
        x=next(g)
        print(x)
    except StopIteration as e:
        print(e.value)
        break

#9-5
class screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,width):
        self._width = width
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,height):
        self._height = height
    @property
    def resolution(self):
        return (self._width + self._height) * 2

s=screen()
s._width=10
s._height=10
print(s.resolution)
