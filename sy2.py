import functools
import sys
#9-1
d = [x * x for x in range(1,5)]
def f(x):
    return x * x
print(d)
t = map (f , iter(d))
print (list(t))

#9-2
#按字母正向排序
print(sorted(['zhu','neng','hui','chen','zheng'],key=str.lower))
#.....逆序
print(sorted(['zhu','neng','hui','chen','zheng'],key=str.lower,reverse=True))


def by_name(l):
    return l[0]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L , key=by_name))

a = [1,2,7,6,3,5,4]
a.sort()
print (a)

#def count():
#    fs = []
#    for i in range (1, 4):
#        def f():
#            return i * i
#        fs.append(f)
#    return fs

#9-3使用装饰器输出日志
def  log(fc):
    def w(*args, **kw):
        print('call %s():' %fc.__name__)
        return fc(*args, **kw)
    return w
@log    #@语法
def by_name(l):
    return l[0]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L , key=by_name))
#偏函数
int2 = functools.partial(int, base=16)
print(int2('a0b54'))


def test():
    args=sys.argv
    if len(args)==1:
        print('hello')
    elif len(args)==2:
        print('hello,%s' %args[1])
    else:
        print('Error,too many argument')
if __name__=='__main__':
    test()

#图片缩小
#from PIL import Image
#im=Image.open(r'D:\照片\123.png')
#print(im.format,im.size,im.mode)
#PNG (1024, 768) RGBA
#im.thumbnail((200,100))
#im.convert('RGB').save(r'D:\照片\thumb.jpg','JPEG')

#9-4类学习
class student(object):
    def __init__(self,name,score,age):
        self.__name=name
        self.__score=score
        self.__age=age
    def get_name(self):
        return self.__name
    @property
    def get_score(self):
        return self.__score
    def get_age(self):
        return self.__age
    def get_grade(self):
        if self.__score>=90:
            print("A")
        elif self.__score<60:
            print("C")
        else:
            print("B")
 #   @set_score.setter
    def set_score(self,score):
        if 0<=score<=100:
            self.__score=score
        else:
            raise ValueError('bad value')
znh=student('znh',99,23)
print(znh.get_score())
znh.get_grade()
znh.set_score(66)
print(znh.get_score())
znh.get_grade()
