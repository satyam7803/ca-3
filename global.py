# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

# The global keyword makes the variable global.

def func():
    global x
    x=500
    print(x)

func()
print(x)      





# If you operate with the same variable name inside and outside of a function, 
# Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
# The function will print the local x, and then the code will print the global x:

a =300
def func1():
    a =200
    print(a)

func1()    # it will take local scope when called by function

print(a)  # it will take gloabal scope when called generally 



#to change the value global variable inside a function


y=1000
def change():
    global y
    y=1200
    print(y)
change()

print(y)



