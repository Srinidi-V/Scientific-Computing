import math

#Function whose root is to be found
def f(x):
    return math.exp(-x) - x

# x=g(x) -> the g(x) function defined here
def g(x):     
    return math.exp(-x)

#Function defining fixed point iteration method
def fixedPtIter(x0,e):
    x1 = g(x0)
    if abs(x1-x0) < e:
        return x1
    else:
        return fixedPtIter(x1,e)

#Getting inputs and displaying the output
initial = int(input("Enter initial guess:"))
e = float(input("Enter error value allowed (epsilon): "))
ans = fixedPtIter(initial,e)
print(ans)
print("root is: " + str(ans))