#global variable is variable which is outside the function is called as global variable
# local variable is a variable which is inside the function is called as local variable
 
#converting global variable to local variable
apple="fruit"
def myfunction():
    print("apple is" +  apple)
    global variable
    variable="local variable"
    festival="dasara"
    print(festival)
myfunction()
print(variable)
print(apple)

m="data_analytics" #global variable
def myfunction():
    print(m+"is intresting course to learn")
    gani="python is fantastic" #local variable
    print(gani)
myfunction()

#converting local variable to global variable
def my_local():
    global data #declare data as a global variable
    data=10 #now, data is a global variable

my_local()
print(data)

def harish():
    global gani
    gani="harish friends"
    
harish()
print(gani)
