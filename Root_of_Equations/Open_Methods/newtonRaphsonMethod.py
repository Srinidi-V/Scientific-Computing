import math

#Function whose root is to be found
def f(x):
    return math.exp(-x) - x

#Derivative of that function -> df/dx
def g(x):     
    return -1*math.exp(-x) - 1

#Function defining newton raphson method
def NRMethod(x0,e):
    x1 = x0 - (f(x0)/g(x0))
    if abs(x1-x0) < e:
        return x1
    else:
        return NRMethod(x1,e)

#Getting inputs and displaying the output
initial = int(input("Enter initial guess:"))
e = float(input("Enter error value allowed (epsilon): "))
ans = NRMethod(initial,e)
print(ans)
print("root is: " + str(ans))