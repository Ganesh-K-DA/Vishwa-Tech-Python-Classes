
#global variable 

x=20
def my_function():
    #accessing global variable
    print(f"global variable x: {x}")
my_function()

y=10
def my_function():
    print(f"global variable y: {y}")
my_function()

z=5
def my_function():
    print(f"global variable z: {z}")
my_function()



#local variable

a=50
def my_function():
    #accesing local variable
    print(f"local variable a: {a}")
my_function()

b=40
def my_function():
    print(f"local variable b: {b}")
my_function()

c=30
def my_function():
    print(f"local variable c: {c}")
my_function()


#converting global variable to local variable

def my_function():
    #local variable (no longer using global a)
    a=20
    print(f"local variable a: {a}")
my_function()

def my_function():
    bb=100
    print(f"local variable bb: {bb}")
my_function()

def my_function():
    r=150
    print(f"local variable r: {r}")
my_function()


#converting local variable to global variable

def my_function():
    global e #declaring e as a global variabl
    e=80
    print(f"variable e inside function: {e}")
my_function()
# acccessing global variable e outside the function 
print(f"global variable e: {e}")


def my_function():
    global f
    f=30
    print(f"variable f inside the function: {f}")
my_function()
print(f"global variable f: {f}")


def my_function():
    global g
    g=60
    print(f"variable g insside the function: {g}")
my_function()
print(f"global variable g: {g}")

def my_function():
    global K
    K=90
    print(f"variable K inside the function: {K}")
my_function()
print(f"global variable K: {K}")

def my_function():
    global GK
    GK=1000
    print(f"variable inside the function GK: {GK}")
my_function()
print(f"global variable GK: {GK}")

