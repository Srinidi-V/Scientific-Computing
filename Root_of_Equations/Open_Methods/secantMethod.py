import math

#Function whose root is to be found
def f(x):
    return math.exp(-x) - x

#Function defining secant method
def Secant(x0,x1,e):
    x2 = float(x1 - (( ( f(x1) * (x1-x0) ) / ( f(x1) - f(x0) )   )))
    if abs(x2-x1) < e:
        return x2
    else:
        return Secant(x1,x2,e)

#Getting inputs and displaying the output
x0 = int(input("Enter first initial guess:"))
x1 = int(input("Enter second initial guess:"))
e = float(input("Enter error value allowed (epsilon): "))
ans = Secant(x0,x1,e)
print(ans)
print("root is: " + str(ans))