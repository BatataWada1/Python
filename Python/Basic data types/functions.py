#python  functions

#greet("s") : def first then call

def greet(name):
    """This function takes user name greet him"""
    return "Good morning " + name

print(greet("mandar"))

print(greet.__doc__)


def my_func():
	x = 10
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)

def default_arg(name,msg="no msg for you"):
    print('HI ' + name + msg)

default_arg('mandar')
default_arg('nia', 'is it ')

l1= [1,23,4,5,6]
l2= ['mandar', 'kulkarni']
l3 = [0.1, 1.1]


def f3(*args):
    print('args' , args, type(args))
    for i in args:
        print(i)

f3(l1,l2,l3)

double = lambda x,y: x + y * 2 - y

print(double(2,3))

even = lambda x: (x % 2 == 0)

print(list(filter(even, l1)))

x = 'global'
print('before f4' , x)
def f4():
    global x
    x = x * 3
    print('inside f4', x)
f4()
print('outside f4', x)


def foo():
    x = 20
    def tar():
        #global x
        x = 40
        def bar():
            global x
            x = 30
        print('Before calling bar x in tar:' ,x)
        bar()
        print('After calling bar x in tar: ', x)
    print('Before calling tar x in foo:', x)
    tar()
    print('After calling tar xin foo: ', x)
foo()
print('x in global scope', x)


def out():
    x = "local"

    def inn():
        print("x in Inn before calling inner# ", x)

        def inner():
            nonlocal x
            x = "Inner"
            print("x in Inner# ", x)

        inner()
        print("x in In after calling inner# ",x )

    print("x in out before calling in# ", x)
    inn()
    print("x in out after calling in# ", x)

out()
print('x in global scope', x)


def g(*name):
    print("hi", name)

g('m','n')
