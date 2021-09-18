#Add
def add(x,y):
    return x+y
#Subtract
def subtract(x,y):   #on master branch
    return x-y
#Multiply
def multiply(x,y):   #on bug2 branch
    return x*y
#Divide
def divide(x,y):     #on Bug3 branch
    if y == 0:
	return divide by zero error
    else:
	return x/y

# Square implementation
def square(x):
    return x*x